# Pre-signing preparation

The successful run at 14:10:53 UTC exercises fourteen proposed signing-registry
cases and eight pre-signing packaging refusal/preservation cases. It reads no
keystore and produces no APK. The source-built verifier has SHA-256
`aad73dd9aa9af1e1fa5fcda86a18d832970c5d048cf45e5e5d7cb5d029485a79`;
its C source matches current AI-CI main. The registry proposal is
https://github.com/isomorphisms/ai-ci/pull/314, commit
`35205345c4d74e4ce630425f6f6c1ff1b0a5dd43`. It is not approved policy.

The initial run at 14:09:38 UTC failed: the newly authored version validation
used a pipeline conditional rejected by Grease's strict error handling. The
repair uses a single grep command with a here-string. The successful recipe
SHA-256 is `6c504f49d51f0436bfb403a5e93814c741403e8a60e5b6c003c8ab4f06b5a796`;
the test SHA-256 is
`246158babe8accc06f12c389cdddbf29788dbef878456fba0c5f84ef93249230`.
The initial failed attempt remains in this directory.

The existing public test-signing route was identified through Mostow's
maintained packaging workflow. It declares the same certificate already
registered for the existing three Crystal test packages. No usable keystore or
actual certificate was acquired here; explicit signer-use authorization remains
pending. No new key or signer migration is authorized. The SDK35/API34 archives
were checksum verified and aapt2 executed. The registered-producer, independent
mathematical and C67 physical acceptance obligations remain open.
