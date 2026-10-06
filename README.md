# flexible-pipes

Deterministic programs with language-model stages that are explicit, inspectable, and replayable.

[Human-visible job delivery](docs/job-delivery.md) extends stage artifacts with
separate observed delivery and dispatch. A composed job without the required
visible surface blocks later pipeline effects.
Text and binary attachments share that handoff identity. Archive members are
materialized deterministically and a first-class attachment must preserve the
declared bytes, filename, MIME type, provenance and digest.

The first target is not a general agent framework. It is a small pipeline substrate where ordinary deterministic stages and model-backed stages can be composed without pretending that model inference itself is deterministic.

## Bootstrap model set

Large models first:

- `openai/gpt-oss-120b` — general reasoning / instruction worker.
- `Qwen/Qwen3-Coder-480B-A35B-Instruct` — code-focused worker.
- `EleutherAI/pythia-12b-deduped` — largest Pythia research/control model.
- `EleutherAI/pythia-6.9b-deduped` — second large Pythia point for comparisons.

Pythia matters here for more than raw capability: its checkpoint series gives us a controlled family for studying where pipeline behavior comes from and how model-dependent a “flexible” stage really is.

## Repository boundary

Git owns:

- model identities and requested revisions;
- resolved immutable revisions;
- pipeline specifications;
- prompts and deterministic stage code;
- generation parameters and seeds where supported;
- input/output hashes, stdout/stderr, exit status, and run receipts.

Git does **not** own model weights. Weights live in a cache outside the repository.

A model run is never silently treated as deterministic. A replayable run records enough information to distinguish:

1. deterministic orchestration;
2. fixed model identity and revision;
3. fixed generation settings;
4. the actual model output used by later deterministic stages.

That lets a later pipeline replay the recorded output exactly even when fresh inference is not bit-for-bit reproducible.

## Initial layout

```
models/catalog.toml       model identities and roles
scripts/fetch-model       resolve a revision and download weights outside Git
docs/pipeline-contract.md first execution/receipt contract
.gitignore                excludes model caches and run scratch
```

## Model bootstrap

The fetcher needs Python 3.11+, Git, and the Hugging Face `hf` CLI for actual downloads.

```sh
python3 scripts/fetch-model --list
python3 scripts/fetch-model gpt-oss-120b --resolve-only
python3 scripts/fetch-model pythia-12b
```

Every fetch first resolves the catalog revision to a full Hugging Face commit SHA. Actual weights default to `~/.cache/flexible-pipes/models`; local resolution/download receipts go under `.flexible-pipes/model-receipts`, which is ignored by Git.

This repository is intentionally starting smaller than `kitchen`: model boundaries and receipts first, scheduler/graph machinery later.
