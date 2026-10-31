#!/usr/bin/env python3
from pathlib import Path
import json
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
renderer = ROOT / "scripts/render-github-fork-script"
runner = ROOT / "scripts/run-pipeline-legacy.py"

cases = [
    (
        ("micropython", "micropython", "dilapidated-shed"),
        """gh auth status --hostname github.com
gh repo fork micropython/micropython --org dilapidated-shed --clone=false
gh api repos/dilapidated-shed/micropython --jq '{full_name, fork, parent: .parent.full_name, source: .source.full_name}'
""",
    ),
    (
        ("example-owner", "tiny-runtime", "example-org"),
        """gh auth status --hostname github.com
gh repo fork example-owner/tiny-runtime --org example-org --clone=false
gh api repos/example-org/tiny-runtime --jq '{full_name, fork, parent: .parent.full_name, source: .source.full_name}'
""",
    ),
]

for argv, expected in cases:
    rendered = subprocess.run(
        [sys.executable, str(renderer), *argv],
        capture_output=True,
        text=True,
    )
    assert rendered.returncode == 0, rendered.stderr
    assert rendered.stdout == expected
    assert " sh " not in f" {rendered.stdout} "
    assert "--fork-name" not in rendered.stdout
    assert "--clone=false" in rendered.stdout

bad = subprocess.run(
    [sys.executable, str(renderer), "owner;bad", "repo", "org"],
    capture_output=True,
    text=True,
)
assert bad.returncode != 0

with tempfile.TemporaryDirectory() as td:
    completed = subprocess.run(
        [
            sys.executable,
            str(runner),
            "github-fork-script",
            "--param", "source_owner=micropython",
            "--param", "repository=micropython",
            "--param", "destination_org=dilapidated-shed",
            "--runs-root", td,
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert completed.returncode == 0, completed.stderr
    run_dirs = list(Path(td).iterdir())
    assert len(run_dirs) == 1
    stdout = (run_dirs[0] / "01-render-script" / "stdout.bin").read_text()
    assert stdout == cases[0][1]
    receipt = json.loads((run_dirs[0] / "receipt.json").read_text())
    assert receipt["status"] == "PASS"
    assert receipt["qualified_operation"] is False
    assert receipt["acceptance_scope"] == "caller-supplied-command-execution"

print("generic GitHub fork script renderer: PASS")
