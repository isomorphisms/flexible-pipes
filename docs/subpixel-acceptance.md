# Subpixel host qualification

`subpixel-acceptance` is a concrete named pipeline, not another planning issue.
Its immutable inputs are recorded in `registry/subpixel-acceptance.json` and
materialized by `.github/workflows/subpixel-acceptance.yml`. Kitchen version 3
performs source preflight, builds the pinned ICK compiler and Ike, runs the actual
producer preview, then runs the independently pinned ai-ci oracle, four compiled
source mutants and two forged-receipt negatives. FP captures each stage's real
exit status, output hashes and the executing control commit. Child timeouts bound
the compiler build and subsequent executions.

On a fresh host prepared by that workflow, invoke the existing maintained runner:

`python3 /absolute/fp/scripts/run-pipeline subpixel-acceptance --param workspace=/absolute/fp`

Run from the same FP checkout. The runner resolves stage working directories from
its own source, so the caller's launch directory does not select inputs. The one
absolute parameter is checked by the pinned Kitchen recipe. Missing parameters,
changed runtime/recipe digests and mismatched producer revisions are tested to
stop before build. Previous output directories are refused rather than reused.

Grease's compiled implementation in the published artifact uses the multicall
basename `ysh`. Keep that verified basename; calling the copied binary `grease`
fails. New orchestration is Grease; the preexisting Python FP controller and the
retained producer/ai-ci POSIX recipe interfaces remain explicit migration debt.
Host GCC/Make build ICK itself; only ICK compiles Ike and consumer/oracle C.
The host driver then links those objects with the declared Linux runtime.

The workflow qualifies this draft registration at the exact checked-out head.
It does not deploy the separate protected admission service, dispatch a coding
model, grant merge/publication authority, implement the whole-curve engine, or
qualify Android. `result.tsv` preserves those boundaries. Future producer edits
require a reviewed producer pin and corresponding independent oracle update.
The next implementation remains the existing FP issue #145.
