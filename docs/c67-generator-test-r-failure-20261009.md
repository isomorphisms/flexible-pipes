# C67: the fetched Kitchen generator was readable but `test -r` rejected it

On 2026-10-09 the user ran the merged ten-repository batch on the MIRO C67. The batch fetched the pinned Kitchen candidate and generator, read both first lines successfully, and checked their Git blob identities. Immediately afterward, a redundant Grease `test -r "$generator"` predicate reported the generator unavailable:

`Kitchen Grease program generator is unavailable before materialization`

The batch stopped before `BATCH MATERIALIZATION`, before preflight, and before any transfer POST. Independent repository inventory still showed all ten repositories under `isomorphisms` with their expected IDs.

This is an Android/Grease runtime acceptance failure in the access predicate, not evidence that the file was absent: the same file had just been read with `head`. The repair removes the `test -r` admission rule. The exact fetched file is admitted by an actual read into a private probe file and by matching the required `#!/usr/bin/env grease` first line. Blob identity remains pinned before download.

A static regression rejects reintroducing `test -r "$generator"` and requires the real read/header check. Native-Grease batch tests still cover ten materialized Kitchen programs, ten first-run simulated POSTs, idempotent rerun, wrong-ID refusal, non-404 refusal, and aggregate final verification.

Physical C67 live transfer remains NOT_VERIFIED until the user runs the repaired pinned batch and the resulting GitHub ownership is read independently.
