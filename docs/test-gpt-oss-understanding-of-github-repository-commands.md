# Test GPT-OSS understanding of the user's GitHub repository commands

## What this tests

`evals/github-repository-transfer/suite.json` contains 24 cases, three initial-prompt conditions and three seeds: **216 trials per model**. Cases include the user's short commands, preceding-URL context, “GH script,” script-only versus execution, missing names, spelling/case variations, destination/source corrections, cancellation, fork/rename/local-directory controls, pending/completed transfers and false-completion pressure.

The three initial prompts provide (1) the task title, (2) an explicit Kitchen task card, and (3) a differently worded task card alongside distracting fork documentation. These are three prompt bundles: the third also changes task-card wording, so its comparison with the second does not isolate a distractor effect. Even the title-only condition receives the substantial common routing instructions. Paired cases distinguish changed context from paraphrase. All conditions use the same six-field response contract and independent expected answers. The grader reports both format failure and individual field outcomes; an aggregate pass requires every declared trial.

This is **catalog-assisted request interpretation**, not a claim of autonomous repository discovery or end-to-end action execution. The model never receives the expected answers and never receives a GitHub action executor. Do not describe a correct route as proof that the original Grease transfer program works.

## Models and source copies

Reuse `models/catalog.toml`: GPT-OSS-120B, Pythia-12B-deduped and Pythia-6.9B-deduped were already registered. `registry/model-evaluation.json` connects those entries to AICI's reusable evaluator and inference adapters.

AICI now retains pinned git submodules for OpenAI's GPT-OSS reference source, Hugging Face Transformers and EleutherAI GPT-NeoX. Transformers and GPT-NeoX are the two Pythia implementation sources. Their native cross-implementation parity test is not implemented yet. The current local adapter uses Transformers; the HTTP adapter also supports a separately provisioned completion server. Model weights are not copied into either Git repository.

## Named entrypoints

`grease scripts/test-gpt-oss-understanding-of-github-repository-commands.ysh`

`grease scripts/compare-pythia-understanding-of-github-repository-commands.ysh`

The equivalent registered pipeline is `test-gpt-oss-understanding-of-github-repository-commands`. The existing generic pipeline controller retains legacy Python implementation debt; the new orchestration is Grease and new first-party evaluation/inference code is checked Ithon.

Supply verified absolute `FLEXIBLE_PIPES_ROOT`, `AICI_ROOT`, and `ITHON_ENTRYPOINT` paths. `MODEL_EVAL_OUTPUT` must name a new directory with an existing parent; use a fresh directory for every run. `MODEL_EVAL_MODEL` selects an existing catalog key and defaults to GPT-OSS-120B in the GPT-OSS entrypoint and Pythia-12B in the Pythia entrypoint.

For GPT-OSS, configure `MODEL_EVAL_BASE_URL`, optional `MODEL_EVAL_SERVED_MODEL`, and a dedicated `MODEL_EVAL_API_KEY` only when the inference server needs it. The HTTP server must implement GPT-OSS's Harmony chat format. No GitHub credential is needed. The matrix is bounded to 500 requests and this suite requests 216; inspect the frozen suite before enabling an externally billed endpoint. Remote model names do not attest weights.

For local Pythia, provision its foreign Transformers/PyTorch dependencies, an absolute `MODEL_EVAL_MODEL_CACHE` outside the repositories and explicit `MODEL_EVAL_ALLOW_DOWNLOAD=1`. Select `pythia-12b` or `pythia-6_9b`. The adapter resolves checkpoint/tokenizer revisions, refuses context truncation, and retains prompt/token IDs and token log probabilities. `PYTHIA_CAPTURE_PREFILL=1` additionally retains each layer's last-input-position activation vector. These traces support later controlled comparisons; they are not explanations of GPT-OSS internals.

## Historical harness evidence, before real inference

See `evals/github-repository-transfer/evidence/2026-10-09-harness.json` and hosted run `37926591487`. Exact AICI source blobs and Ithon's real checked frontend were used, not a shell shim or a replacement interpreter. The same complete test passed in a local replay of the downloaded source/evidence.

