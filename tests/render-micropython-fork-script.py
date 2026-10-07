#!/usr/bin/env python3
from pathlib import Path
import hashlib
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
renderer = ROOT / "scripts/render-micropython-fork-script"
result = subprocess.run([sys.executable, str(renderer)], capture_output=True)

assert result.returncode == 0, result.stderr.decode()
text = result.stdout.decode("utf-8")
expected = """gh auth status --hostname github.com
gh api user --jq '.login'
gh api orgs/dilapidated-shed --jq '.login'
gh api user/memberships/orgs/dilapidated-shed --jq '.state + ":" + .role'
gh api repos/micropython/micropython --jq '.full_name'
gh api --method POST repos/micropython/micropython/forks -f organization=dilapidated-shed -f name=micropython -F default_branch_only=false
gh api repos/dilapidated-shed/micropython --jq '{full_name, fork, source: .source.full_name}'
"""
assert text == expected
assert " sh " not in f" {text} "
assert "#!/bin/sh" not in text
assert "#!/system/bin/sh" not in text
assert text.count("POST repos/micropython/micropython/forks") == 1
assert "organization=dilapidated-shed" in text
assert "name=micropython" in text
assert "default_branch_only=false" in text
assert text.rstrip().endswith("'{full_name, fork, source: .source.full_name}'")
print(hashlib.sha256(result.stdout).hexdigest())
