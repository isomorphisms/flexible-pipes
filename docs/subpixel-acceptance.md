# Subpixel host qualification

`subpixel-acceptance` version 2 executes the accepted whole-path/font producer
and independent oracle through Kitchen version 5, source-pinned ICK and
ICK-built Ike. Exact sources and runtime materials are in
`registry/subpixel-acceptance.json`; the complete assignment is
`tasks/subpixel/assignment.txt`. Version 1 and Kitchen 4 remain historical
local-patch qualification, not acceptance of the later whole-path/font engine.

On a fresh host prepared by that workflow, invoke the existing maintained runner:

`python3 /absolute/fp/scripts/run-pipeline subpixel-acceptance --param workspace=/absolute/fp`

Run from the same FP checkout. The runner resolves stage working directories from
its own source, so the caller's launch directory does not select inputs. The one
absolute parameter is checked by the pinned Kitchen recipe. Missing parameters,
changed runtime/recipe digests and mismatched producer revisions are tested to
stop before build. Previous output directories are refused rather than reused.

The native Grease engine and published portable `bin/grease` launcher are
authenticated separately. Only the launcher comes from the portable archive;
its Android engine is never selected on this x86_64 host. Consumer commands
invoke `grease`. The engine basename inside the package is implementation
provenance, not the public shell interface.

The hosted workflow checks identities and refusal fixtures, builds ICK and Ike,
renders four-mode paths and 32 font panels, and executes the independent
rational, whole-path and glyph oracles. Both independent markers and all ten
genuine defect rejections are required. The exact receipt checker must also
reject forged final-result and selected-target receipts. FP records each
stage's exit and output hashes; child timeouts bound the build and executions.

Retained evidence includes font masks and counts, PPM panels, per-mode path
metrics, native preview binaries, positive/negative logs, producer and
independent Ike receipts, result.tsv and its complete hash manifest. The
independent glyph oracle excludes a declared 1/64-pixel boundary strip.

The preexisting Python FP controller and retained producer/ai-ci POSIX recipe
interfaces remain explicit migration debt. No new Python is introduced.
Host GCC/Make build ICK itself; only ICK compiles Ike and consumer/oracle C.
The host driver then links those objects with the declared Linux runtime.

The workflow qualifies this draft registration at the exact checked-out head.
It does not deploy the separate protected admission service, dispatch a coding
model, grant merge/publication authority, accept the Conway bridge, or
qualify Android. `result.tsv` preserves those boundaries. Future producer edits
require a reviewed producer pin and corresponding independent oracle update.
A workflow configuration alone is not a successful registered run.
