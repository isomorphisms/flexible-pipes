# Compact interpreter source handoff

This record separates three jobs that should not be collapsed:

1. **Kitchen** owns tested script semantics and source pins.
2. **Flexible Pipes** owns reusable deterministic renderers/pipelines and exact run receipts.
3. **Cat Food** owns build/deployment facts and Android runtime delivery.

The current machine-readable lock is `registry/compact-interpreters.json`.

## Generic GitHub fork script

The reusable pipeline is `github-fork-script`. It takes three parameters:

- `source_owner`
- `repository`
- `destination_org`

The repository name is preserved by construction. The renderer deliberately omits
`--fork-name`, and `--clone=false` prevents a local clone.

Example request:

```text
Run flexible-pipes pipeline github-fork-script with source_owner=micropython, repository=micropython, destination_org=dilapidated-shed.
```

MicroPython is only one invocation of this generic operation.

The authoritative output is the stage's literal plain-text command block. It contains
no `sh` invocation and is not an attachment. The pipeline records exact parameters and
the stdout digest.

## Interpreter intent

- MicroPython is the compact Python candidate.
- Field Mouse is the active small JavaScript runtime line.
- MuJS is the compact C JavaScript reference/fallback for footprint comparisons.
- Cat Food should package runtime artifacts for MIRO A1 and MIRO C67 rather than cloning
  these source trees onto phones. A1 remains the primary constrained target.

MicroPython's own large hardware-specific submodule graph should not be initialized
recursively unless the selected build needs it.
