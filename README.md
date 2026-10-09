# Flexible Pipes

Deterministic programs with language-model stages that are explicit, inspectable, and replayable.

This is a small pipeline substrate, not a general agent framework. Ordinary deterministic stages and model-backed stages can be composed without pretending that model inference is deterministic.

[Human-visible job delivery](docs/job-delivery.md) extends stage artifacts with separate observed delivery and dispatch. A composed job without its required visible surface blocks later pipeline effects. Text and binary attachments share the handoff identity; first-class attachments preserve their declared bytes, filename, MIME type, provenance, and digest.

## Common task: transfer a GitHub repository

See [the Grease-first repository-transfer task](docs/how-to-move-the-users-github-repository-to-a-different-organization.md).

It calls Kitchen to generate one complete standalone program, runs it under Grease, verifies the repository ID, and renders a checked answer.

## Bootstrap model set

- `openai/gpt-oss-120b` — general reasoning and instruction work
- `Qwen/Qwen3-Coder-480B-A35B-Instruct` — code-focused work
- `EleutherAI/pythia-12b-deduped` — large Pythia research/control model
- `EleutherAI/pythia-6.9b-deduped` — second Pythia point for comparison

Pythia’s checkpoint series provides a controlled family for studying where pipeline behavior comes from and how model-dependent a flexible stage is.

## Repository boundary

Git owns:

- model identities and requested revisions
- resolved immutable revisions
- pipeline specifications
- prompts and deterministic stage code
- generation parameters and seeds where supported
- input/output hashes, stdout/stderr, exit status, and run receipts

Git does **not** own model weights. Weights live in a cache outside the repository.

A replayable model run distinguishes:

1. deterministic orchestration
2. fixed model identity and revision
3. fixed generation settings
4. the actual model output used downstream

This allows exact replay of the recorded output even when fresh inference is not bit-for-bit reproducible.

## Initial layout

```text
models/catalog.toml       model identities and roles
scripts/fetch-model       resolve a revision and download weights outside Git
docs/pipeline-contract.md execution and receipt contract
.gitignore                model caches and run scratch
```

## Model bootstrap

The fetcher needs Python 3.11+, Git, and the Hugging Face `hf` CLI for downloads.

```sh
python3 scripts/fetch-model --list
python3 scripts/fetch-model gpt-oss-120b --resolve-only
python3 scripts/fetch-model pythia-12b
```

Each fetch resolves the catalog revision to a full Hugging Face commit SHA. Weights default to `~/.cache/flexible-pipes/models`. Local receipts go under `.flexible-pipes/model-receipts`, which is ignored by Git.

The repository starts smaller than Kitchen: model boundaries and receipts first, scheduler and graph machinery later.
