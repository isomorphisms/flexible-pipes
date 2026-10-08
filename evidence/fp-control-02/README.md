# FP-CONTROL-02: repairs and evidence, 2026-10-08

The mission is incomplete. These are source repairs and executed host fixtures,
not activation of mandatory ChatGPT routing or acceptance of a live transfer.

## Refreshed source

| Repository | Default branch observed |
| --- | --- |
| flexible-pipes | 9775aa324f523cbc6c758e89461915484a5a0fc7 |
| kitchen | 7953ee33280ff6e276f31204995c2d2491f3e588 |
| ai-ci | 01608a2493fa409463f70e8fbfd8a123ef59ee85 |
| catfood | 609a9628d5a52860f956bf62e0914a0cd03292ae |
| cockswain | f6ad9f2ff1a15676bfcc7a139e240bfedaf195fb |

Continued isomorphisms/flexible-pipes PR #31, “Implement registered Kitchen
script execution and preserve FP2 qualification attempts”, retained branch
`implement/fp2-runtime-qualification`, starting at
`1fbe5d3373c983aeecbe355e23d9f12e6737b41d`:
https://github.com/isomorphisms/flexible-pipes/pull/31 . No replacement PR.
Its merge base with current main remains
`43ff931660254f30094a53596af2e89d35e8e643`. Integration must retain the newer
job-delivery, attachment, fork, organization-pin and other default-branch work.

## Actual caller boundary

| Surface | What it actually loads | Acceptance / limitation |
| --- | --- | --- |
| This ChatGPT Work session | Available instructions and GitHub/terminal capabilities; no Flexible Pipes or Kitchen callable adapter exposed | Interpretation and voluntary invocation; cannot enforce all future responses |
| Main terminal/workflow | Generic `scripts/run-pipeline`, caller pipeline spec; request-branch workflow executes event checkout | Command completion only; no independent operation approval |
| Retained installed client | Fixed Grease/Ithon, `/etc/flexible-pipes/client.json`, signed GitHub event adapter | Inactive configuration rejects before requesting credentials |
| Retained TLS supervisor | Fixed deployment, registry, material/tool digests, admission and isolated workers | Existing candidate authority boundary; not activated |
| Kitchen generator | Maintained candidate 9, six explicit data arguments | Generates exact standalone Linux Grease bytes without live transfer |
| AICI / Cat Food | Independent observed-API validator / sealed-script validator on retained branches | Fixture acceptance / delivery respectively; neither owns Kitchen recipes |
| Main job-delivery controller | Captured stage bytes plus trusted sink/dispatcher and AICI gate | Repository explicitly says no deployed ChatGPT visible-sink adapter |
| Cockswain | Supervisor and retirement surfaces; no `bin/cockswain-dispatch` | Existing dispatch test executed and fails because implementation is absent |

The available API showed the old `functorial-games/young-tableaux` path redirecting
to numeric repository 1405872600; a separate destination lookup returned the same
ID at `isomorphismes/young-tableaux`, public and not a fork. This is current
read-only ownership evidence, not this task executing the historical transfer.
No transfer request was sent to GitHub.

## Executed repairs and controls

- Reused the exact October 8 reproducer from
  https://github.com/isomorphisms/flexible-pipes/issues/24#issuecomment-6064340162 .
  The runner blob remains `45e7b509d86a14b6352bb61680b7580036ba2ac4`.
  `legacy-summary.json` records all six matching characterizations: three controls
  and three acceptance-boundary counterexamples. These are not six acceptance
  passes. `characterize-legacy-runner.py` is the original audit harness, not a
  new production Python implementation.
- Reproduced delivery's premature PASS: the original `submit` raised
  `DELIVERY_DIGEST_MISMATCH` but left `result.json` as PASS. The regression failed
  with `REJECTED_DELIVERY_LEFT_PASS: changed-bytes`; the old receipt is retained.
- The repaired client records PENDING, retains the untrusted service response,
  validates the complete artifact set before exposing files, and records PASS
  only after successful publication. Rejection writes FAIL. It rejects empty
  PASS, duplicate artifacts, substituted bytes and reserved output names.
- Nine focused real-client cases passed through checked Ithon with inert
  transport: valid, changed bytes, missing delivery, empty PASS, wrong artifact,
  duplicate artifact, reserved receipt name, blocked-with-bytes, and legitimate
  blocked result. See `delivery-checks.json`. This is not TLS acceptance.
- The actual generic `regression-history-smoke` still completes. Its receipt now
  explicitly says exploratory, caller-supplied-command-execution and
  `qualified_operation: false`; this preserves useful exploration.
- Qualification now includes the client regression, binds its source, and is
  eligible for every PR change and pushes to the retained branch. The old path
  filter omitted delivery/admission/bootstrap changes.
- Corrected invocation documentation to distinguish current main, retained
  registered entry and inactive installation. No instruction-only adoption claim.

## Maintained generation

Kitchen's retained Ithon diagnostic was extended to accept the same six explicit
request fields. The recipe itself was not rewritten. Both the synthetic sample
and the public Young Tableaux transfer parameters ran through the maintained
Grease generator, repeated generation and all 13 independent AICI API scenarios,
including fresh homes/unrelated directories containing spaces and quotes.
The latter tests are in Kitchen `evidence/fp-control-02/`. Generation and simulated
script execution are separate; no real transfer occurred. The known source
fixture ID/login parameters are not authentication or future mutation authority.

Grease was built on this disposable Ubuntu 24.04 x86_64 host through Cat Food's
existing build recipe, using Grease `f19c94c6df18cddbdc1e81463e5bd689533e3c13`,
Oils gitlink `6d29702a10ea9eb72a43950554dbcd4174d07a89`, and checked Ithon
`d6e83969f82512e920fb17b44326cb54f31d015c`. No device build or service activation.
The qualification workflow remains the owner of full hosted runtime acceptance.

## Remaining boundaries

The container maps only UID 0 and has no `/usr/bin/gh`; it cannot qualify the
separate-worker/actual-gh supervisor suite. Historical exact-head hosted run
37419044563 was refreshed as completed/success at the original retained head:
https://github.com/isomorphisms/flexible-pipes/actions/runs/37419044563 . It does
not qualify these repairs or establish deployment.

The generated body is about five kilobytes, has Linux-specific paths and requires
Grease plus authenticated gh at execution time. It is not yet the requested
compact paste unit for a fresh phone. No compact handoff is claimed.

Source review also identifies two still-unverified acceptance gaps to exercise:
the delivery client does not compare a PASS result's request/operation identity
with its submission, and the engine's cached-PASS path checks artifact bytes but
does not compare the old qualification identity with the active release. These
need targeted bad specimens and valid cache controls before choosing repairs.

Reusable evidence must bind recipe, checker, runtime, contract, operation and
context. Changed parameters require fresh generation/identity checks; changed
implementation, oracle or runtime requires requalification. No current deployed
cache is established here. Fresh model interpretation remains distinct from
deterministic orchestration and recorded replay.
