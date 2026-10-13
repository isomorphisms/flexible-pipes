# College and good jobs — one checked model

Continue the existing renderer and [isomorphisms/flexible-pipes PR #104,
“Add reproducible animated college/job Venn pipeline”](https://github.com/isomorphisms/flexible-pipes/pull/104).
Source belongs in the repository. Deliver the movie, not a source archive.

`models/CollegeVenn.idric` owns the four disjoint population cells, the events,
complement, query labels, and exact integer weights for every frame. Both
percentages use the same intersection/conditioning operation. Bad job or no
job is the whole universe outside the good-job set.

Good-job holders among graduates falls from 50.0% to 20.0%. Graduates among
good-job holders stays at 37.9%. These are illustrative weights, not employment
statistics.

## Representation and motion

The good-job disk stays fixed. College membership is a rectangle whose right
edge expands while its other edges stay fixed. The overlap and good-job
population remain fixed; college-only growth transfers weight from the cell
outside both sets. Total population weight stays 8600. The former sliding-circle
implementation did not guarantee monotone membership.

`examples/college-job-venn.json` supplies presentation choices, not percentages
or growth. The existing Python/Pillow renderer and Python checker remain
inherited migration debt.

## Execution and evidence

`pipelines/college-job-venn.json` runs the actual Idriç model check/evaluation,
rendering, and movie verification through `scripts/run-pipeline`. The workflow
pins Idriç at 2734ac5a86610eddfab73b1644d72b4ac85a65ee. The checker explicitly
selects that checkout's bootstrap library prefix. A version string alone does
not qualify the consumer runtime.

The model stage requires a fresh executable, a valid positive control, nine
semantic type rejections, 768 independent conditional queries, 392 movie
queries, and five rejected corruptions. Empty conditioning populations remain
undefined. Error diagnostics invalidate success even when exit status is zero.
Fixture constants are qualified to prevent accidental implicit rebinding.

Receipts bind the model, checker, generated executable, evaluated output,
compiler launcher, compiler application/runtime files, and library prefix.
New attempts invalidate old success before compiling. Log names differ by
more than letter case.

Outputs under `.flexible-pipes/artifacts/college-job-venn/` include the MP4,
first/last PNGs, source frames, endpoint cell/complement masks, model TSV, and
model/render/acceptance receipts. This version does not emit a GIF. Checks cover
every counter, endpoint mask areas and partitions, video dimensions/rate/count,
and every decoded frame against its source frame.

## Remaining boundaries

Endpoint mask files are not independent proof of every visible region in every
frame. Wrong-label and wrong-hatching mutations with correct metadata still
need independent rejection checks. Monotone inclusion is checked by the
renderer; it is not yet an Idriç theorem over a typed trajectory.

The bootstrap runtime has not been qualified as a standalone relocatable
package. Independent ai-ci promotion and trusted attachment delivery remain
unaccepted. Keep this PR draft. See `college-job-venn-recovery.md`.
