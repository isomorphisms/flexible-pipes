# October 21 continuation

This is candidate execution evidence, not registered-producer admission or APK
delivery. The task envelope remains SUN-CRYSTAL-GROWTH-C67-01.

The exact application build is commit
`e745edd98f5b8c854fbba4c72bb0a0a699aa50b5`, tree
`4b2b972e7351d9edc24bd32264ff20b7350baf5f`. All four ARM64 variants compiled,
linked and stripped. Native inspection passed; no APK packaging, signing,
installation, device rendering or delivery ran. `status.tsv` retains those
boundaries and the exact GitHub prerequisite failure.

The `crystal-growth-c67-native-candidate-20261021T121313.321656Z` run is the
clean exact-commit native result. Its pipeline hash matches the checked-in
candidate pipeline. The inspection run is
`crystal-growth-c67-inspection-20261021T121609.443539Z`. The host run at 12:08:33 passed, including
10,000 steps per material and the three mutation controls. Its application
snapshot buffer predates the final buffer enlargement; the mathematical and
render-adapter translation units match the exact native build. The final
application also passed an ARM64 format check and the full native build.

Earlier attempts are retained, not upgraded:

- 12:04:35: NDK linker alias had been extracted as text; hash gate rejected it.
- 12:05:41: host check rejected the same linker alias.
- 12:07:32: restored linker passed; compiler execute mode was missing.
- 12:08:02: verifier reproduced its pinned executable; the native recipe
  rejected untracked source files left in the dependency checkout.
- 12:09:02: clean dependency worktree allowed a native build of the working
  application changes, still based on the previous application HEAD. This is
  superseded by the later clean exact-commit result, not relabeled exact-head.

The archive SHA-256 was verified. Restoring its linker/readelf symlinks and
compiler executable mode restored the required pinned hashes; no expected hash
was changed. The native build retains an upstream Lua `tmpnam` deprecation
warning. `pipeline-before-clean-guard.json` preserves the early pipeline bytes;
the final native pipeline additionally checks tracked source before and after
building. The current source's registered-operation check remains intact.

The retained AI-CI verifier source is an unmerged candidate, not an accepted
shared-producer deployment. Its own tests and exact kernel reproduction do not
independently accept the Crystal growth implementation. The maintained
Kitchen/producer prerequisites, signing and C67 acceptance remain open.
