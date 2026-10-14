#!/bin/sh
# Physical C67 regression: Grease test -r rejected a generator that head read.
# Cover both the accepted batch path and the standalone transfer wrapper.
set -eu
root=$(CDPATH= cd "$(dirname "$0")/.." && pwd)
batch=$root/scripts/move-new-math-repositories-to-isomorphismes.ysh
single=$root/scripts/how-to-move-the-users-github-repository-to-a-different-organization.ysh

for entrypoint in "$batch" "$single"; do
    if grep -F 'test -r "$generator"' "$entrypoint" >/dev/null; then
        echo "C67-failing generator readability predicate: $entrypoint" >&2
        exit 1
    fi
    grep -F 'head -n 1 "$generator" > "$generator_probe"' "$entrypoint" >/dev/null
    grep -F 'generator_header=$(cat "$generator_probe")' "$entrypoint" >/dev/null
    grep -F "test \"\$generator_header\" = '#!/usr/bin/env grease'" "$entrypoint" >/dev/null
done

echo 'PASS batch and single transfer entrypoints admit the generator by an actual read and header identity'
