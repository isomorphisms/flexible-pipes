#!/usr/bin/env python3
"""Host-only FP RMR stage driver: pinned source preflight and real converter example.

Never handles user/private-phone data, APK signing keys or physical-device facts.
The producer is the leaf's exact pinned converter; independent verification is
a later FP stage running code from the separate pinned AI-CI repository.
"""
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
REG = ROOT / "registry/rmr-signing-restore.json"
CHECKOUTS = {
    "producer": ROOT / "_reading/producer",
    "aici": ROOT / "_reading/aici",
}


def fail(s):
    raise SystemExit(s)


def pins():
    manifest = json.loads(REG.read_text())
    for key in ("producer", "aici"):
        source = manifest["sources"][key]
        repository_path = CHECKOUTS[key]
        if not repository_path.is_dir():
            fail("Missing " + key + " checked out source")
        actual = subprocess.run(["git", "-C", str(repository_path), "rev-parse", "HEAD"],
                                capture_output=True, text=True, check=True).stdout.strip()
        if actual != source["commit"]:
            fail(f"Source pin mismatch: {key} observed {actual} expected {source['commit']}")
        print(f"source={key} repository={source['repository']} pinned_commit={actual}")
    if manifest["production_admission"] != "NOT_ACCEPTED" or (
            manifest["physical_A1_C67"] != "NOT_RUN"):
        fail("Host-only pipeline may not claim product release or device acceptance")
    return manifest


def sample():
    pins()
    output = ROOT / "_reading/evidence"
    output.mkdir(parents=True, exist_ok=True)
    if any(output.iterdir()):
        fail("Evidence output must begin empty")
    fixture_path = CHECKOUTS["aici"] / "reading-backup/test_compare_legacy.py"
    spec = importlib.util.spec_from_file_location("aici_seed_fixture", fixture_path)
    fixture_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(fixture_module)
    source, seeded_zip, _, _ = fixture_module.fixture(output, version=3)
    # The independent test fixture itself makes a reference zip; delete it.
    # The *real producer* writes the archive that AI-CI later reads.
    seeded_zip.unlink()
    candidate = output / "portable.zip"
    converter = CHECKOUTS["producer"] / "ci/legacy-to-portable.py"
    completed = subprocess.run([sys.executable, str(converter),
                                str(source), str(candidate)],
                               capture_output=True, text=True, check=False)
    if completed.returncode:
        fail(f"Leaf converter failed: {completed.stderr}")
    if not candidate.is_file():
        fail("Converter reported success without creating portable ZIP")
    print(completed.stdout.strip())
    print("actual_producer=ci/legacy-to-portable.py")
    print("origin=" + str(source.relative_to(ROOT)))
    print("candidate=" + str(candidate.relative_to(ROOT)))


def seal():
    pins()
    output = ROOT / "_reading/evidence"
    paths = [output / "old.tar", output / "portable.zip"]
    if any(not file.is_file() for file in paths):
        fail("Host evidence missing")
    for file in paths:
        hash_value = hashlib.sha256(file.read_bytes()).hexdigest()
        print(f"artifact={file.relative_to(ROOT)} sha256={hash_value} bytes={file.stat().st_size}")
    print("status=HOST_ARCHIVE_ACCEPTED")
    print("device_update_status=NOT_VERIFIED")
    print("protected_signer_status=NOT_VERIFIED")
    print("fp_platform_dispatch_status=NOT_VERIFIED")


if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in ("preflight", "produce", "seal"):
        fail("Usage: rmr-host-test.py preflight|produce|seal")
    if sys.argv[1] == "preflight":
        pins()
    elif sys.argv[1] == "produce":
        sample()
    else:
        seal()
