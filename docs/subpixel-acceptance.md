# Subpixel host qualification

`subpixel-acceptance` version 4 executes the corrected whole-path/font producer,
real Conway bridge and independent oracle through Kitchen version 7, source-pinned ICK and
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

The hosted workflow authenticates the exact published source-built ICK archive,
driver and frontend and freshly compiles Ike through that compiler. This is
declared artifact acquisition, not another compiler source build. The original
version 2 run built ICK and passed native tests/preview, then failed collection
because find's batched cp destination followed `{}`. Kitchen 6 corrects that
operation and executes a real collection/change-rejection fixture.

The workflow checks identities and refusal fixtures,
renders four-mode paths and 32 font panels, and executes the independent
rational, whole-path and glyph oracles. Both independent markers and all ten
genuine path/font defect rejections are required. The separate Conway stage
requires 22,778 full-scene checks, 5,979,792 definite sample decisions, ordered
translucent CLI pixels and seven genuine source defects. Its declared
1/32-pixel boundary strip excludes 243,696 comparisons. The exact receipt checker must also
reject forged final-result and selected-target receipts. FP records each
stage's exit and output hashes; child timeouts bound the build and executions.

The ninth stage independently decodes the emitted font previews, checking all
105,344 masks, printed counts and 6,742,016 fine-grid pixels. Literal bitmap
answers are exact; continuous geometry reports 5,015,040 definite and 41,472
excluded boundary samples. Exact image/mask/count equalities have no tolerance.
Twelve compiled source defects and four malformed inventories must reject
with unchanged expectations. The native path oracle supplies repeated union
and work-cap cases; targeted preview mutations use a declared one-panel scope
with an unchanged positive twin. The stage also checks the original collected
preview files and binds a separate exact Ike target/recipe receipt.

Retained evidence includes font masks and counts, PPM panels, per-mode path
metrics, native preview binaries, positive/negative logs, producer and
independent Ike receipts, result.tsv and its complete hash manifest. The
independent glyph oracle excludes a declared 1/64-pixel boundary strip.

The preexisting Python FP controller and retained producer/ai-ci POSIX recipe
interfaces remain explicit migration debt. No new Python is introduced.
The authenticated compiler was source-built through its declared stage-zero
boundary; only ICK compiles this run's Ike and consumer/oracle C.
The host driver then links those objects with the declared Linux runtime.

The workflow qualifies this draft registration at the exact checked-out head.
It does not deploy the separate protected admission service, dispatch a coding
model, grant merge/publication authority, or
qualify Android. `result.tsv` preserves those boundaries. Future producer edits
require a reviewed producer pin and corresponding independent oracle update.
A workflow configuration alone is not a successful registered run.
