#!/bin/sh
set -eu
root=$(CDPATH='' cd -- "$(dirname "$0")/../.." && pwd -P)
work="$root/.flexible-pipes/ib-c67-source-acceptance"
ick=$ICK
test -n "$ick" && test -x "$ick"
test -x "$work/appendfat_arena" && test -x "$work/ib-arena-slice"
"$ick" -fno-link-libatomic -std=c11 -O2 -Wall -Wextra -Wpedantic -Werror -pthread \
    "$root/.deps/ib153/native/android/ib_reader_pfd.c" \
    "$root/.deps/ib153/tests/test_android_reader_pfd.c" \
    -o "$work/test-reader-pfd"
"$ick" -fno-link-libatomic -std=c11 -O2 -Wall -Wextra -Wpedantic -Werror -pthread \
    "$root/.deps/ib153/native/android/ib_reader_pfd.c" \
    "$root/.deps/ib153/native/android/ib_arena_source_owner.c" \
    "$root/.deps/ib153/tests/test_android_arena_source_owner.c" \
    -o "$work/test-arena-pfd"
"$work/test-reader-pfd"
export IB_APPEND_ARENA="$work/appendfat_arena"
export IB_ARENA_SLICE="$work/ib-arena-slice"
export IB_TEST_VERIFIED_ARENA_PIPE="$work/test-arena-pfd"
export IB_AICI_SOURCE_VERIFY="$root/.deps/ai-ci/ib-source/verify.sh"
sh "$root/.deps/ib153/tests/test_android_arena_source_owner_synthetic.sh"
sh "$root/.deps/ib153/tests/test_android_arena_source_owner.sh"
sha256sum "$work/test-reader-pfd" "$work/test-arena-pfd" \
    > "$work/native-pfd-artifacts.sha256"
printf 'PASS\tpfd-source-owner-host\t%s\n' "$work/native-pfd-artifacts.sha256"
printf 'android_real_binder\tNOT_RUN\n'
