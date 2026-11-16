# Registered Android native APK producer (candidate)

Run the existing pipeline runner using the registered operation named
android-native-apk, with a build host that has already materialized and
verified the input checkouts and ICK object. The current registered consumer
is isomorphismes/wegert; other apps need a reviewed entry, not a substituted
source path selected by a model.

Required environment for registered mode:
  FP_ANDROID_REPOSITORY (an entry in registry/android-native-applications.tsv)
  FP_ANDROID_SOURCE_SHA (full exact 40-character Git commit)
  FP_ANDROID_APP_ROOT (verified checkout at that revision)
  FP_CATFOOD_CHECKOUT (pinned policy checkout)
  FP_AICI_CHECKOUT (pinned policy checkout)
  FP_ANDROID_NDK_CHECKOUT (pinned direct packager checkout)
  FP_ANDROID_ICK_OBJECT (actual source-built ICK AArch64 object)
  FP_ANDROID_ICK_OBJECT_SHA256 (exact object bytes)
  FP_ANDROID_OUTPUT_DIR (new output directory)
  ANDROID_HOME and ANDROID_NDK_HOME (build-host Android SDK/NDK)

Invoke:
  python3 scripts/run-pipeline-legacy.py android-native-apk

The command uses the *registered* application recipe and source revision to
produce both required APKs. It then constructs the exact target/APK map and
delegates artifact acceptance to AICI's independently approved Cat Food
companion-plan gate. AICI failure fails the entire pipeline. The runner's
stage receipt distinguishes build output from independent artifact approval;
the operation never reports physical-device PASS.

Cat Food #128, android-NDK #18 and AICI #230 are now accepted on main,
at merge commits 395cdb37a542e653b77d606879bcb78362f2485e,
2b93dc9a84641e5f7eeb373c4360ff0538facd78 and
35cb2749be232e6cd0ac9d9ae3e33266b1d19aa3 respectively. The producer checks
main ancestry for all three policy checkouts before execution. Wegert #72
retains unique paired NativeActivity work after #73 and is being reconciled
against actual main. Current-head missing-input, tampered-object and
unregistered-recipe negatives pass, as do the existing preflight fixtures.
Hosted execution of this exact registered operation remains required; fixture
registration is not a positive producer or artifact receipt. It cannot publish
completed builds on the strength of an unmerged policy or unverified ICK object.
Bash and the legacy Python runner are migration debt, not a newly authorized
general shell/scheduler framework.
