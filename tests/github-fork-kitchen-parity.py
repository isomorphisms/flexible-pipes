#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FP_RENDERER = ROOT / "scripts/render-github-fork-script"
FP_PIPELINE = ROOT / "pipelines/github-fork-script.json"


def run_renderer(renderer: Path, parameters: dict[str, str]) -> bytes:
    completed = subprocess.run(
        [
            sys.executable,
            str(renderer),
            parameters["source_owner"],
            parameters["repository"],
            parameters["destination_org"],
        ],
        capture_output=True,
        check=False,
    )
    assert completed.returncode == 0, completed.stderr.decode(errors="replace")
    return completed.stdout


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--kitchen-root", type=Path, required=True)
    args = parser.parse_args()

    kitchen_task = args.kitchen_root / "tasks/github-repository-fork"
    contract_path = kitchen_task / "paste-contract.json"
    kitchen_renderer = kitchen_task / "render-paste-block.py"

    contract = json.loads(contract_path.read_text())
    pipeline = json.loads(FP_PIPELINE.read_text())

    assert contract["schema_version"] == 1
    assert contract["operation"] == "github-repository-fork"
    assert contract["output_contract"]["form"] == "plain-text-paste-block"
    assert contract["output_contract"]["shell_interpreter_invocation"] is False

    kitchen_parameters = contract["parameters"]
    fp_parameters = list(pipeline["parameters"])
    assert fp_parameters == kitchen_parameters, (fp_parameters, kitchen_parameters)

    assert pipeline["name"] == "github-fork-script"
    stage = pipeline["stages"][0]
    assert stage["argv"][2:] == [f"{{{{{name}}}}}" for name in kitchen_parameters]

    for case in contract["cases"]:
        parameters = case["parameters"]
        expected = case["expected"].encode()
        kitchen = run_renderer(kitchen_renderer, parameters)
        flexible = run_renderer(FP_RENDERER, parameters)
        assert kitchen == expected
        assert flexible == expected
        assert flexible == kitchen

    print(f"Kitchen/Flexible Pipes fork parity: PASS ({len(contract['cases'])} vectors)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
