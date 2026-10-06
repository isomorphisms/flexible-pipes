#!/usr/bin/env bash
set -Eeuo pipefail

root=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
work=$(mktemp -d "${RUNNER_TEMP:-${TMPDIR:-/tmp}}/flexible-pipes-preflight.XXXXXX")
trap 'rm -rf "$work"; rm -f "$root/pipelines/test-prevalidation.json" "$root/pipelines/test-required.json"' EXIT

marker="$work/mutated"

cat > "$root/pipelines/test-prevalidation.json" <<JSON
{
  "schema_version": 1,
  "name": "test-prevalidation",
  "stages": [
    {
      "name": "would-mutate",
      "kind": "command",
      "argv": ["sh", "-c", "touch '$marker'"],
      "cwd": "."
    },
    {
      "name": "invalid-later-stage",
      "kind": "unsupported",
      "argv": ["true"],
      "cwd": "."
    }
  ]
}
JSON

if python3 "$root/scripts/run-pipeline" test-prevalidation --runs-root "$work/runs-a"     >"$work/prevalidation.out" 2>"$work/prevalidation.err"
then
  echo "invalid later stage unexpectedly passed" >&2
  exit 1
fi
grep -Fq "unsupported kind" "$work/prevalidation.err"
test ! -e "$marker"

cat > "$root/pipelines/test-required.json" <<JSON
{
  "schema_version": 1,
  "name": "test-required",
  "required_stages": ["android-producer-gate"],
  "stages": [
    {
      "name": "would-mutate",
      "kind": "command",
      "argv": ["sh", "-c", "touch '$marker'"],
      "cwd": "."
    }
  ]
}
JSON

if python3 "$root/scripts/run-pipeline" test-required --runs-root "$work/runs-b"     >"$work/required.out" 2>"$work/required.err"
then
  echo "pipeline missing required gate unexpectedly passed" >&2
  exit 1
fi
grep -Fq "pipeline is missing required stages: android-producer-gate" "$work/required.err"
test ! -e "$marker"

fake_sha=1111111111111111111111111111111111111111
head=$(git -C "$root" rev-parse HEAD)
GITHUB_SHA="$fake_sha" python3 "$root/scripts/run-pipeline" regression-history-smoke     --runs-root "$work/runs-c" > "$work/identity.out"

grep -Fq "\"repository_commit\": \"$head\"" "$work/identity.out"
grep -Fq "\"github_sha_declared\": \"$fake_sha\"" "$work/identity.out"

printf 'flexible-pipes pipeline preflight tests: PASS\n'
