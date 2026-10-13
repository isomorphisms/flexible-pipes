# College and good jobs — an area-correct animated Venn diagram

An illustrative counterpoint to the title **“You can't get a good job without a college degree”**: a fixed good-job circle and a growing college circle whose good-job overlap stays fixed. The growing area represents college graduates with bad jobs. The footer shows *college graduates with bad jobs : college graduates with good jobs*, moving through 2:1, 3:1 and 4:1.

This is **not empirical labor-market data**. The ratios are chosen for the illustration.

The geometry is checked analytically. If the fixed overlap has area *I*, the college circle at ratio *q* has radius `sqrt((q+1) × I / π)`. Bisection finds the center separation giving exactly overlap *I*. It follows that the college-only area is `q × I`, regardless of which frame is shown. All values and timing are in `examples/college-job-venn.json`.

To render directly from this checkout (Python ≥3.11, Pillow, ffmpeg, ffprobe, Inter or DejaVu fonts):

```sh
python3 scripts/render-college-job-venn.py --config examples/college-job-venn.json
python3 tests/check-college-job-venn.py --config examples/college-job-venn.json --output-dir .flexible-pipes/artifacts/college-job-venn
```

Registered Flexible Pipes invocation:

```sh
python3 scripts/run-pipeline college-job-venn
```

The checked-in `pipelines/college-job-venn.json` is authoritative: **render** then independent **verify**. Standard FP stage receipts bind argv, exit status, hashes of standard output and standard error, and repository revision. The generator writes a content receipt with the config digest, font and FFmpeg identities, image hashes, exact frame count and the computed milestone intersections. Delivering attachments to ChatGPT's UI is a separate visible-delivery step, **not** proven by local pipeline success.

Default outputs under `.flexible-pipes/artifacts/college-job-venn/`:

- `college-good-jobs-venn.mp4` — 16:9 H.264
- `college-good-jobs-venn.gif` — looped, 720px wide
- `college-good-jobs-venn-preview.png` — final frame
- `college-good-jobs-venn-receipt.json` — hashes and acceptance facts

There is no model inference in the renderer. A future model stage may propose claims or visuals, but it must not silently replace the checked mathematical ratio or promote empirical statistics without sourced inputs and a separate validation policy.
