#!/usr/bin/env python3
from pathlib import Path
import hashlib
import json
import os
import shlex
import stat
import subprocess
import sys
import tempfile

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

fake = r'''#!/usr/bin/env python3
import json, os, sys
args=sys.argv[1:]
state=os.environ["FAKE_GH_STATE"]
if args[:2] == ["auth","status"]:
    raise SystemExit(0)
if not args or args[0] != "api":
    raise SystemExit(90)
args=args[1:]
method="GET"
endpoint=None
fields={}
jq=None
i=0
while i < len(args):
    a=args[i]
    if a=="--method":
        method=args[i+1]; i+=2
    elif a in ("-f","-F"):
        k,v=args[i+1].split("=",1); fields[k]=v; i+=2
    elif a=="--jq":
        jq=args[i+1]; i+=2
    elif endpoint is None:
        endpoint=a; i+=1
    else:
        raise SystemExit(91)
if endpoint=="user":
    print("isomorphisms"); raise SystemExit(0)
if endpoint=="orgs/dilapidated-shed":
    print("dilapidated-shed"); raise SystemExit(0)
if endpoint=="user/memberships/orgs/dilapidated-shed":
    print("active:admin"); raise SystemExit(0)
if endpoint=="repos/micropython/micropython":
    print("micropython/micropython"); raise SystemExit(0)
if method=="POST" and endpoint=="repos/micropython/micropython/forks":
    assert fields=={
        "organization":"dilapidated-shed",
        "name":"micropython",
        "default_branch_only":"false",
    }, fields
    open(state,"w").write("forked\n")
    raise SystemExit(0)
if endpoint=="repos/dilapidated-shed/micropython":
    assert os.path.exists(state), "destination queried before fork POST"
    print(json.dumps({
        "full_name":"dilapidated-shed/micropython",
        "fork":True,
        "source":"micropython/micropython",
    }))
    raise SystemExit(0)
raise SystemExit(92)
'''

with tempfile.TemporaryDirectory() as td:
    td=Path(td)
    gh=td/"gh"
    gh.write_text(fake)
    gh.chmod(gh.stat().st_mode | stat.S_IXUSR)
    state=td/"state"
    env=dict(os.environ, PATH=str(td)+os.pathsep+os.environ.get("PATH",""), FAKE_GH_STATE=str(state))
    outputs=[]
    for line in text.splitlines():
        argv=shlex.split(line)
        assert argv and argv[0]=="gh"
        completed=subprocess.run(argv, env=env, capture_output=True, text=True)
        assert completed.returncode==0, (line, completed.stderr, completed.stdout)
        outputs.append(completed.stdout.strip())
    assert state.read_text()=="forked\n"
    assert outputs[1]=="isomorphisms"
    assert outputs[2]=="dilapidated-shed"
    assert outputs[3]=="active:admin"
    assert outputs[4]=="micropython/micropython"
    final=json.loads(outputs[6])
    assert final=={
        "full_name":"dilapidated-shed/micropython",
        "fork":True,
        "source":"micropython/micropython",
    }

print(hashlib.sha256(result.stdout).hexdigest())
