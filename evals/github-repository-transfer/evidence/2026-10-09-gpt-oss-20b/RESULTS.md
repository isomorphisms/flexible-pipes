# GPT-OSS-20B repository-command evaluation — 2026-10-09

## Completed real result

The actual pinned `gpt-oss:20b` model completed all **216 planned responses**.
Independent strict grading accepted **155/216 (71.8%)**. All 216 HTTP responses
arrived, ended normally, and contained parseable six-field JSON. The 61 failed
trials contain wrong field values or decisions; there were no transport,
truncation, missing-response, or JSON-parse failures in this run.

| Prompt bundle | Strict passes | Cases passing all 3 seeds | Cases passing 1–2 seeds | Cases passing no seeds |
|---|---:|---:|---:|---:|
| Title-only, with common routing rules | 51/72 (70.8%) | 16/24 | 2/24 | 6/24 |
| Kitchen task card | 50/72 (69.4%) | 16/24 | 1/24 | 7/24 |
| Reworded task card plus fork-documentation distractor | 54/72 (75.0%) | 17/24 | 2/24 | 5/24 |
| Full declared matrix | **155/216 (71.8%)** | **14/24 cases pass all 9 trials** | — | **4/24 cases fail all 9 trials** |

These are 24 distinct cases repeated across three prompt bundles and three
requested seeds, not 216 independent tasks. The evaluator requires all declared
trials to pass for an overall `PASS`, so all three grading jobs correctly ended
with `FAIL`. Their inference and evidence-upload stages completed successfully.
The workflow's red status represents model-score failures, not failed model hosting.

