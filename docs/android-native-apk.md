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
  python3 scripts/run-pipeline android-native-apk

The command uses the *registered* application recipe and source revision to
produce both required APKs. It then constructs the exact target/APK map and
delegates artifact acceptance to AICI's independently approved Cat Food
companion-plan gate. AICI failure fails the entire pipeline. The runner's
stage receipt distinguishes build output from independent artifact approval;
the operation never reports physical-device PASS.

This is an implementation candidate pending merge of Cat Food #128,
android-NDK #18, AICI #230 and Wegert #72, plus hosted execution fixtures
for this exact pipeline. It cannot legitimately publish completed builds on
the strength of a candidate policy checkout or an unverified ICK object.
Bash and the legacy Python runner are migration debt, not a newly authorized
general shell/scheduler framework.
