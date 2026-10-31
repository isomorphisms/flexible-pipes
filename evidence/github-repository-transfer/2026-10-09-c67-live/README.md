# MIRO C67 live GitHub ownership-transfer acceptance — 2026-10-09

This directory records the first accepted live use of the maintained Kitchen → Flexible Pipes GitHub ownership-transfer path on the physical MIRO C67.

## What succeeded

The user copied one ordinary plain-text command from ChatGPT Android into Termux. The command fetched a blob-pinned Flexible Pipes batch, which fetched the pinned Kitchen generator and candidate, materialized ten standalone Grease programs before mutation, preflighted every source name and immutable GitHub repository ID, executed the transfers sequentially, and verified each destination.

After the user reported success, the connected GitHub account was read independently. All ten repositories in `repositories.tsv` were canonical under `isomorphismes` and retained their expected numeric IDs. That independent state read, not a zero exit status or a success sentence, is the live postcondition.

## Evidence classes

The evidence is intentionally split:

- **Visible delivery:** user-confirmed PASS for ordinary plain text in ChatGPT Android. Earlier fenced CodeBlock output rendered as an unavailable component and is retained as a failed delivery mode.
- **Physical execution:** user-confirmed PASS on MIRO C67 Termux using the Cat Food AArch64 Grease package.
- **Exact terminal transcript:** NOT RETAINED. Do not reconstruct or invent the final stdout bytes.
- **GitHub mutation postcondition:** independently verified PASS by canonical destination owner/name and immutable repository ID for all ten repositories.
- **Generic trusted chat adapter:** NOT DEPLOYED. This successful conversation is positive operational evidence, not proof that arbitrary future chat responses are intercepted or attested.

## What the scaffold must retain

1. **Use the maintained route.** Kitchen owns each standalone mutation program. Flexible Pipes owns batch materialization, execution order, receipts, and aggregate verification. Cat Food owns the physical Grease runtime and device facts. ai-ci owns independent acceptance rules.
2. **Materialize before mutation.** Fetch, identify, read, generate, parse, and hash every Kitchen program before the first transfer POST.
3. **Observed reads beat access predictions.** On this C67, Grease `test -r` rejected files that `head` had just read successfully. Admit downloaded scripts by an actual bounded read plus exact header/blob identity, not by a redundant readability predicate.
4. **Preserve exit status and response bytes separately.** Real `gh api` returned nonzero while emitting a REST 404 JSON body on stdout. Do not erase either channel with `$(... || true)` or assume errors appear only on stderr.
5. **Do not substitute interpreters.** Native Grease acceptance cannot be established by a fixture whose `grease` command simply invokes `sh`.
6. **Separate stages.** Visible handoff, target execution, mutation request, per-repository verification, and final aggregate verification are different claims.
7. **Success means current state.** Completion requires every destination to resolve canonically under `isomorphismes` with the original numeric repository ID. A generated script, green fixture, accepted POST, zero exit code, or user-facing claim alone is insufficient.
8. **Keep the interface small.** The successful Android handoff was one plain-text command with no assumed checkout, working directory, manual repository IDs, or separate downloaded attachment.

## Pinned accepted path

- Kitchen merge: `2d5c0afa372bb532750067a1a79194854f7236fb`
- Flexible Pipes merge: `6a162f17e9f2a677f621b6b8e397fa9b6bc58ea5`
- Batch script Git blob: `11158dc11770ba7ff755b82d39a5b212c31b3bee`
- Cat Food Grease archive SHA-256: `3ddb962ef313e528e525fa03518f494577e921c2201ecb49f7a11f2fbf4e82b2`

The machine-readable receipt and repository ledger are `receipt.tsv` and `repositories.tsv`.
