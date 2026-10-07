# Compact interpreter source handoff

This record separates three jobs that should not be collapsed:

1. **Kitchen** prepares and tests human-facing scripts and pins exact interpreter source.
2. **Flexible Pipes** records the exact producer/source identities used by repeatable work.
3. **Cat Food** owns build/deployment facts and Android runtime delivery.

The current machine-readable lock is `registry/compact-interpreters.json`.

## Why there is no fork pipeline yet

Flexible Pipes can run checked-in named pipelines, but its current delivery contract does
not improve on Kitchen for producing a small standalone terminal script for a human to
execute. Copying the same fork script into this repository would create two script owners.

Therefore the fork operation remains a Kitchen artifact. Flexible Pipes records the exact
Kitchen commit and blob identities so later automation can materialize or invoke that
specific checked helper rather than reconstructing it from chat.

A future pipeline may consume the registry after two conditions are true:

- `dilapidated-shed/micropython` exists and contains the pinned MicroPython commit;
- the pipeline has a reviewed cross-repository materialization stage with a receipt binding
  the Kitchen helper bytes and source gitlinks.

Until then, do not describe a Flexible Pipes fork/build as executed merely because the
registry exists.

## Interpreter intent

- MicroPython is the compact Python candidate.
- Field Mouse is the active small JavaScript runtime line.
- MuJS is the compact C JavaScript reference/fallback for footprint comparisons.
- Cat Food should package runtime artifacts for MIRO A1 and MIRO C67 rather than cloning
  these source trees onto phones. A1 remains the primary constrained target.

MicroPython's own large hardware-specific submodule graph should not be initialized
recursively unless the selected build needs it.
