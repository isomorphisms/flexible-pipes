#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import platform
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NAME_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]*$")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def repository_commit() -> str | None:
    try:
        return subprocess.run(
            ["git", "-C", str(ROOT), "rev-parse", "HEAD"],
            check=True,
            text=True,
            capture_output=True,
        ).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return None


def utc_now() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat()


def fail(message: str) -> int:
    print(message, file=sys.stderr)
    return 2


def main() -> int:
    parser = argparse.ArgumentParser(description="Run one checked-in flexible-pipes pipeline")
    parser.add_argument("pipeline", help="pipeline name, without pipelines/ or .json")
    parser.add_argument("--ithon", help="verified Ithon entrypoint, required for job artifacts")
    parser.add_argument(
        "--runs-root",
        default=os.environ.get(
            "FLEXIBLE_PIPES_RUNS_ROOT",
            str(ROOT / ".flexible-pipes" / "runs"),
        ),
        help="directory for run receipts and stage output",
    )
    args = parser.parse_args()

    if not NAME_RE.fullmatch(args.pipeline):
        return fail(f"invalid pipeline name: {args.pipeline!r}")

    pipeline_path = ROOT / "pipelines" / f"{args.pipeline}.json"
    if not pipeline_path.is_file():
        return fail(f"unknown pipeline {args.pipeline!r}: {pipeline_path} does not exist")

    raw = pipeline_path.read_bytes()
    try:
        spec = json.loads(raw)
    except json.JSONDecodeError as exc:
        return fail(f"invalid pipeline JSON {pipeline_path}: {exc}")

    if spec.get("schema_version") != 1:
        return fail("pipeline schema_version must be 1")
    if spec.get("name") != args.pipeline:
        return fail(f"pipeline name mismatch: file says {spec.get('name')!r}")
    stages = spec.get("stages")
    if not isinstance(stages, list) or not stages:
        return fail("pipeline must contain a non-empty stages list")

    required_stages = spec.get("required_stages", [])
    if not isinstance(required_stages, list) or not all(
        isinstance(name, str) and NAME_RE.fullmatch(name)
        for name in required_stages
    ):
        return fail("required_stages must be a list of valid stage names")
    if len(set(required_stages)) != len(required_stages):
        return fail("required_stages contains duplicates")

    validated_stages: list[dict[str, object]] = []
    seen_names: set[str] = set()
    root_resolved = ROOT.resolve()
    for index, stage in enumerate(stages, start=1):
        if not isinstance(stage, dict):
            return fail(f"stage {index} must be an object")
        if stage.get("kind") != "command":
            return fail(f"stage {index}: unsupported kind {stage.get('kind')!r}")

        name = stage.get("name")
        argv = stage.get("argv")
        if not isinstance(name, str) or not NAME_RE.fullmatch(name):
            return fail(f"stage {index}: invalid name {name!r}")
        if name in seen_names:
            return fail(f"duplicate stage name: {name}")
        seen_names.add(name)
        if not isinstance(argv, list) or not argv or not all(
            isinstance(x, str) and x for x in argv
        ):
            return fail(f"stage {name}: argv must be a non-empty string list")

        cwd_rel = stage.get("cwd", ".")
        if not isinstance(cwd_rel, str):
            return fail(f"stage {name}: cwd must be a string")
        cwd = (ROOT / cwd_rel).resolve()
        if root_resolved not in (cwd, *cwd.parents):
            return fail(f"stage {name}: cwd escapes repository: {cwd_rel!r}")
        if not cwd.is_dir():
            return fail(f"stage {name}: cwd does not exist: {cwd_rel!r}")

        validated_stages.append(
            {"name": name, "argv": argv, "cwd_rel": cwd_rel, "cwd": cwd,
             "handoff": stage.get("handoff")}
        )
        if "handoff" in stage:
            if not isinstance(stage["handoff"], dict):
                return fail(f"stage {name}: handoff must be an object")
            if not args.ithon or not Path(args.ithon).is_file():
                return fail("job handoff requires an explicit verified --ithon entrypoint")
            # Whole-plan validation precedes all command effects. New policy
            # lives in checked Ithon; this controller remains migration debt.
            with tempfile.NamedTemporaryFile(mode="w", suffix=".json") as spec_file:
                json.dump(stage["handoff"], spec_file)
                spec_file.flush()
                checked = subprocess.run(
                    [args.ithon, str(ROOT / "scripts/compose-handoff.pi"),
                     "validate-spec", spec_file.name], capture_output=True)
            if checked.returncode != 0:
                return fail(f"stage {name}: invalid handoff: " + checked.stderr.decode(errors="replace"))

    missing_required = [name for name in required_stages if name not in seen_names]
    if missing_required:
        return fail(
            "pipeline is missing required stages: " + ", ".join(missing_required)
        )

    run_token = (
        os.environ.get("GITHUB_RUN_ID")
        or dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%S.%fZ")
    )
    run_dir = Path(args.runs_root) / f"{args.pipeline}-{run_token}"
    run_dir.mkdir(parents=True, exist_ok=False)

    receipt: dict[str, object] = {
        "schema_version": 1,
        "pipeline": args.pipeline,
        "pipeline_path": str(pipeline_path.relative_to(ROOT)),
        "pipeline_sha256": sha256_bytes(raw),
        "repository_commit": repository_commit(),
        "github_sha_declared": os.environ.get("GITHUB_SHA"),
        "runner": {
            "system": platform.system(),
            "release": platform.release(),
            "machine": platform.machine(),
            "python": platform.python_version(),
        },
        "started_at": utc_now(),
        "status": "RUNNING",
        "stages": [],
    }
    final_path = run_dir / "receipt.json"

    try:
        for index, stage in enumerate(validated_stages, start=1):
            name = stage["name"]
            argv = stage["argv"]
            cwd_rel = stage["cwd_rel"]
            cwd = stage["cwd"]

            stage_dir = run_dir / f"{index:02d}-{name}"
            stage_dir.mkdir()
            started = utc_now()
            try:
                completed = subprocess.run(
                    argv,
                    cwd=cwd,
                    text=False,
                    capture_output=True,
                    check=False,
                )
                exit_code = completed.returncode
                stdout = completed.stdout
                stderr = completed.stderr
            except OSError as exc:
                exit_code = 127
                stdout = b""
                stderr = f"{type(exc).__name__}: {exc}\n".encode()

            (stage_dir / "stdout.bin").write_bytes(stdout)
            (stage_dir / "stderr.bin").write_bytes(stderr)
            stage_receipt = {
                "index": index,
                "name": name,
                "kind": "command",
                "argv": argv,
                "cwd": str(cwd.relative_to(ROOT)),
                "started_at": started,
                "finished_at": utc_now(),
                "exit_code": exit_code,
                "stdout_sha256": sha256_bytes(stdout),
                "stderr_sha256": sha256_bytes(stderr),
            }
            receipt["stages"].append(stage_receipt)
            if exit_code != 0:
                receipt["status"] = "FAIL"
                receipt["failed_stage"] = name
                break
            if stage["handoff"] is not None:
                stage_path = stage_dir / "stage.json"
                stage_path.write_text(json.dumps(stage_receipt))
                spec_path = stage_dir / "handoff-spec.json"
                spec_path.write_text(json.dumps(stage["handoff"]))
                composed = subprocess.run(
                    [args.ithon, str(ROOT / "scripts/compose-handoff.pi"), "compose",
                     str(stage_path), str(spec_path), str(stage_dir / "stdout.bin")],
                    capture_output=True)
                if composed.returncode != 0:
                    receipt["status"] = "FAIL"
                    receipt["runner_error"] = composed.stderr.decode(errors="replace")
                    break
                receipt["stages"][-1] = json.loads(stage_path.read_bytes())
                # Composition and an internal output file are not delivery.
                # Do not execute later stages (including dispatch) on this path.
                receipt["status"] = "AWAITING_HANDOFF_DELIVERY"
                receipt["handoff_stage"] = name
                composed_handoff = receipt["stages"][-1]["handoff"]
                if composed_handoff.get("transport") == "attachment":
                    receipt["attachment_artifact"] = str(stage_path) + ".attachment"
                    receipt["attachment_file_name"] = composed_handoff["attachment"]["file_name"]
                    receipt["attachment_mime_type"] = composed_handoff["attachment"]["mime_type"]
                else:
                    receipt["response_artifact"] = str(stage_path) + ".response.txt"
                break
        else:
            receipt["status"] = "PASS"
    except Exception as exc:
        receipt["status"] = "FAIL"
        receipt["runner_error"] = f"{type(exc).__name__}: {exc}"
    finally:
        receipt["finished_at"] = utc_now()
        final_path.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n")

    print(json.dumps(receipt, indent=2, sort_keys=True))
    return 0 if receipt["status"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
