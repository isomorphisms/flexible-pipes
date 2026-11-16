#!/usr/bin/env python3
"""Offline characterization of the retrieved Flexible Pipes runner, not a new runner."""
from __future__ import annotations
import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('runner', type=Path, help='Exact retrieved scripts/run-pipeline file')
parser.add_argument('evidence_directory', type=Path, help='New directory; previous evidence is never overwritten')
args = parser.parse_args()
SOURCE = args.runner.resolve(strict=True)
OUT = args.evidence_directory.resolve()
EXPECTED_BLOB = '45e7b509d86a14b6352bb61680b7580036ba2ac4'
PIN = '9775aa324f523cbc6c758e89461915484a5a0fc7'
b = SOURCE.read_bytes()
blob = hashlib.sha1(b'blob ' + str(len(b)).encode() + b'\0' + b).hexdigest()
if blob != EXPECTED_BLOB:
    raise SystemExit('Source bytes do not match the observed upstream Git blob')
if OUT.exists():
    raise SystemExit('Refusing to overwrite previous evidence: ' + str(OUT))
OUT.mkdir()
seed = OUT / 'seed'
(seed / 'scripts').mkdir(parents=True)
(seed / 'pipelines').mkdir()
shutil.copyfile(SOURCE, seed / 'scripts/run-pipeline')
(seed / 'scripts/gate.py').write_text(
    "from pathlib import Path\nimport sys\nsys.exit(0 if Path('input.txt').read_text() == 'allowed' else 23)\n")
(seed / 'scripts/effect.py').write_text(
    "from pathlib import Path\np=Path('effect-count.txt')\np.write_text(str((int(p.read_text()) if p.exists() else 0)+1))\nprint('fixture effect')\n")
(seed / 'input.txt').write_text('allowed')
spec = {
    'schema_version': 1, 'name': 'boundary-fixture',
    'required_stages': ['policy-check', 'fixture-effect'],
    'stages': [
        {'name': 'policy-check', 'kind': 'command', 'argv': [sys.executable, 'scripts/gate.py']},
        {'name': 'fixture-effect', 'kind': 'command', 'argv': [sys.executable, 'scripts/effect.py']}
    ]
}
(seed / 'pipelines/boundary-fixture.json').write_text(json.dumps(spec, sort_keys=True)+'\n')
git = shutil.which('git')
if not git:
    raise SystemExit('git missing: cannot produce the synthetic fixed-HEAD fixture')
env = {'PATH': os.defpath, 'HOME': str(OUT / 'home'), 'LANG': 'C.UTF-8',
       'GIT_CONFIG_NOSYSTEM': '1', 'GIT_CONFIG_GLOBAL': '/dev/null',
       'GIT_AUTHOR_NAME': 'Offline fixture', 'GIT_AUTHOR_EMAIL': 'fixture@example.invalid',
       'GIT_COMMITTER_NAME': 'Offline fixture', 'GIT_COMMITTER_EMAIL': 'fixture@example.invalid',
       'GIT_AUTHOR_DATE': '2026-10-08T16:13:00Z', 'GIT_COMMITTER_DATE': '2026-10-08T16:13:00Z'}
Path(env['HOME']).mkdir()
for args in (['init', '-q'], ['add', '.'], ['commit', '-qm', 'Synthetic offline fixture; not upstream history']):
    subprocess.run([git, '-C', str(seed), *args], env=env, check=True, capture_output=True)
fixture_head = subprocess.check_output([git, '-C', str(seed), 'rev-parse', 'HEAD'], env=env, text=True).strip()
rows = []
cases = [
    ('valid-control', 'PASS', 0, 1),
    ('failing-gate-control', 'FAIL', 1, 0),
    ('missing-stage-retained-requirement', 'REJECTED_BEFORE_RECEIPT', 2, 0),
    ('stage-and-requirement-removed', 'PASS', 0, 1),
    ('gate-file-replaced-at-same-head', 'PASS', 0, 1),
    ('source-revision-unavailable', 'PASS', 0, 1)
]
for name, expected_status, expected_exit, expected_effects in cases:
    work = OUT / name
    shutil.copytree(seed, work)
    if name in {'failing-gate-control', 'stage-and-requirement-removed', 'gate-file-replaced-at-same-head'}:
        (work / 'input.txt').write_text('forbidden')
    if name in {'missing-stage-retained-requirement', 'stage-and-requirement-removed'}:
        variant = json.loads(json.dumps(spec))
        variant['stages'] = variant['stages'][1:]
        if name == 'stage-and-requirement-removed':
            del variant['required_stages']
        (work / 'pipelines/boundary-fixture.json').write_text(json.dumps(variant, sort_keys=True)+'\n')
    if name == 'gate-file-replaced-at-same-head':
        (work / 'scripts/gate.py').write_text('print("checked")\n')
    if name == 'source-revision-unavailable':
        shutil.rmtree(work / '.git')
    run_env = dict(env)
    run_env['HOME'] = str(work / 'fresh home')
    Path(run_env['HOME']).mkdir()
    child = subprocess.run([sys.executable, str(work / 'scripts/run-pipeline'), 'boundary-fixture',
                            '--runs-root', str(work / 'receipts')],
                           cwd=run_env['HOME'], env=run_env, capture_output=True, timeout=15)
    (work / 'runner.stdout').write_bytes(child.stdout)
    (work / 'runner.stderr').write_bytes(child.stderr)
    receipts = list((work / 'receipts').glob('*/receipt.json'))
    receipt = json.loads(receipts[0].read_text()) if receipts else {}
    status = receipt.get('status', 'REJECTED_BEFORE_RECEIPT')
    effect_path = work / 'effect-count.txt'
    effects = int(effect_path.read_text()) if effect_path.exists() else 0
    row = {'case': name, 'observed_status': status, 'exit': child.returncode,
           'fixture_effect_count': effects, 'repository_commit': receipt.get('repository_commit'),
           'pipeline_sha256': receipt.get('pipeline_sha256'),
           'stage_names': [s['name'] for s in receipt.get('stages',[])],
           'receipt': str(receipts[0].relative_to(OUT)) if receipts else None}
    row['characterization_matches'] = (status, child.returncode, effects) == (expected_status, expected_exit, expected_effects)
    rows.append(row)
    print(json.dumps(row, sort_keys=True))
summary = {'source_repository': 'isomorphisms/flexible-pipes', 'observed_upstream_ref': PIN,
           'source_path': 'scripts/run-pipeline', 'source_git_blob': blob,
           'source_sha256': hashlib.sha256(b).hexdigest(), 'synthetic_fixture_head': fixture_head,
           'scope': 'Offline isolated host characterization, simulated local effects only; no hosted workflow, network, model inference, phone test, or GitHub mutation',
           'cases': rows}
(OUT / 'summary.json').write_text(json.dumps(summary, indent=2, sort_keys=True)+'\n')
assert all(r['characterization_matches'] for r in rows), 'Unexpected observation; inspect retained evidence'
assert rows[0]['pipeline_sha256'] == rows[4]['pipeline_sha256']
assert rows[0]['repository_commit'] == rows[4]['repository_commit'] == fixture_head
assert rows[5]['repository_commit'] is None
print('Six characterization cases matched; three controls and three acceptance-boundary counterexamples retained.')
