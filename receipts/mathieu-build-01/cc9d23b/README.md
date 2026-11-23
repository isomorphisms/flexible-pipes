# MATHIEU-BUILD-01 — executed boundary, 2026-10-21

Source: isomorphisms/mathieu at cc9d23bb74bd31fe63cf601096eb42aee6f21967.
[isomorphisms/mathieu PR #3, “Implement exact Mathieu choreography and native Android application core”](https://github.com/isomorphisms/mathieu/pull/3) remains draft. This is partial execution, not completion, release, installation, or merge acceptance.

| Boundary | Observed result |
| --- | --- |
| ICK host engine, Debug and Release | PASS |
| Touch → permutation state → actual raster, both layouts and A1-sized framebuffer | PASS on Linux host |
| Independent GAP comparison of 5,009 reference lines; corrupt word/design/code exports | PASS; all three corruptions rejected |
| M12/M24 orders, stabilizer chains and five-transitivity | PASS |
| All 132 hexads / 759 octads, every five-subset unique | PASS |
| Golay dimension 12, 4096 words, complete specified weight distribution and invariance | PASS |
| Native Android libraries, armeabi-v7a / arm64-v8a / x86_64, Debug and Release | PASS compile and strict NDK link |
| APK signing / packaging | BLOCKED: Mathieu has no declared persistent signer |
| Hosted required checks on the application head | ABSENT; empty combined-status result must not count as PASS |
| Emulator input / window execution | NOT_RUN |
| Physical MIRO A1 / C67 installation, launch and interaction | NOT_RUN |
| Cat Food APK delivery | NOT_RUN |
| Saved real session → replay → verified video | INCOMPLETE; journal foundation only |
| M11/M22/M23 interactive actions | NOT_IMPLEMENTED; derived stabilizer orders are verified |
| Whole-job independent acceptance / merge | NOT_ACCEPTED / NOT_MERGED |

## Exact execution inputs

- Flexible Pipes runner/pipeline source: 8f38cb8980f4ea88f4737b080d80fbdb9a51835c.
- Kitchen recipes: 775482a9ef3cd56fc32d00c07ed12de40ee653be.
- AI-CI GAP gate: 4401133889e089695cd1475dbe7b45473fafc497.
- Ike source receipt: 3f513e58ed2b83946fca8e9be6a952a582bafb85; executable SHA-256 dfdc99d4d36b36e6cced60d417df02d1528d73ace7d738a32451c5a825effb0b.
- Host ICK installed executable SHA-256: 45805e3295f2709737fcc87985a8a2341aa8663ff8e4e398d2a9d78dc1283e10. The installed byte identity is observed; a new source-build provenance claim is not invented for that reused stage.
- ARM64 ICK fbe86e23d55cfec2000c08e61deea2a407fd7175; prebuilt stage from [coefficient-root-dance run 38606599229](https://github.com/isomorphismes/coefficient-root-dance/actions/runs/38606599229), artifact 11916480509, archive SHA-256 216dfac9516ddbf9d12ae858549461610145c46da2b9726f25df4a46f3673b14. Driver SHA-256 43c1428950cebac57fbd428f1888819720f70f14de3a02e6bc4e07911a872fc6; cc1 SHA-256 e337216a53b771e96c4ac58247220ef6de55f1498cd548665ad674d1162b22ac.
- ARM32 prebuilt compiler from [ICK run 39362629417](https://github.com/dilapidated-shed/ick/actions/runs/39362629417), artifact 12238352717 named ick-a1-e822c13df4f67b1807a792d3d6feeb1924879400. Archive SHA-256 baf747c948ebdb01e70e347d25853eeb43030cc02901b56b167ffee9fa998a81. Driver SHA-256 c78697d096ffe8ba10fbcc3bae9b35d0c934bee11a3626813656ac84e126f9ad; cc1 SHA-256 d308fd5cc7b3eb3269bff63ec60a7614c44f3bd0dce0e2b748edb2b6d77b74fb. The consumer used these exact bytes, not an assumed compiler from PATH.
- Android NDK r27c / 27.2.12479018; source.properties SHA-256 70f1c5165e6d997b18782a49cff71da7a3caacd0c4cd811da24c43359fb83cf6.
- Grease entrypoint SHA-256 37088097c36a2f82cf45aaea9392e4a4cf16155fecb9da87d08a9c7fb4d92e4a; actual runtime SHA-256 7e31cd05b7a9d8fb2a4a9e003a7f3fcb0159138506d17f0fb28da8cbe22aa85c. Its inherited sanitizer runtime required ASAN_OPTIONS=detect_leaks=0 in this container because LeakSanitizer cannot inspect the process task directory; this does not disable any application test.
- GAP 4.12.1-2build2, extracted from the declared Ubuntu snapshot packages into an isolated build-host directory.
- Idriç host permutation example: 94dfd99bd3e376507fedc8611053b7173b2519f0, Chez backend, compiled and executed successfully. No Android Idriç ABI claim.

The new control/gate branches are themselves drafts awaiting independent integration review:
[isomorphisms/ai-ci PR #316, “Verify exact Mathieu actions and Golay invariants with an independent GAP oracle”](https://github.com/isomorphisms/ai-ci/pull/316);
[isomorphisms/kitchen PR #75, “Prepare exact-head Mathieu builds through Grease and pinned Ike”](https://github.com/isomorphisms/kitchen/pull/75);
[isomorphisms/flexible-pipes PR #248, “Route Mathieu native builds and independent GAP acceptance through Flexible Pipes”](https://github.com/isomorphisms/flexible-pipes/pull/248).

## Failure and refusal evidence

Initial Android source compilation caught an obsolete app_dummy call and a missing Android window-flag header; both were repaired before the successful source head. The relocated ARM32 bundle required an explicit compiler prefix. Provisioning also attempted execution while cc1 was still being extracted, producing “Text file busy”; this was an orchestration error, not a compiler or application defect. The retained failing ARM32 FP receipt records that boundary. Successful retry followed completed archive extraction and verified executable setup.

The Kitchen host recipe rejected a deliberately wrong source revision before creating the proposed evidence directory. The independent GAP gate rejected corrupted word, design and code exports. Producer tests reject invalid bijections, an odd transposition outside the generated groups, and a duplicated design block.

## Remaining handoff

The existing android-NDK signing rule forbids generating or silently selecting an application signer. No Mathieu signer was found or invented. A dedicated permanent public development signer, or an explicitly selected existing suitable signer, must be authorized and recorded for org.isomorphisms.mathieu before producing signed candidate APKs.

Then package separate Mathieu-A1.apk and Mathieu-C67.apk through the maintained packager, run signing/update and independent artifact gates, perform emulator input/replay checks, deliver through Cat Food, and obtain actual A1/C67 installation/behavior receipts. No physical-device access or successful installation was observed in this session. FP #243 replay/export work remains a release blocker; this receipt does not retire it.
