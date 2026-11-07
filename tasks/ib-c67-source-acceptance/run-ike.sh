#!/bin/sh
set -eu
root=$(CDPATH='' cd -- "$(dirname "$0")/../.." && pwd -P)
task="$root/tasks/ib-c67-source-acceptance"
out="$root/.flexible-pipes/ib-c67-source-acceptance"
mkdir -p "$out"
test -n "${ICK:-}" && test -x "$ICK"
# ICK compiles Ike; its own receipt records every actual executed recipe.
"$ICK" -fno-link-libatomic -std=c11 -O2 -Wall -Wextra -Wpedantic \
    "$root/.deps/ike/ike.c" -o "$out/ike"
cd "$task"
export IKE_RECEIPT="$out/ike.tsv"
export IKE_IKEFILE_IDENTITY="sha256:$(sha256sum Ikefile | cut -d ' ' -f 1)"
"$out/ike" pfd-host-execution
grep -Fx "$(printf 'final_result\tPASS')" "$IKE_RECEIPT"
sha256sum "$out/ike" "$IKE_RECEIPT"
printf 'PASS\tike-pfd-host-execution\n'
