# Mathieu exact-source continuation — 2026-10-21

Application source: [3b860d41841209b62433be80be76b62ecfdfbfcf](https://github.com/isomorphisms/mathieu/commit/3b860d41841209b62433be80be76b62ecfdfbfcf).
The application remains a draft and the build assignment remains incomplete.

The checkpoint fix preserves the actual in-flight permutation transition, cycle/frame, pause/play mode, redo history, display settings and 64-bit logical time. Portable little-endian encoding replaces the earlier C structure dump, which restored only the completed permutation and discarded interrupted motion. Restore validates exact generator/undo provenance and rejects corrupt/truncated input without partially mutating the live session.

| Evidence | Result | Scope |
| --- | --- | --- |
| Debug and Release host tests | PASS | Exact groups/designs/Golay plus controller/raster tests |
| Interrupted-session continuation | PASS | Both groups; paused intermediate dancer positions, 400 continuation ticks, undo/redo, 125 truncations/byte changes and checksum-valid semantic corruptions |
| AI-CI GAP reference comparison | PASS | 5,009 exact lines; word/design/code corruption rejected |
| Native libraries, Debug and Release | PASS | armeabi-v7a, arm64-v8a, x86_64; ICK C frontend and separate NDK assembly/link stages |
| Signed APKs | BLOCKED | No application-owned permanent signer declared |
| Hosted required workflow checks | NOT_RUN | Local FP execution is not hosted CI |
| Android window/input execution | NOT_RUN | No emulator installed here; no emulator PASS |
| Physical A1 / C67 | NOT_RUN | No physical device channel here |
| APK replacement install and Cat Food delivery | NOT_RUN | Requires signer-bound APKs and actual target evidence |
| Complete event replay and video export | NOT_ACCEPTED | Checkpoint persistence is not video acceptance |

Execution inputs: FP 8f38cb8980f4ea88f4737b080d80fbdb9a51835c; Kitchen 775482a9ef3cd56fc32d00c07ed12de40ee653be; Ike 3f513e58ed2b83946fca8e9be6a952a582bafb85; AI-CI 4401133889e089695cd1475dbe7b45473fafc497. Exact compiler binary digests and NDK source-properties digest are in each stage's materials.sha256. Six output library hashes are retained separately.

The existing FP Python runner and Kitchen Grease entrypoint were invoked unchanged. The Grease interpreter's LeakSanitizer initially failed while inspecting this container's process list after the application tests passed. Final runs set ASAN_OPTIONS=detect_leaks=0 for that existing launcher; this is not an application leak-check PASS. Application test flags remain visible in the logs.

No application merge, release, signing-key generation, APK installation, physical-device claim or completed-job claim occurred. Existing earlier receipts are historical evidence for their own application revision.
