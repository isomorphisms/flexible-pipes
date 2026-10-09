# Test GPT-OSS understanding of the user's GitHub repository commands

## What this tests

`evals/github-repository-transfer/suite.json` contains 24 cases, three initial-prompt conditions and three seeds: **216 trials per model**. Cases include the user's short commands, preceding-URL context, “GH script,” script-only versus execution, missing names, spelling/case variations, destination/source corrections, cancellation, fork/rename/local-directory controls, pending/completed transfers and false-completion pressure.

The three initial prompts provide (1) the task title, (2) an explicit Kitchen task card, and (3) that task card alongside distracting fork documentation. Paired cases distinguish changed context from paraphrase. All conditions use the same six-field response contract and independent expected answers. The grader reports both format failure and individual field outcomes; an aggregate pass requires every declared trial.

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

## Evidence from this turn

See `evals/github-repository-transfer/evidence/2026-10-09-harness.json` and hosted run `37926591487`. Exact AICI source blobs and Ithon's real checked frontend were used, not a shell shim or a replacement interpreter. The same complete test passed in a local replay of the downloaded source/evidence.

The synthetic positive control accepted 216/216 responses. A constant first-answer policy accepted only 36/216 and correctly failed the suite. Stale request bindings, synthetic responses claiming live provenance, and missing responses also correctly failed. One positive and ten targeted parser/oracle controls passed. All three model request profiles were prepared.

**Actual model responses: zero. GPT-OSS inference: BLOCKED_NO_ENDPOINT. Pythia inference: NOT_RUN. Grease/Kitchen execution and live transfer: NOT_RUN.** No GPT-OSS accuracy claim follows from these harness results. Public development/evaluation labels are not a secret holdout.

## Next-turn boundary

The missing input for actual GPT-OSS results is a reachable, explicitly chosen inference endpoint. Keep the current suite/prompts/oracles frozen for the first run, retain every raw response and request hash, then compare per-case/per-prompt outcomes rather than rewriting prompts until only a favorable result remains. A separate actual-Grease simulated-GitHub test must qualify the generated-program path before combining model routing with execution acceptance.

The earlier transfer-plan audit, including error swallowing, separated identity reads, unpinned host/source assumptions and nonexclusive output writes, is in AICI's `model-evaluation/README.md`. Those operational defects are identified here, not silently declared repaired by a language-model test.
