# Proposed Mathieu development signing identity

This proposal has not generated or selected a key.

- Application ID: org.isomorphisms.mathieu.
- Lane: permanent public development signing for direct sideloaded builds.
- Application-owned path: android/signing/mathieu-development.p12.
- Format: PKCS12; alias: mathieu-development; RSA 3072-bit key.
- Public test passwords: android. The keystore is intentionally non-secret.
- Validity: 10,000 days. This identity is separate from any future production/store signer.
- Initial versionCode: 1; subsequent packages must keep the same signer and a nondecreasing versionCode.
- Generate this one key once after explicit approval, commit it with its certificate SHA-256, and have the application recipe pin that exact digest.
- Use the maintained android-NDK packager; missing or changed signer must fail closed. Never uninstall to bypass a certificate conflict.
- Build separate Mathieu-A1.apk (armeabi-v7a) and Mathieu-C67.apk (arm64-v8a), plus an emulator candidate.
- Before human delivery, perform finished-APK certificate/package/ABI checks, independent AI-CI acceptance and Cat Food registration. Physical installation, interaction, persistence and replacement-update acceptance stay separate.

The currently pinned android-NDK/AGENTS.md says “never generate or silently select a signing key for a maintained installable APK.” The public development signer therefore remains an explicit human decision; no borrowed app certificate or per-run random signer was used.
