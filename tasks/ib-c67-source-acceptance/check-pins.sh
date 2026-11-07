#!/bin/sh
set -eu
root=$(CDPATH='' cd -- "$(dirname "$0")/../.." && pwd -P)
test -n "${ICK:-}" && test -x "$ICK" || {
    printf 'qualified ICK host executable not available\n' >&2
    exit 2
}
check() {
    location=$1
    expected=$2
    test -d "$root/.deps/$location/.git" || {
        printf 'unmaterialized pinned source: %s\n' "$location" >&2
        exit 1
    }
    actual=$(git -C "$root/.deps/$location" rev-parse HEAD)
    test "$actual" = "$expected" || {
        printf 'wrong source %s: expected %s observed %s\n' "$location" "$expected" "$actual" >&2
        exit 1
    }
    printf 'source_pin\t%s\t%s\n' "$location" "$actual"
}
check ib152 d6c74283fa6bc41462a5af53c022894fe66cad90
check ib153 d9f18955801864cce2e8c8ac02df853772b271ac
check icu 0da041fbe906657f4f705da45a842d96832e5ee1
check appendfat 05a0cb7246c5a9f46abfbe92925812e7b607f454
check ai-ci 634626a14834e14b776616440e0a9071708f81b7
check ike 93f9eb0aee9094757414df8a7929c89b6a294b0c
test -f "$root/.deps/ai-ci/ib-source/verify.sh"
printf 'verified_ick_host\t%s\n' "$ICK"
