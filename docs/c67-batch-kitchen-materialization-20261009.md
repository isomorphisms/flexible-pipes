# Batch materialization boundary after C67 generator disappearance

On 2026-10-09 the user ran the merged ten-repository batch on the MIRO C67. All ten repositories passed preflight with the expected immutable IDs. Before the first POST, the batch invoked the nested single-repository Flexible Pipes wrapper. That child resolved `KITCHEN_ROOT` to the batch workspace correctly but then reported that the already-fetched Kitchen generator at that path was unavailable.

Observed output ended at:

`TRANSFER mapping-class`

followed by:

`Kitchen Grease program generator is unavailable: .../kitchen/tasks/github-repository-transfer/render-standalone-github-repository-organization-transfer.ysh`

The GitHub state was checked independently afterward: all ten repositories were still canonical under `isomorphisms`; no transfer occurred.

This repair removes the unnecessary late dependency on a nested wrapper finding the transient Kitchen tree. Flexible Pipes now asks the pinned Kitchen generator to materialize all ten standalone transfer programs immediately after source admission and before GitHub mutation. Every program is parsed under native Grease and hashed before preflight. Execution later runs exactly those materialized Kitchen programs, checks their `status=verified` receipts and immutable IDs, then performs an independent final ten-repository destination/ID verification.

This is not a second transfer implementation: Kitchen still owns each mutation program and its transfer policy; Flexible Pipes owns batch orchestration, retained execution output, and aggregate verification. The old single-repository wrapper remains separately tested and available.

Acceptance must show:
- ten Kitchen programs materialized before mutation;
- exact ten source IDs preflighted;
- ten simulated POSTs on the first run;
- zero additional POSTs on rerun;
- wrong-ID and non-404 destination errors rejected before POST;
- native Grease, not a sh shim;
- final `BATCH COMPLETE` only after 10/10 destination verification.

Physical C67 live transfer remains NOT_VERIFIED until the user runs the pinned batch and the resulting GitHub state is independently read.
