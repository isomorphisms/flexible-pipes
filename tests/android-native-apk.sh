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

# TAB_P10 gate: synthetic source/ABI checks do not prove installed behavior.
source_sha=1111111111111111111111111111111111111111
{
    printf 'schema\tcatfood-android-build-plan-v1\n'
    printf 'source_sha\t%s\n' "$source_sha"
    printf 'requested_target\ttablet\n'
    printf 'package_id\torg.isomorphisms.fastchat.diskstreaming.arena\n'
    printf 'target\tdevice\tabi\tobligation\tacceptance\n'
    printf 'tablet\tTAB_P10\tarm64-v8a\trequired\tnot_run\n'
} > "$tmp/tablet-plan.tsv"
bash "$root/scripts/fastchat-tablet-plan-gate.sh" "$tmp/tablet-plan.tsv" "$source_sha"
reject_tablet() {
    if bash "$root/scripts/fastchat-tablet-plan-gate.sh" "$tmp/tablet-plan.tsv" "$source_sha" >"$tmp/out" 2>"$tmp/err"; then
        echo 'bad tablet plan was accepted' >&2; exit 1
    fi
}
cp "$tmp/tablet-plan.tsv" "$tmp/valid-plan.tsv"
sed 's/TAB_P10/MIRO_C67/' "$tmp/valid-plan.tsv" > "$tmp/tablet-plan.tsv"
reject_tablet
sed 's/arm64-v8a/armeabi-v7a/' "$tmp/valid-plan.tsv" > "$tmp/tablet-plan.tsv"
reject_tablet
sed 's/not_run/PASS/' "$tmp/valid-plan.tsv" > "$tmp/tablet-plan.tsv"
reject_tablet
sed 's/source_sha/source_SHA/' "$tmp/valid-plan.tsv" > "$tmp/tablet-plan.tsv"
reject_tablet
sed 's/requested_target.*tablet/requested_target  c67/' "$tmp/valid-plan.tsv" > "$tmp/tablet-plan.tsv"
reject_tablet
rm "$tmp/tablet-plan.tsv"
reject_tablet
printf '%s\n' 'PASS FastChat tablet refusal fixtures (no physical/signer acceptance)'
