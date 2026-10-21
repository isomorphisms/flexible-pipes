# Mathieu signer and APK candidate evidence — 2026-10-21

Application source: `b338e3c9c92b7c8c32804b63c02dd15f600a79fd`.
Permanent signer commit: `025e26a55f3f1e230dd958a87773d532e92c8382`.
Package: `org.isomorphisms.mathieu`; versionCode 1; versionName
`0.1.0-development`; minSdk 26; targetSdk 35; label Mathieu.
The deliberately public development key is application-owned under
`android/signing`. Its certificate SHA-256 is
`f997a30170a967e073ab47e1212a71b3967ffe2e1e88d78d659c77bf085cb3fe`.
The user authorized its creation; it is not a production/store key.

## Qualification correction

The available Grease wrapper (SHA-256
`37088097c36a2f82cf45aaea9392e4a4cf16155fecb9da87d08a9c7fb4d92e4a`)
executes the inherited runtime
`7e31cd05b7a9d8fb2a4a9e003a7f3fcb0159138506d17f0fb28da8cbe22aa85c`.
Direct ELF inspection shows `DT_NEEDED: libstdc++.so.6`.
[The standing human correction in Flexible Pipes #67](https://github.com/isomorphisms/flexible-pipes/issues/67)
prohibits that C++ implementation. No Grease runtime was invoked in this
continuation.

**Earlier cc9d23b and 3b860d4 FP/Kitchen/Ike runs remain historical technical
results, NOT_ELIGIBLE for managed-route acceptance.** Their zero exit statuses,
compiler outputs and mathematical observations are preserved; they do not
waive runtime admission. The correction supersedes eligibility claims in the
earlier receipt summaries. A permitted Grease-compatible implementation and
independent admission are required before rerunning the maintained path.
No replacement interpreter was selected.

## Candidate observations

The existing application Makefiles and the maintained android-NDK NativeActivity
packager were invoked directly for bounded candidate checks. This is explicitly
outside qualified FP/Kitchen/Ike acceptance, and is not an alternative delivery
route.

- Debug and Release host engine, actual touch/controller/raster and portable
  checkpoint tests pass at the application source above.
- The independent GAP `reference.g` and actual Release engine export agree
  byte-for-byte on 5,009 lines. The GAP/reference implementation is the existing
  AI-CI implementation, not the native application's algorithms.
- The ICK frontend plus separate NDK assembly/link builds succeed for
  armeabi-v7a, arm64-v8a and x86_64, each in Debug and Release.
- NDK `llvm-strip --strip-unneeded` creates separate stripped libraries; the
  original debug/native files remain debugging artifacts.
- Six native-only APKs are linked/aligned/signed by android-NDK packager
  `11edd1e0d9748d7c618413ec9f5afad52049046a`.
  Every packager run verifies package/version/label/NativeActivity/ABI/no-DEX
  and actual finished-APK signer. A separate apksigner verify succeeds for all
  six. The stripped A1 library retains `ANativeActivity_onCreate`.
- The AICI signing verifier, compiled through the recorded host ICK binary,
  accepts each extracted package/certificate against candidate registry
  `5a3c7b2361e162c5743fcbb92191258bf7dc4dbe`.
  All 14 registry fixtures pass, including Mathieu's wrong-signer and
  unregistered-production-lane controls.
- One initial A1 Release packager invocation returned exit 134 with empty
  captured output. Its cause is UNKNOWN. A separate sequential retry succeeds;
  the earlier result is not erased or attributed to the application.

Android SDK Platform 35 revision 2 was downloaded from the official
`https://dl.google.com/android/repository/platform-35_r02.zip`.
The official repository metadata SHA-1
`0bb560a90a7a2cbd0dd8348224d518b638fe7949` matches.
Archive SHA-256:
`0988cacad01b38a18a47bac14a0695f246bc76c1b06c0eeb8eb0dc825ab0c8e0`;
android.jar SHA-256:
`4566663c3876e022b4fa4ced8c8697c4ab1688267f090114fd92d027b32e619b`.
Build-tools are 35.0.0. NDK is r27c / 27.2.12479018. Compiler byte identities
remain those in the prior materials receipts; the reused host compiler's
source-build provenance remains a separate unresolved qualification boundary.

## Open gates

The central signer row is a candidate in
[isomorphisms/ai-ci PR #316, “Verify exact Mathieu actions and Golay invariants with an independent GAP oracle”](https://github.com/isomorphisms/ai-ci/pull/316).
It is not in protected main. The standard Android producer requires accepted
policy and packager ancestry plus the consumer toolchain contract; these
candidate checks do not constitute producer approval.

Qualified managed execution, producer approval, hosted exact-head checks,
emulator input/window execution, physical A1 and C67 installation/behavior,
replacement installation without uninstall, Cat Food acquisition and qualified
direct APK publication are **not accepted**. There is no local emulator/ADB
installation or /dev/kvm, and no connected physical-device evidence.
Candidate APK hashes are recorded below for later comparison; their names do
not assert publication. No APK download URL is fabricated or promoted into
the Cat Food feed. No merge or job-completion claim is made.

Each physical acceptance must bind the source above and the corresponding
exact APK hash from artifacts.tsv, identify the handset instance, exercise
generators/inverses, five-point completion and transformed selections,
play/pause/step/undo/redo/reset, reopen/checkpoint continuity and a replacement
install. A1 and C67 remain separate pending obligations.
