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

The maintained runner prepares the exact assignment as ordinary text, without
adding a CodeBlock. `deliver(..., summary="")` sends those same bytes. This
avoids the added component that the Android client rejected on October 9; it
does not attest how a client rendered the payload itself. The ordinary-text
form still excludes HTML markup under the independent gate.

A summary does not change the default ordinary-text presentation. The explicit
`presentation="literal"` option selects the existing top-level literal block,
with a delimiter longer than any delimiter in the assignment. Use that form
only when the controller knows the client supports CodeBlocks. `render` remains
the literal-block helper. ai-ci checks the complete observed response against
the stage artifact. Nested/quoted blocks, hidden HTML,
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
is not repeated. Recovery resets `delivery_status` to
`AWAITING_HANDOFF_DELIVERY`; a previous PASS cannot survive the reported failure.
When the client reports an unavailable CodeBlock, recover the same stage and
redeliver with an empty summary to send the original ordinary-text bytes.
An observed unavailable-component placeholder fails before dispatch.
“Where’s the text?” without recovered context is rejected by
ai-ci. The original request is retained rather than overwritten by the
correction.

## Adoption and evidence boundary

The exploratory `scripts/run-pipeline-legacy.py` prevalidates handoff metadata through
checked Ithon (`--ithon /verified/entrypoint`) before any command effects. When
the producing stage completes it saves the extended stage and complete
response artifact and returns nonzero `AWAITING_HANDOFF_DELIVERY`. Later stages
cannot execute. Neither that response file nor stdout is a visible receipt.
The trusted transport controller completes the same stage using `deliver`.
There is currently no deployed ChatGPT visible-sink adapter in this repository.
The attachment contract makes that adapter implementable and independently
checkable, but no platform delivery is inferred from local fixtures. The retained registered
Kitchen/Android runtime work is separate; this change does not activate it or
resolve its existing deployment blockers. Its controllers can consume the
same captured-stage extension when they gain model-job operations.

The generic runner receipt carries `qualified_operation: false`. Captured
delivery checks prove the declared handoff bytes and lifecycle; they do not
promote a caller-supplied pipeline into a registered operation.

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
The runtime suite also reproduces an unavailable-CodeBlock sink, rejection
before dispatch, recovery through complete ordinary text with the same artifact
identity, and removal of stale PASS on recovery. These are transport regression
tests; actual Android rendering and trusted platform acknowledgements remain
unverified by this suite. Issue #35 remains open for that adoption boundary.


## Admission, readback and restart qualification

`deliver_controlled` consumes the existing stage plus a supervisor-owned expected
specification and required literal corrections. It compares that admission
before any presentation effect. An internally consistent worker rewrite of the
request, model or audience no longer agrees with the independent admission.

The controller separately asks a reader for the accepted message/file bytes.
AI-CI's `check_actual` checks those bytes and service metadata; its archive
reference path uses its own extraction instead of FP's materializer. Merely
declaring a correct digest or file ID cannot replace the byte input.

COMPOSED, PRESENTED, ACCEPTED and DISPATCHED are checkpoints on the same stage.
A completed presentation is read back on restart instead of resent. Before
dispatch the controller creates a durable exclusive attempt journal. If execution
stops after the remote effect, restart uses `lookup(handoff_id)`; an unknown
outcome blocks resubmission. Accepted dispatch is never repeated during display
recovery. These are bounded fixture-controller results, not a deployed isolation
or platform-security boundary.

Only fixture controller execution is currently implemented. Calling that
controller with a platform profile fails before effects with
`HANDOFF_PLATFORM_ADAPTER_UNAVAILABLE`. It returns `FIXTURE_PASS` and
`platform_delivery_status=NOT_VERIFIED`. The lower-level `deliver` result is
explicitly labeled `transport-contract-only`. Caller-controlled labels, keys,
captures and signatures cannot activate a platform verifier.

`compose-workflow` is the checked-Ithon composition interface:
`compose-handoff.pi compose-workflow STAGE SPEC SELECTED RUN ARTIFACT SOURCE`.
RUN and ARTIFACT are connector observations; SELECTED binds the selected
repository ID, run, observed attempt, commit, artifact ID/name, archive digest,
member, filename, MIME and payload digest. The composer checks their relations,
successful/nonexpired state and bytes, and emits `STAGE.attachment` containing
the exact selected member. It does not acquire credentials or attest arbitrary
caller-created metadata. GitHub artifact metadata does not expose its run
attempt; that limitation is retained as
`artifact_attempt_binding=NOT_PROVIDED_BY_ARTIFACT_METADATA`, rather than
inventing an artifact-to-attempt attestation.

The maintained `fp35-delivery-acceptance` pipeline captures the implementation
envelope, FP runtime/effect tests and independent AI-CI cases as separate stage
artifacts. Required inputs name verified absolute source/runtime locations.
Tests preserve the ordinary-text positive control, all three delivery modes,
placeholder recovery, unique member selection and negative provenance/readback
cases. This qualification does not claim a ChatGPT attachment adapter, actual
Android presentation, execution on the MIRO C67/A1, or full issue closure.

## Interrupted presentation and live storage

Before a new message/upload, the controlled fixture profile writes an exclusive,
fsynced presentation attempt journal. The key is the existing handoff identity
plus the number of recorded delivery failures. A recorded recovery starts the
next presentation generation; an ordinary retry must reconcile the previous
generation. Optional send_text_once/send_attachment_once receive that key.
On restart, lookup_text/lookup_attachment must return an ACCEPTED observation;
a missing lookup, unknown outcome or different journal identity blocks resend.
This covers interruption after sink acceptance and before readback. The returned
observation still undergoes exact byte/metadata and independent AI-CI checks.
A saved visible state reads only the latest observation after the last failure.
These journals qualify process interruption, not crash-proof storage hardware.

The fp35-live-artifact pipeline captures the complete authoritative SUN packet
and the pinned original Wegert archive in existing stage artifacts. It selects
only app-debug.apk, preserves its bytes/name/MIME and stops at
AWAITING_HANDOFF_DELIVERY. The compose-workflow CLI additionally checks the
actual repository/run/commit/artifact observations. AI-CI's stored CLI inspects
the independently retrieved file without inventing a visible event.

The live source was artifact 11528177870 from run 37727204424, commit
71e6f969b102d70a06ebb2d98b6426f79f287173 in isomorphismes/wegert. Its archive
SHA-256 is 7a69447a00e3a674d12aeaa41c3e4895e30f53e6a8c8373775df5e3e19c6478c;
the exact 1558364-byte APK is
a6897b357365b2e59ee653f3e39736ec328aa34eafa532da7e32d444e6e9ed67.
The exposed file interfaces support this source-to-storage path. An initial
name collision and absent MIME failed acceptance. Recovery kept the same
storage identity, moved it to a dedicated directory, restored the basename,
and replaced its backing version through the prepared upload interface.
Independent retrieval then preserved the exact filename, APK MIME and bytes.
Private service identifiers remain outside public receipts.

This is live storage qualification and a prepared named attachment, not a
deployed production controller or proof of client display. The original Young
Tableaux artifact download returned KeyError for id; its accessibility/expiry
was not established. Wegert is a separately identified incident specimen,
not a silent replacement for those missing Young Tableaux bytes.

