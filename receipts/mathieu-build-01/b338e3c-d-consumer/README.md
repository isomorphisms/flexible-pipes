# Mathieu: bounded D-runtime consumer evidence

Application source: `b338e3c9c92b7c8c32804b63c02dd15f600a79fd`.
Date: 2026-10-21. Target: disposable Linux x86_64 build host.
Status: **consumer diagnostics PASS; managed-runtime admission BLOCKED; Android execution NOT_RUN**.

This continuation actually invoked the D implementation `ysh-d`, SHA-256
`cb461eb12ae88f7927f9ceec79bfa129ef8e5dcbc629a7ce64686956d1319237`.
Its real name and qualification limits are retained. It is not represented as an
admitted complete Grease runtime. The C++ implementation prohibited by the
[standing human correction in Flexible Pipes issue #67](https://github.com/isomorphisms/flexible-pipes/issues/67)
was not invoked for any run in this directory. Earlier C++-backed records remain
historical observations, NOT_ELIGIBLE for managed acceptance.

## What actually ran

- Kitchen `1.grease` and pinned Ike compiled and executed fresh ICK Debug and
  Release engine, controller, raster and portable-checkpoint tests. Both pass.
  The earlier host smoke reused outputs; `d-host-fresh` records actual recompilation.
- Kitchen `2.grease` and pinned Ike rebuilt Debug and Release NativeActivity
  libraries for armeabi-v7a, arm64-v8a and x86_64.
- Independent AI-CI GAP calculations and the native export match all 5,009 lines.
  Wrong permutation-word, design and code exports are rejected. Both complete
  exports have SHA-256 `d7c314e574d73bca532b7598cddabcd4e3154c1a9586dbc87c5cd3dd439a2d25`;
  their material hashes and gate receipt are retained here.
- Kitchen `5.grease` strips staged library copies and invokes the unchanged
  maintained android-NDK NativeActivity packager under Ike. Six signed native-only
  APK candidates result. The application owns its permanent public development
  signer; no build chooses or generates a signer.
- AI-CI `mathieu/apk.grease` inspects actual finished APK bytes independently of
  the producer receipts. All six pass package, version, SDK, launcher label,
  NativeActivity, signature, central candidate signer registration, alignment,
  single-ABI native payload, source marker, ELF machine, stripping and no-DEX checks.
- The acceptance branch reconciles the new main-branch Crystal Pyrite signer
  without discarding either registration. All 17 central registry fixtures and
  the finished-APK positive/hostile cases pass their expected outcomes at
  `0200258f5c9367c9c0cad8245be26151d0ae1422`.

Native and host tests verify M12 order 95,040, M24 order 244,823,040, stabilizer
chains, five-transitivity, all 132 hexads and 759 octads with unique five-subset
completion, and all 4,096 extended Golay words with the required weights and
generator invariance. They also exercise touch-coordinate dispatch, dancer
endpoints, selection equivariance, pause/step, history reversal, layouts and
checkpoint continuation. This is host execution of application logic, not an
Android window/input or physical-device result.

## Deliberate failures

`negative-cases.tsv` maps each actual FP receipt to its intended result. FP
records FAIL for a rejected input; that is the required negative-test outcome.

Two valid hostile APKs replace only the A1 Debug candidate within otherwise
complete six-APK directories. One has an altered self-signed certificate using a
fixture copy of the same public development private key, without generating
another key. It fails with `SIGNER_MISMATCH`. The other is packaged with the real
permanent signer and label `Wrong fixture label`; it fails with
`LAUNCHER_LABEL_MISMATCH expected=Mathieu observed=Wrong fixture label`.
This establishes rejection of actual hostile packages, not just fabricated
signer strings.

Packaging rejects a stale source head, missing SDK, wrong packager revision,
existing output and a clean fixture omitting the required PKCS12 file. The missing
signer fixture is local commit `00bbb878f68eeb4503bd07afda5d2a905706ce61`,
parented by the application head with exactly one deletion,
`android/signing/mathieu-development.p12`. It is not an application release.
All absent-output cases leave no output directory; rejecting an existing output
does not change the good candidate hashes. The real keystore and certificate
hashes remain unchanged.

The first finished-APK gate failed because it assumed aapt2 used
`sdkVersion` and `application-label`. Build-tools 35 emits
`minSdkVersion` and `application: label=`. AI-CI retains that failed attempt,
then accepts both real field spellings while keeping the same exact expected
values. The final label diagnostic is explicit. The corrected positive and both
hostile cases were rerun after branch reconciliation.

## Pins and provenance

`pins.tsv` identifies source, recipe, oracle, packager and interpreter pins.
Per-run JSON is the unchanged existing FP runner's native receipt format.
The runner checkout remains at `8f38cb8980f4ea88f4737b080d80fbdb9a51835c`;
the separately added package and APK-acceptance specs are published at
`96b0a49e43d7e57fed4c930135fb4b263e2a419a`. Their recorded content hashes
match those published specs. Do not read the runner pin as a claim that its
checkout contained the later committed receipt tree. The existing FP Python
runner and maintained Bash APK packager are named compatibility boundaries;
no new Python/Bash replacement was authored for these recipes.

`runtime/owner-qualification.tsv` is a snapshot from the D implementation's
owning work, not an independent admission. Dynamic ELF inspection finds no
libstdc++ dependency. It does not rule out statically embedded or transitive C++
code. The owner still reports inherited qualification FAIL, static-transitive
AI-CI UNKNOWN and managed FP admission NOT_RUN. Those limits are not waived by
successful Mathieu consumer tests.

## Candidate artifacts and unfinished acceptance

The two requested Release names exist: `Mathieu-A1.apk` (33,213 bytes,
SHA-256 `132fdc833937722f9f21396ff315560c83f5247173b7876fca418bf7bfc7ea4a`)
and `Mathieu-C67.apk` (37,307 bytes,
SHA-256 `27c1f654ca8bae601dc02cc9179c2876664c573ccb1642b0780610307ef56dfc`).
All six candidate identities are in `d-apk-accept-reconciled/packages.tsv`.
They share package `org.isomorphisms.mathieu`, versionCode 1 and certificate
`f997a30170a967e073ab47e1212a71b3967ffe2e1e88d78d659c77bf085cb3fe`.

**First blocker:** permitted Grease runtime admission remains unestablished.
Accepted central signer policy, consumer toolchain/producer qualification,
hosted current-head checks, emulator launch/window/input execution, separate
physical A1/C67 installation/behavior/replacement updates, Cat Food publication
and whole-application independent acceptance also remain open.
No adb, emulator executable or KVM device is available on this host. No physical
device channel was used. There is no installation, launch, device PASS, accepted
delivery, merge or completed-job claim.

The user will move the repository to isomorphismes themselves. This work does
not transfer it or change Android package/signing identity.

Related work:
- [isomorphisms/mathieu PR #3, “Implement exact Mathieu choreography and native Android application core”](https://github.com/isomorphisms/mathieu/pull/3).
- [isomorphisms/kitchen PR #75, “Prepare exact-head Mathieu builds through Grease and pinned Ike”](https://github.com/isomorphisms/kitchen/pull/75).
- [isomorphisms/ai-ci PR #316, “Verify exact Mathieu actions and Golay invariants with an independent GAP oracle”](https://github.com/isomorphisms/ai-ci/pull/316).
- [isomorphisms/flexible-pipes PR #248, “Route Mathieu native builds and independent GAP acceptance through Flexible Pipes”](https://github.com/isomorphisms/flexible-pipes/pull/248).
