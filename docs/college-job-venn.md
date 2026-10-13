# College and good jobs — conditional percentages

Keep editing `scripts/render-college-job-venn.py` on the existing college/job
Venn branch and PR. The repository is the source handoff; send the movie itself,
not source ZIPs or duplicate scripts.

## Sets and their complement

Let U be all people in the diagram, G the good-job circle, and C the college
circle. **Bad job or no job is the whole complement U minus G.** It includes
both C minus G (graduates without a good job) and U minus (C union G) (people
without a degree and without a good job). It is not just the college-only
crescent, and college membership must not appear in its definition.

The universe now has a visible rectangular boundary labeled ALL PEOPLE.
Diagonal hatching covers U minus G, including outside both circles. The label
BAD JOB OR NO JOB describes that entire hatched region. The old arrow singling
out the college crescent has been removed. Both circles, the overlap area,
the growth schedule, and the two conditional percentages remain unchanged.

The header stays **You can't get a good job without a college degree**.
The footer has two distinct conditional percentages, not a bad-jobs : good-jobs
count ratio:

| Counter | Numerator | Denominator |
| --- | --- | --- |
| % of college graduates with a good job | College intersect good jobs | Entire college circle |
| % of people with a good job who have a college degree | College intersect good jobs | Entire good-job circle |

Both fractions are multiplied by 100. The exact same per-frame values supply the
visible numbers and the receipt. Labels are kept intact, split over two lines
only for layout. The left percentage falls as the college circle expands; the
right stays constant because the good-job circle and overlap stay fixed.

With the unchanged illustrative geometry, the left counter moves through
50.0%, 33.3%, 25.0%, and 20.0%. The right stays at 37.9%, computed from
`100 × 50000 / (π × 205²)`. Neither percentage is an employment statistic.
Do not replace the right number with a more persuasive invented value while
leaving the geometry unchanged.

## Geometry and inputs

`examples/college-job-venn.json` owns the title, palette, geometry, and timing.
The existing `start_ratio` and `milestones` remain geometric expansion controls,
not footer statistics. For overlap area I and college-only / overlap ratio q,
the college radius is `sqrt((q+1) × I / π)`. Bisection finds the center separation
giving overlap I. The college-only area reaches 2I, 3I, then 4I, as originally
requested. This is the part of college with a bad job or no job, not the entire
population without good jobs.

## Execution

Python 3.11+, Pillow, ffmpeg, ffprobe, and Inter or DejaVu Sans are required.
The existing Python renderer and checker are migration debt, not a newly
approved Python control-plane implementation. This revision repairs their
existing output; it does not add another runtime or bypass the FP runner.

From the repository checkout:

```sh
python3 scripts/run-pipeline college-job-venn
```

`pipelines/college-job-venn.json` remains authoritative: render, then verify.
The existing workflow checks out the exact PR head and invokes this pipeline.
A successful ancestor run is not acceptance of a new revision.

## Outputs and checks

The renderer writes MP4, GIF, preview PNG, the exact complement mask used for
hatching, and a version-3 content receipt under
`.flexible-pipes/artifacts/college-job-venn/`. It records source/config/font
hashes, runtime identities, every frame's circle geometry, both percentages,
and both displayed strings. The checker independently recomputes each
percentage, checks the denominator populations, numerically integrates the
milestone circle intersections without importing the renderer, and verifies
encoded frame count and file hashes.

The earlier `1 : 1` footer, swapping either denominator, omitting the factor of
100, and freezing the left percentage at its initial value are retained as five
rejected regression cases in the existing checker.

The new complement checks establish that G and the actual hatching mask are
disjoint and together cover exactly U. At all four growth milestones they
reject three incorrect masks: only C minus G, only outside both circles, and
all of U including good-job holders. Those are twelve rejection cases. The
complement is computed once without consulting the college circle.

Standard FP receipts record stage results. Local or hosted success does not
establish independent ai-ci promotion or a trusted ChatGPT attachment-delivery
receipt. No such adapter or promotion is claimed. No model inference occurs in
the renderer; the output remains explicitly schematic, not labor-market data.
