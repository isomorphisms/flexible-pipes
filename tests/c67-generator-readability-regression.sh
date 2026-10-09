#!/bin/sh
# C67 regression: a downloaded Kitchen generator was readable by head but
# Grease `test -r` returned false. Verify actual read, not an access predicate.
set -eu
root=$(CDPATH= cd "$(dirname "$0")/.." && pwd)
batch=$root/scripts/move-new-math-repositories-to-isomorphismes.ysh

if grep -F 'test -r "$generator"' "$batch" >/dev/null; then
    echo 'batch still relies on the C67-failing test -r generator predicate' >&2
    exit 1
fi
grep -F 'head -n 1 "$generator" > "$generator_probe"' "$batch" >/dev/null
grep -F 'generator_header=$(cat "$generator_probe")' "$batch" >/dev/null
grep -F "test \"\$generator_header\" = '#!/usr/bin/env grease'" "$batch" >/dev/null

echo 'PASS batch admits the fetched Kitchen generator by an actual read and header identity'
