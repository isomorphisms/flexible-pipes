# FC-CONTROL-01 — source audit and blocked handoff

Status: **PARTIAL / BLOCKED**. The original assignment is preserved in
`assignment.txt`. This is a read-only source audit and an executed FP handoff
registration. No model conversation, native controller implementation,
trusted visible delivery, model-job dispatch or independent product acceptance
has been completed by this change.

## Decision and evidence

The controller needs two distinct paths: durable model conversation and
FP-owned work. Preserve the existing `ModelRequest → Transport → ModelEvent`
boundary; the UI sends typed user actions. A model's tool event remains data
until the existing FP authority admits its corresponding effect.

The current reading/provider candidate at
`410ce85df1eebc06c01768bbc0084ce6292c65c2` does **not** send conversation history.
`transport_boundary_send` calls `provider_request_body_for` with only
`conversation->prompt` and `prompt_length`.
The Chat Completions builder emits one user message; Responses emits a single
string input. History selection/replay does not make either request multi-turn.

`history_turn` can retrieve a request and its final attempt projection from
the durable journal, and `read_history_window` reads bounded response windows.
That projection is insufficient as an exhaustive context iterator: it does not
expose prior attempts or tool payload records. Before provider context can be
called complete, define a journal snapshot/cursor that preserves their distinct
identities and terminal outcomes. Do not treat cancelled, failed or uncertain
response bytes as a successful assistant answer.

The existing provider parser retains tool events through `store_tool_event`;
no model-produced shell command should become an execution route. Keep
provider-specific tool framing separate from an explicitly authorized typed
FP proposal. Preserve the full job artifact, source digest and FP identity
rather than classify a summary as the authoritative work.

The request builder and native transport both impose body limits. A context
limit must be checked after JSON escaping and before network submission;
oversized history needs an explicit refusal/selection result with zero POSTs,
not silent truncation. A local serialization refusal must not be presented as
uncertain remote delivery. The current Android send failure path maps any
`transport_boundary_send` error to `TRANSPORT_LOSS`, so that distinction needs
a focused controller change.

The profile already separates origin, CA, model, path and optional request
format from the compiled application, with authorization in a private file.
Keep Chat Completions and Responses as explicit schemas. A caller-supplied
GPT-OSS endpoint can use the compatible schema it actually implements; model
name alone does not qualify protocol, tool support, authentication or deployment.

The user's current target is one GPT-OSS on **SDF.org**, with repository and
automated-work interception. Its actual host, model service, endpoint,
credentials and execution capabilities remain **UNVERIFIED**. Do not substitute
Hetzner, presume a GPU/service exists, or install a model in the SDF account
without verified capability and appropriate scope.

## First concrete blocker

The mandatory path in [the registered assignment](https://github.com/isomorphisms/flexible-pipes/issues/223)
requires an actual captured visible handoff before implementation. At FP main
`181c6011956a39454fd8b018380c2ea54f0ab8e7`, `scripts/run-pipeline` composes the
stage artifact and deliberately exits nonzero with
`AWAITING_HANDOFF_DELIVERY`. `docs/job-delivery.md` explicitly records the
absence of a deployed ChatGPT visible-sink adapter. This session exposes no
trusted controller operation returning actual accepted bytes, message/surface
identity and FP dispatch acknowledgement. A local file, issue, chat claim,
green leaf test or this draft registration cannot supply that receipt.

This is an unavailable execution boundary, not a request for the user to grant
the same implementation authorization again. The display-only metadata is the
existing conservative handoff default; it does not revoke the user's invocation
of FC-CONTROL-01 or pretend that the whole task was only a request for a draft.

The named `fc-control-01-handoff` pipeline actually ran twice on exact source
`c135d6c3c2594d50eb5bbd7a0ed3746ad053b3c2`. All seven read-only command stages
exited 0. Both controller runs exited 1 at the expected handoff gate. Neither is
reported as a successful end-to-end pipeline. Original receipts and output bytes
are retained under `receipts/fc-control-01/`.

Payload: 6,914 bytes; SHA-256
`c97ce4c2f2b459134c41d803cf0c7fc0005e9850b90d5464810c25a3a1084c8f`.
Handoff identity:
`79b7e4d84593bdf50e4c08fb2ecaf8258a5fe8c6d3f96cec7c923195757bcf18`.
Both runs preserve `visible_state=PENDING` and no accepted dispatch.

## Acceptance boundaries

| Boundary | Result |
| --- | --- |
| Immutable source inspection and full assignment capture | Executed |
| Existing handoff composition, two independent runs | Executed; same identity |
| Overall registered pipeline | AWAITING_HANDOFF_DELIVERY, exit 1 |
| Trusted actual visible delivery | PENDING |
| Implementation through Kitchen / pinned Ike | NOT_RUN |
| Independent ai-ci product acceptance | NOT_RUN |
| Local TLS two-turn conversation | NOT_RUN |
| Real provider / SDF model service | NOT_RUN |
| Production watcher, responder or model-job dispatch | NOT_RUN |
| APK build, physical A1/C67 interaction | NOT_RUN |

Separate predecessor evidence was refreshed: at FastChat
`7d70c331862e36cdf26981aa8c2558a5d0758eb4`, A1/H2/Idriç checks succeed and
the Icky C workflow fails. This change neither repairs that producer nor calls
the predecessor green. The original source pins and assertions remain intact.

## Recommended allocation

- Sun: the present source diagnosis is established; the overall job remains
  incomplete at the mandatory handoff boundary.
- Earth: after a qualified handoff, implement the bounded durable two-turn
  context path, including local refusal versus uncertain-delivery distinction,
  through a registered Kitchen/Ike procedure and independent ai-ci TLS oracle.
- Earth: a separate FP client/visible-sink change must use the existing captured
  stage and delivery APIs; qualify a single authorized watcher fixture with
  restart deduplication. Do not build another scheduler or infer production
  dispatch from fixture acknowledgements.
- Moon: none until an exact Earth source and independent result are green.
  Later propagation may update fixtures, receipts and device packages without
  changing controller semantics.

No merge, release, deployment, model installation, account access or device
action was performed. FC-UI-01 remains separate.

## Initial publication attempt

Automatic approval review rejected the attempted push of local source commit
`c135d6c3c2594d50eb5bbd7a0ed3746ad053b3c2` to
`isomorphisms/flexible-pipes:work/fc-control-01-handoff`. It stated that the
short task invocation did not authorize repository publication. No alternate
publication route was attempted. The registration, audit and original receipts
are retained locally for explicit review and approval. No draft PR was created.

The user explicitly authorized publication on 18 October 2026. Publish this
prepared branch as a draft PR. That authorization resolves the initial
publication refusal; it does not supply trusted visible delivery or dispatch
evidence for the controller implementation.

The terminal Git transport lacked credentials and `gh` was unavailable.
Connected GitHub publication recreated the source commit with the identical
tree `33c9bcf4773c766d9ab7dc8d48a62e310d705b4f`. The original executed commit
object is retained verbatim in `source-commit.txt`; `publication.tsv` maps its
local revision to the published source revision. The historical receipts
retain their original source identity. The prepared final file tree was also
verified identical before adding this publication provenance.

Earth follow-up job
NONE at this boundary. A new implementation assignment cannot assert the
missing trusted delivery/dispatch evidence. Resume the already authorized
FC-CONTROL-01 assignment once its required controller path is available, or
after an explicit change to that requirement.

Moon follow-up job(s)
NONE. No implemented controller or accepted source is available to propagate.
