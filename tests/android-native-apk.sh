#!/usr/bin/env bash
set -Eeuo pipefail
root=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
tmp=$(mktemp -d)
trap 'rm -rf "$tmp"' EXIT
bash -n "$root/scripts/android-producer-stage"
if bash "$root/scripts/android-producer-stage" registered >"$tmp/out" 2>"$tmp/err"; then
    echo 'registered producer unexpectedly accepted missing input' >&2; exit 1
fi
grep -Fq 'required registered input is unset: FP_ANDROID_REPOSITORY' "$tmp/err"
printf 'fake ICK object bytes\n' > "$tmp/ick.o"
digest=$(sha256sum "$tmp/ick.o" | awk '{print $1}')
fixture() {
    env FP_ANDROID_REPOSITORY=unregistered/malicious \
        FP_ANDROID_SOURCE_SHA=1111111111111111111111111111111111111111 \
        FP_ANDROID_APP_ROOT="$tmp/missing-source" \
        FP_CATFOOD_CHECKOUT="$tmp/missing-catfood" \
        FP_AICI_CHECKOUT="$tmp/missing-aici" \
        FP_ANDROID_NDK_CHECKOUT="$tmp/missing-ndk" \
        FP_ANDROID_ICK_OBJECT="$tmp/ick.o" \
        FP_ANDROID_ICK_OBJECT_SHA256="$1" \
        FP_ANDROID_OUTPUT_DIR="$tmp/must-stay-absent" \
        bash "$root/scripts/android-producer-stage" registered >"$tmp/out" 2>"$tmp/err"
}
if fixture 0000000000000000000000000000000000000000000000000000000000000000; then
    echo 'tampered ICK object digest accepted' >&2; exit 1
fi
grep -Fq 'ICK object digest mismatch' "$tmp/err"
if fixture "$digest"; then
    echo 'unregistered app recipe accepted' >&2; exit 1
fi
grep -Fq 'application not uniquely registered' "$tmp/err"
test ! -e "$tmp/must-stay-absent"
if python3 "$root/scripts/run-pipeline" android-native-apk \
    --runs-root "$tmp/runs" >"$tmp/pipeline.log" 2>"$tmp/pipeline.err"; then
    echo 'missing runtime qualification unexpectedly passed pipeline' >&2; exit 1
fi
grep -Fq '"status": "FAIL"' "$tmp/pipeline.log"
grep -Fq '"failed_stage": "registered-build-and-companion-artifact-gate"' "$tmp/pipeline.log"
printf '%s\n' 'Flexible Pipes Android registered producer negative fixtures: PASS'