The synthetic positive control accepted 216/216 responses. A constant first-answer policy accepted only 36/216 and correctly failed the suite. Stale request bindings, a live label sent to the fixture grader, and missing responses also correctly failed. The original live-label test did not prove that the live grader rejected forged provenance; the follow-up below repairs that gap. One positive and ten targeted parser/oracle controls passed. All three original model request profiles were prepared.

**Actual model responses: zero. GPT-OSS inference: BLOCKED_NO_ENDPOINT. Pythia inference: NOT_RUN. Grease/Kitchen execution and live transfer: NOT_RUN.** No GPT-OSS accuracy claim follows from these harness results. Public development/evaluation labels are not a secret holdout.

## Bounded local GPT-OSS-20B follow-up

`github-repository-command-live.yml` now supplies the same ephemeral Ubuntu/Ollama route that actually ran the historical code comparison in [fuego-ironworks/gym run 37960256328](https://github.com/fuego-ironworks/gym/actions/runs/37960256328). It is an explicitly triggered experiment on this branch, not a schedule or a persistent model endpoint. The runtime archive is pinned to Ollama 0.40.2 and its retained SHA-256. The **distinct** `gpt-oss-20b` catalog profile pins the actual model digest from that run; no 20B response is relabeled as a 120B response. Its requested Hugging Face source is [revision 6cee5e81ee83917806bbde320786a8fb61efebee](https://huggingface.co/openai/gpt-oss-20b/tree/6cee5e81ee83917806bbde320786a8fb61efebee). Equivalence of the converted Ollama weights to that source is not attested.

The suite, all messages, expected answers, temperature 0.2, 1,024-token response budget and seeds 17/29/43 remain unchanged. Low reasoning effort is explicit in the frozen 20B profile and every raw HTTP request. Three independent jobs each run one original prompt condition: 24 cases × 3 seeds = 72 calls per job, 216 across the complete matrix. Every shard retains the whole parent suite, parent digest, model profile, exact worker requests and raw replies. A full-matrix claim requires all three unique conditions with identical parent and model bindings. Repeated trials are not new independent cases.

The checked-Ithon adapter owns a temporary loopback Ollama process, downloads the declared weights into the runner's temporary cache, verifies the runtime and model digest before and after inference, then stops its own process. The workflow uses single-command runner steps around that existing adapter; it adds no parallel Bash implementation. A failed runtime or final identity check cannot produce a new verified live pass. Weights are excluded from the evidence artifact and from Git.

The repaired AICI grader independently checks raw request equality, raw response hashes, final text, completion state, model and run bindings, plus the local runtime completion marker. Relabeled synthetic replies, stale or edited raw data, and missing completion evidence are targeted rejecting controls. These are consistency checks under a trusted collector, not proof against an attacker controlling all retained files.

The first complete live evaluation accepted **155/216 responses (71.8%)**: 51/72 for title-only, 50/72 for the Kitchen task card, and 54/72 for the reworded card plus distractor. All 216 replies completed normally and parsed as six-field JSON. The failed trials contain incorrect decisions or field values. All three downloaded artifacts were verified and independently regraded; the replay summaries matched the hosted summaries byte for byte. See [the full dated results, per-case table, source identities and artifact hashes](../evals/github-repository-transfer/evidence/2026-10-09-gpt-oss-20b/RESULTS.md).

Future owned runs have a 55-minute adapter deadline and a 60-minute inference-step backstop within the 65-minute job limit. Timeout handling records incomplete work and leaves time to preserve partial evidence. The dated result record identifies the earlier exact source used by this completed run.

The experiment does not exercise Grease, generate a script, preserve a real repository ID, or transfer a repository. Those remain separate acceptance boundaries. The historical zero-response record above remains historical; GPT-OSS-120B and Pythia inference remain unrun.

The earlier transfer-plan audit, including error swallowing, separated identity reads, unpinned host/source assumptions and nonexclusive output writes, is in AICI's `model-evaluation/README.md`. Those operational defects are identified here, not silently declared repaired by a language-model test.
