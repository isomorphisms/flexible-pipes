#!/usr/bin/env python3
"""FP must execute Kitchen's exact repository-pin preflight, not a copied policy."""
from __future__ import annotations

import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
PINNED_KITCHEN_SHA = "f37a33ac9693623cfafc16fb68c4eb10f83cf961"
KITCHEN_SCRIPT = ROOT / "kitchen/tasks/github-organization-pin-preflight/1.py"
KITCHEN_TEST = ROOT / "kitchen/tests/github-organization-pin-preflight.py"
PIPELINE = ROOT / "pipelines/github-organization-pin-preflight.json"
RUNNER = ROOT / "scripts/run-pipeline"

spec = json.loads(PIPELINE.read_text())
assert spec["name"] == "github-organization-pin-preflight"
assert spec["required_stages"] == ["eligibility"]
assert spec["stages"][0]["argv"] == [
    "python3", "kitchen/tasks/github-organization-pin-preflight/1.py",
    "{{organization}}", "{{repositories}}",
]
assert KITCHEN_SCRIPT.is_file() and KITCHEN_TEST.is_file()
head = subprocess.run(
    ["git", "-C", str(ROOT / "kitchen"), "rev-parse", "HEAD"],
    text=True, capture_output=True, check=True,
).stdout.strip()
assert head == PINNED_KITCHEN_SHA, (head, PINNED_KITCHEN_SHA)

fixture = subprocess.run(
    [sys.executable, str(KITCHEN_TEST)], text=True,
    capture_output=True, check=False,
)
assert fixture.returncode == 0, fixture.stdout + fixture.stderr

# Fake gh in the FP test, while the Kitchen fixture independently exercises its
# full negative matrix. The FP runner may never mutate a GitHub repository.
GH_STUB = """#!/usr/bin/env python3
import json
import sys
from pathlib import Path
import os
args = sys.argv[1:]
Path(os.environ["PIN_CALLS"]).open("a").write(json.dumps(args) + "\\n")
if args == ["auth", "status", "--hostname", "github.com"]:
    sys.exit(0)
if args == ["api", "repos/isomorphismes/wegert"]:
    print(json.dumps({"id": 1341206906, "full_name": "isomorphismes/wegert"}))
    sys.exit(0)
if args == ["api", "repos/functorial-games/spinor"]:
    print(json.dumps({"id": 1407855382, "full_name": "functorial-games/spinor"}))
    sys.exit(0)
sys.exit(1)
"""

with tempfile.TemporaryDirectory() as directory:
    root = Path(directory)
    stub = root / "gh"
    stub.write_text(GH_STUB)
    stub.chmod(0o755)
    log = root / "calls"
    env = {
        **os.environ,
        "PATH": str(root) + os.pathsep + os.environ["PATH"],
        "PIN_CALLS": str(log),
    }

    def run(repositories: str, expected_status: str):
        log.write_text("")
        run_root = root / ("runs-" + expected_status.lower())
        completed = subprocess.run(
            [
                sys.executable, str(RUNNER), "github-organization-pin-preflight",
                "--param", "organization=isomorphismes",
                "--param", "repositories=" + repositories,
                "--runs-root", str(run_root),
            ],
            cwd=ROOT, capture_output=True, text=True, env=env, check=False,
        )
        run_dirs = list(run_root.iterdir())
        assert len(run_dirs) == 1
        receipt = json.loads((run_dirs[0] / "receipt.json").read_text())
        report = json.loads(
            (run_dirs[0] / "01-eligibility/stdout.bin").read_text()
        )
        calls = [json.loads(line) for line in log.read_text().splitlines()]
        assert all(call[:1] in (["auth"], ["api"]) for call in calls)
        assert receipt["parameters"]["organization"] == "isomorphismes"
        assert report["status"] == expected_status
        assert report["mutation_performed"] is False
        assert report["pins_verified"] is False
        if expected_status == "PENDING_UI":
            assert completed.returncode == 0 and receipt["status"] == "PASS"
        else:
            assert completed.returncode != 0 and receipt["status"] == "FAIL"
            assert receipt["failed_stage"] == "eligibility"
        return report

    good = run("isomorphismes/wegert", "PENDING_UI")
    blocked = run("isomorphismes/wegert,functorial-games/spinor", "BLOCKED")
    assert blocked["resolved"][0]["id"] == good["resolved"][0]["id"]
    assert blocked["resolved"][1]["id"] == 1407855382

print("Flexible Pipes / pinned Kitchen org-pin preflight: PASS")