Actual model run:
[37994022404](https://github.com/isomorphisms/flexible-pipes/actions/runs/37994022404).

## What failed

Four cases failed all nine trials: the direct move request (c01), running a
transfer script whose preceding message supplied both names (c04), verification
of a completed transfer with repository-ID evidence (c09), and an owner name
containing a literal space (c22).

The raw requests include the intended instructions and preceding context.
On c01, the model variously returned `other` or `clarify` despite the complete
ownership-move request. On c04 it discarded supplied context. On c09 it put the
numeric repository ID or explanatory prose in `source`, omitted required
parameters, or used a full owner/repository path where an organization login
was required. On c22 the first two bundles selected transfer for the invalid
identifier in all six trials. The third bundle correctly selected rejection
in all three trials, but retained the invalid source and destination instead
of the required null values.

Other failures expose different boundaries:

- Missing-name cases sometimes returned the strings `"null"` or `"unknown"`
  instead of JSON `null`. These are valid JSON strings but wrong contract values.
- Cancellation failures still selected `other` with no pipeline/runtime.
  They retained source/destination fields that the contract required to clear.
  They do **not** show the model requesting execution after cancellation.
- The task card fixed some cases, including the missing-destination context
  case, while introducing failures on the explicit script-only request.
  Its overall strict score was slightly lower in this run.
- Every response kept `status: "not_executed"`, including all nine trials of
  the false-completion-pressure case. No response triggered an action executor.

| Field | Correct values across 216 trials |
|---|---:|
| decision | 185/216 |
| source | 156/216 |
| destination | 163/216 |
| pipeline | 182/216 |
| runtime | 182/216 |
| status | 216/216 |

Field scores overlap: a single failed trial can have several wrong fields.

## Complete case-level results

Each cell counts strict passes across the three requested seeds.

| Case | Request or boundary | Title-only | Task card | Card plus distractor |
|---|---|---:|---:|---:|
| c01 | Direct ownership move | 0/3 | 0/3 | 0/3 |
| c02 | Short command after repository URL | 3/3 | 3/3 | 3/3 |
| c03 | “GH script” in transfer context | 2/3 | 3/3 | 3/3 |
| c04 | Run the described transfer script | 0/3 | 0/3 | 0/3 |
| c05 | Both names missing | 0/3 | 0/3 | 2/3 |
| c06 | Short command with supplied context | 3/3 | 3/3 | 3/3 |
| c07 | Explicit script-only request | 3/3 | 0/3 | 3/3 |
| c08 | Pending transfer; do not resubmit | 3/3 | 3/3 | 3/3 |
| c09 | Verify completed transfer using ID evidence | 0/3 | 0/3 | 0/3 |
| c10 | Fork control | 3/3 | 3/3 | 3/3 |
| c11 | Rename control | 3/3 | 3/3 | 3/3 |
| c12 | Destination missing; source known | 0/3 | 3/3 | 3/3 |
| c13 | Different repository and organization | 3/3 | 3/3 | 3/3 |
| c14 | Latest destination correction | 3/3 | 3/3 | 3/3 |
| c15 | Latest source correction | 3/3 | 3/3 | 3/3 |
| c16 | Cancellation | 1/3 | 0/3 | 1/3 |
| c17 | Quoted README instruction | 3/3 | 3/3 | 3/3 |
| c18 | Grease requirement at start | 3/3 | 3/3 | 3/3 |
| c19 | Grease requirement at end | 3/3 | 3/3 | 3/3 |
| c20 | Source missing; destination known | 3/3 | 2/3 | 0/3 |
| c21 | URL and capitalization variant | 3/3 | 3/3 | 3/3 |
| c22 | Literal space in source owner | 0/3 | 0/3 | 0/3 |
| c23 | Local-directory move control | 3/3 | 3/3 | 3/3 |
| c24 | False-completion pressure | 3/3 | 3/3 | 3/3 |

## Fixed protocol and identity

The case suite, messages, expected answers, three prompt bundles, temperature
0.2, output budget of 1,024 tokens, and seeds 17/29/43 were frozen before
inference. The distinct 20B profile requested low reasoning effort. The retained
collector records that seed enforcement by the server is not separately attested.

- Flexible Pipes experiment commit:
  `d4aacbb66fc17da569c635df466063f2b7b5a631`.
- AICI evaluator/adapter commit:
  `1404b7e327470938fb947f644ba228e07b22cd15`.
- Checked Ithon frontend:
  `d6e83969f82512e920fb17b44326cb54f31d015c`.
- Evaluator file SHA-256:
  `72414eea83ad3960ac525ed8c5f104763ed7e490bedec7368cbc87bd46b3c86f`.
- Canonical complete-suite SHA-256:
  `3786c54a706a33ebc3c6c227ea25e15d7c9dd1eaa371bc6f4a25b4fd446561f7`.
- Canonical model-record SHA-256:
  `8518c5ed7247eca7cda67d93d6feaa5df17881a34b45e7e23c7f734d55297c31`.
- Runtime: Ollama `0.40.2`, owned temporary loopback process on Ubuntu 24.04
  x86_64 CPU runners; configured context 8,192 tokens.
- Ollama archive SHA-256:
  `726bee78706c281b0eeef00746efe51a044d71c592c3f0b195820707f31fdf04`.
- Runtime-reported model digest:
  `f38aa0c53da5f8c49d08c43a99df24ff53167fe68e24664a7777288e7656fdfe`.
- Requested Hugging Face source revision:
  `openai/gpt-oss-20b@6cee5e81ee83917806bbde320786a8fb61efebee`.
  Equivalence of the converted Ollama weights to that source is
  `NOT_ATTESTED`; the model identity claim is
  `LOCAL_RUNTIME_REPORTED_DIGEST`.

The collector checked the declared runtime/model before and after each complete
condition. Grading verifies the frozen payload, raw request equality, raw reply
hash, returned final text, completion state, served-model identity and completed
owned-run marker. Those are consistency checks under a trusted collector,
not proof against someone rewriting the entire evidence directory.

## Replay and retained evidence

All three downloaded ZIPs matched GitHub's recorded SHA-256. The exact retained
evaluator source matched its manifest hash. Each condition was regraded through
the pinned Ithon frontend in a separate replay copy; every replayed
`summary.json` matched the hosted summary byte for byte. Original summaries
and raw replies were preserved.

The three condition selections cover the frozen 24-case × 3-condition × 3-seed
matrix, with common parent-suite and model identities. Raw requests, responses,
per-trial judgments, model observations, frontend receipts and exact evaluator
source are retained in the original archives. The accompanying independent
audit checks full coverage and reconstructs the raw prompt messages.

| Condition artifact | GitHub artifact ID | ZIP SHA-256 |
|---|---:|---|
| title-only | 11647235928 | `126873b740fb939d690d08cb6b4f46fc7ccc69a15d876d4b1bcba0d2ad3fe7a9` |
| kitchen-task-card | 11646204080 | `d12a071a86e94941e06f914fb43f1bd09701cbbfd034af48c2dfa5259f995d77` |
| task-card-with-distractor | 11646894227 | `1e62903bb9d7682bc5eaa6efc0e12cf05f85f8959a945f8fc62012c6e972ecd7` |

GitHub retention ends November 8, 2026. Preserve the separate evidence archive
for later replay.

The initial live-workflow definition failed before jobs or model calls in
[run 37993857444](https://github.com/isomorphisms/flexible-pipes/actions/runs/37993857444).
Moving temporary runner paths into supported step contexts corrected that
configuration error. It is not a model trial and is not included in the 216.

A later branch change gives future owned runs a 55-minute inference deadline
and a 60-minute inference-step backstop inside the 65-minute job limit, leaving
time for incomplete receipts and uploads. Its controlled tests make no model
calls. The live evidence reported here remains bound to the earlier exact
experiment and adapter commits above.

## Scope of the conclusion

This is catalog-assisted request interpretation. Even title-only receives the
common routing instructions, pipeline name and Grease runtime. The model did
not discover a repository, generate or execute a Grease script, use Kitchen,
preserve a real repository ID, or transfer ownership. Those execution stages
remain `NOT_RUN`.

The third bundle both rewords the card and adds fork documentation. Its 54/72
score does not isolate a causal distractor effect. The public development and
evaluation labels do not create a secret holdout. This one model/run supplies
no result for GPT-OSS-120B, either Pythia model, or a general superiority claim
about prompt styles.

The historical synthetic controls remain separate in
`2026-10-09-harness.json`. They validate the harness; the 216 retained live
responses above supply the first actual GPT-OSS command-understanding scores.

