# Compact interpreter source handoff

This record separates three jobs that should not be collapsed:

1. **Kitchen** owns tested script semantics and source pins.
2. **Flexible Pipes** deterministically renders the exact human-visible script text and records its digest.
3. **Cat Food** owns build/deployment facts and Android runtime delivery.

The current machine-readable lock is `registry/compact-interpreters.json`.

## Human-visible MicroPython fork script

`pipelines/micropython-fork-script.json` runs a deterministic Python renderer. Its
authoritative output is the literal multi-line paste block in stage stdout. The stage is
`display-only`: the human-visible text must be byte-identical to that stdout artifact.

The rendered block deliberately contains no `sh` invocation and is not an attached file.
It uses GitHub CLI/API commands directly in the user's existing shell.

Canonical request form:

```text
Run flexible-pipes pipeline micropython-fork-script.
```

A controller may only call the script delivered when the exact stage output has been
presented visibly. Repository-side composition does not itself prove ChatGPT delivery.

## Interpreter intent

- MicroPython is the compact Python candidate.
- Field Mouse is the active small JavaScript runtime line.
- MuJS is the compact C JavaScript reference/fallback for footprint comparisons.
- Cat Food should package runtime artifacts for MIRO A1 and MIRO C67 rather than cloning
  these source trees onto phones. A1 remains the primary constrained target.

MicroPython's own large hardware-specific submodule graph should not be initialized
recursively unless the selected build needs it.
