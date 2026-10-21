# Moonrise / small Tarot markers — test candidates

Source: `1d1153074cc2fde872f3bd29014c19881c52d2e1`.
Package `org.isomorphisms.mathieu`, versionCode **2**, versionName
`0.1.1-development`, minSdk 26 / targetSdk 35.

The user requested a Wes Anderson palette, small Tarot markers (four suits ×
six forms), and very small digits. The renderer now uses Moonrise2 colors,
original Wand/Cup/Sword/Pentacle line glyphs, six badge forms (circle, square,
diamond, triangle, hexagon, shield), smaller bodies and a tiny 3×5 digit font.
M12 uses three forms per suit. Thin rings show selections and Witt blocks.
The ATLAS permutations, coordinates, touch hit targets and checkpoint format
are unchanged.

Both host profiles pass the mathematical, actual touch/controller/raster and
checkpoint tests on a clean checkout at this exact head. The added image
checks establish that all 24 suit/form markers differ and transport
pixel-for-pixel under generator B in both layouts. A real renderer frame was
visually inspected; no generated artwork was substituted.

Both ABIs compile in Debug and Release through ICK + NDK assembly/link.
Separate Release payloads are stripped and packaged through android-NDK
`11edd1e0d9748d7c618413ec9f5afad52049046a`.
The packager verifies package, version, label, NativeActivity, ABI payload,
no DEX and actual signing certificate; a separate apksigner verification also
passes for both finished APKs.

| Candidate | Native before/after stripping | APK bytes | SHA-256 |
| --- | --- | --- | --- |
| Mathieu-A1.apk | 52,664 / 39,912 | 33,213 | `f0d62392c49403f28259d2c4ebcee9e427eb5b2689827dd4f5d52f6298167620` |
| Mathieu-C67.apk | 54,528 / 46,040 | 37,307 | `6f9242e332f4722c7680584dfc77d6b5f8d91bfd0b7d3a2d5fbd02a74b0da530` |

The permanent certificate remains
`f997a30170a967e073ab47e1212a71b3967ffe2e1e88d78d659c77bf085cb3fe`;
package identity is unchanged and versionCode increases from 1 to 2.
Replacement installation has not been observed for version 2.

The user reported that the previously supplied **version 1** C67 candidate
runs, with a screenshot showing M24, a nine-move word and an intermediate
permutation. This is human-reported physical launch/visible-state evidence.
The handset instance and installed bytes were not independently retrieved.
It does not establish version 2 acceptance, the full interaction matrix, or A1.

These are direct candidate Makefile/packager checks. No Grease runtime was
invoked for this presentation update. The [earlier D consumer record](../b338e3c-d-consumer/README.md)
belongs to source b338e3c; it is not silently carried forward to this head.
Permitted Grease admission, current-head maintained FP/Kitchen/Ike execution,
independent producer policy, emulator execution, version 2 physical A1/C67
behavior and replacement updates, and qualified Cat Food publication remain
open. The user explicitly requested APKs to try; candidate handoff does not
constitute qualified feed delivery or job completion.
