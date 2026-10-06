# Human-visible assignments use the existing stage artifact

A command/model worker's authoritative output is already captured in
`stdout.bin` with `stdout_sha256`. Optional `handoff` metadata extends that
stage receipt; it does not define another task format. The metadata specifies
audience/model, source context, optional execution target, the human request,
and its requested delivery mode. Its canonical contract digest and the exact
payload digest determine one identity. UTF-8 bytes, including the final LF,
are authoritative. No prose summary or pointer can replace them.

The default is `display-only`. `display-and-dispatch` and `dispatch-only`
require an explicit captured human mode; dispatch-only also requires an
unambiguous direct-execution phrase. This small conservative parser does not
claim to understand every equivalent phrase; an unsupported intent remains
blocked rather than being inferred from an available dispatcher.

The lifecycle is composition → observed visible delivery → optional dispatch
→ receipt. Explicit dispatch-only omits the visible step. `handoff.deliver`
takes trusted sink, dispatcher and ai-ci gate objects supplied by the
controller, never executable fields from a generated request. The sink's
`send(response)` returns the actual accepted `bytes`, `message_id`, and
`surface`; the dispatcher's `send(payload, id)` returns actual accepted bytes
and `dispatch_id`. A declaration that sending succeeded is insufficient.
The gate examines those captures before dispatch and after completion.
States and sequenced events keep visible delivery distinct from dispatch.

The response uses a top-level literal text block with a delimiter longer than
any delimiter in the assignment. ai-ci checks its full bytes against the stage
artifact. Plain full-text responses are also supported without HTML markup.
Summaries may surround a literal block. Nested/quoted blocks, hidden HTML,
links, altered/truncated assignments, swapped captures and wrong dispatches
are rejected. These are bounded supported response forms, not a general
Markdown renderer or screenshot-based proof of human perception.

Binary outputs use the same stage and handoff identity with version 2 and
`transport=attachment`. The attachment contract binds the source bytes,
delivered bytes, names, MIME type and connector provenance. A direct attachment
must preserve the source name and digest. A ZIP member names one canonical,
unique member whose basename is the delivered filename; extraction is bounded
and its bytes must match the declared digest. The trusted sink receives those
bytes and returns the bytes, file ID, filename, MIME type and surface it actually
accepted. A link, temporary signed URL, success flag, renamed file, changed MIME
type or mutated payload is not an observed attachment.

`recover(stage, correction)` retains the same payload/contract identity and
records `delivery-failed`. A new delivery follows that event. Accepted dispatch
is not repeated. “Where’s the text?” without recovered context is rejected by
ai-ci. The original request is retained rather than overwritten by the
correction.

## Adoption and evidence boundary

The maintained `scripts/run-pipeline` now prevalidates handoff metadata through
checked Ithon (`--ithon /verified/entrypoint`) before any command effects. When
the producing stage completes it saves the extended stage and complete
response artifact and returns nonzero `AWAITING_HANDOFF_DELIVERY`. Later stages
cannot execute. Neither that response file nor stdout is a visible receipt.
The trusted transport controller completes the same stage using `deliver`.
There is currently no deployed ChatGPT visible-sink adapter in this repository.
The attachment contract makes that adapter implementable and independently
checkable, but no platform delivery is inferred from local fixtures. The active registered
Kitchen/Android runtime work is separate; this change does not activate it or
qualify its existing deployment blockers. Its controllers can consume the
same captured-stage extension when they gain model-job operations.

`review_packet` runs the deterministic gate before supplying actual artifact,
actual response, original task, corrections and stage evidence to final review.
`review_decision` retains reviewer identity/revision, prompt, raw response,
reason, decision and input digest separately. Review can request a bounded
revision or block, but cannot turn absent delivery into PASS. This implements
the job-output portion of #17; visual preview inspection, real model execution
and independent creative-outcome calibration remain separate open work.

## Ownership and existing interfaces

Flexible Pipes owns representation, rendering, captured delivery/dispatch
mechanics and recovery. ai-ci owns behavioral rejection using that contract.
Existing #205 execution/API validators and #176 host checks remain required
for operational scripts; a visible job cannot inherit shell-execution
acceptance. The existing stage stdout/artifact hash is the common exact-output
identity, rather than another independent task classifier. Kitchen owns a
script recipe when that is the deliverable. Cat Food owns device/build facts
consumed by a particular assignment. Leaf repositories own neither policy.

Tracked work: [#35](https://github.com/isomorphisms/flexible-pipes/issues/35),
[ai-ci #219](https://github.com/isomorphisms/ai-ci/issues/219),
[#17](https://github.com/isomorphisms/flexible-pipes/issues/17),
[ai-ci #205](https://github.com/isomorphisms/ai-ci/issues/205),
[ai-ci #176](https://github.com/isomorphisms/ai-ci/issues/176).

The independent ai-ci response matrix and FP runtime/effect suite both retain
the sanitized October 6 recurrences, with complete visible positive twins.
Their transport is explicitly `fixture-visible-chat`, not actual ChatGPT.
