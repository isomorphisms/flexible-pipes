#!/bin/sh
set -eu
root=$(CDPATH='' cd -- "$(dirname "$0")/../.." && pwd -P)
work="$root/.flexible-pipes/ib-c67-source-acceptance"
mkdir -p "$work"
ick=$ICK
test -n "$ick" && test -x "$ick"
# No alternate compiler route: ICK is the declared native build tool.
"$ick" -fno-link-libatomic -std=c11 -O2 -Wall -Wextra -Wpedantic -Werror \
    "$root/.deps/appendfat/lib/appendfat_arena.c" \
    "$root/.deps/appendfat/tools/appendfat_arena.c" \
    -o "$work/appendfat_arena"
"$ick" -fno-link-libatomic -std=c11 -O2 -Wall -Wextra -Wpedantic -Werror \
    "$root/.deps/ib152/native/android/ib_arena_slice.c" -o "$work/ib-arena-slice"
"$ick" -fno-link-libatomic -std=c11 -O2 -Wall -Wextra -Wpedantic -Werror \
    "$root/.deps/ib152/tests/icu_native_transport_probe.c" \
    "$root/.deps/icu/native/transport.c" -lssl -lcrypto -o "$work/icu-native-probe"
"$ick" -fno-link-libatomic -std=c11 -O2 -Wall -Wextra -Wpedantic -Werror \
    -fPIC -shared "$root/.deps/icu/native/transport.c" \
    -lssl -lcrypto -o "$work/libicu_transport.so"
export IB_APPEND_ARENA="$work/appendfat_arena"
export IB_ARENA_SLICE="$work/ib-arena-slice"
export IB_ICU_NATIVE_PROBE="$work/icu-native-probe"
export IB_ICU_NATIVE_SO="$work/libicu_transport.so"
export IB_AICI_SOURCE_VERIFY="$root/.deps/ai-ci/ib-source/verify.sh"
sh "$root/.deps/ib152/tests/test_android_icu_arena.sh"
sh "$root/.deps/ib152/tests/test_android_icu_native_bridge.sh"
sha256sum "$work/appendfat_arena" "$work/ib-arena-slice" \
    "$work/icu-native-probe" "$work/libicu_transport.so" \
    > "$work/native-icu-artifacts.sha256"
printf 'PASS\ticu-native-source-accepted\t%s\n' "$work/native-icu-artifacts.sha256"
printf 'physical_c67\tNOT_RUN\nandroid_direct_dex\tNOT_RUN\n'
