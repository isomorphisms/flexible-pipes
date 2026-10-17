# PR-JUDGE-01: invalidate saved success before revalidation

Parent: https://github.com/isomorphisms/ai-ci/issues/238
Owner: https://github.com/isomorphisms/flexible-pipes/pull/127
Scope: fixture controller state; no platform deployment or physical acceptance.

## Types and invariant

The input is a previously accepted stage, a saved receipt, and a fresh readback action. The output is either freshly checked fixture acceptance or a nonpassing current status. The stage's accepted effect history remains separate from that status. A prior FixturePass must not serve as proof about a later readback.

The repair stays in the existing checked-Ithon controller. The adjacent job-delivery attempt records the established Idriç compiler/runtime boundary. No new Python implementation or backend fallback was authored.

## Reproduced defect

At FP fab9edcc4e4d31c566a749aad91acf01807ef19b, with independent AI-CI 41e3aeefab0e3249bdb743507bd51b5c273eb022 and checked Ithon d6e83969f82512e920fb17b44326cb54f31d015c, the original 59 runtime cases passed. A saved display-only success was resumed with changed readback bytes. The gate rejected HANDOFF_VISIBLE_MISSING, but the persisted delivery_status remained FIXTURE_PASS.

The generated initial test failed static checking because its empty list lacked an element type; a later expanded test needed a typed intermediate mapping before indexing. The exact added test bodies are retained alongside this note. They are extensions to the pinned runtime suite, not standalone programs. Those type-check failures are not controller failures.

## Repair and qualification

Invalidate delivery_status to AWAITING_HANDOFF_DELIVERY and checkpoint it before any resumed readback. This preserves accepted presentation/dispatch events. Four regression cases cover changed bytes and reader exceptions in display-only and display-and-dispatch modes, then prove valid retries do not repeat accepted effects.

The review pipeline records the original assignment, candidate source digests, runtime tests, and independently owned acceptance separately. Locally: all 63 runtime cases and the unchanged independent 57-case matrix plus nine rejection transitions passed. The original failing specimen was retained. The source snapshot was materialized by verified Git blob identities, not claimed as an original Git checkout; repository_commit in these local receipts is null.

Original runtime stdout SHA-256: 0cf625bb2794910507c95ca1fd676bc50fafd227f84f820e1c9d22885c61dd9d
Repaired runtime stdout SHA-256: 2e1ed3e03031a001ec194c15da78ded826596feb5e8cae89b130b5bda1a352cb
Unchanged independent acceptance stdout SHA-256: 6fa657db3d57186dcab24ffc4db70ff28e123fc949235f0fa56800eeaa3ff5a8
Repaired handoff source SHA-256: 6b959c22a1c2ffd5527650fdff6ee8e727d1f46d985ff990689e948ec068c171
Repaired runtime test source SHA-256: 7f404d1e9270523990acc909ecdd142eae5d4082a892776318af07e81585ce7d

Use the maintained scripts/run-pipeline entrypoint with pr-judge-01-review and verified absolute ithon, fp-root, aici-root, aici-test and results parameters. The checked-in job-delivery workflow also runs the updated runtime suite through the existing fp35-delivery-acceptance pipeline. Hosted exact-head acceptance must be refreshed after publication.

Remaining Idriç work is still the parent example's real SHA-256/transport/compiler boundary; this narrow correction does not claim to remove it.
