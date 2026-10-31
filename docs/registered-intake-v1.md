# Reconciled registered intake interface

BC-FP01-S01 retains the live controller branch at
`442a33bfd36a23df3d757d17a31b8084cab21a38`, the exporter extension at
`3257e30042b8dc45e6b0a1000a2ae2b4ad72f2ca`, and main at
`d70159ff1dddefb163eb32fdd1c51335b9128fdc`. None is replaced with the older
closed pull-request snapshot. Newer main handoff, parameter, attachment,
runtime-selection and transfer behavior survives in the exploratory runner.

| Boundary | Fixed interface |
| --- | --- |
| Terminal | `run-pipeline.yml` manual input `request`, containing only data |
| Request branch | `pipeline-requests`, one regular `requests/*.json` blob relative to the admitted base |
| Event mapping | `event_adapter.envelope(event, environment, token)` |
| Authentication | `admission.verify_token(token, config, jwks)` then `verify_submission(decision, route, envelope)` |
| Supervisor | `registered-service.pi`, fixed `/v1/execute`, fixed installed engine |
| Source preflight | `registered-execution.verify_materials(config, diagnostic)`; no execution authority granted |
| Operation | `registered-execution.execute(config, raw, route, retry, diagnostic)` after deployment preflight |
| Client | `delivery.submit(endpoint, certificate, route, envelope, directory, accepted_release)` |
| Exploration | `run-pipeline-legacy.py`; always `qualified_operation=false` |

Both routes select the same fixed operation implementation, registry and
independent checks. The request envelope contains schema version 1, a bounded
request ID, a registered pipeline name and operation-specific inputs. Kitchen
takes source/destination owner, repository, expected login/repository ID and
qualified target context. Exporter takes only an exact source revision and
`scope=all`. No executable, checker, policy, environment or skip field is allowed.

Production admission binds signed event type, workflow/control revision and
run/attempt identity to the selected route. It does not authenticate a native
ChatGPT conversation or prove that a human saw the result. Request-branch data
is read from immutable Git objects; its runner and checker are never executed.
Changed control files make the request ineligible. Current material bytes must
match their declared source blobs, checkout revisions and canonical origins.

Accepted result schema 2 retains source/tool identities, operation/version and
registry generation, required child evidence, request digest, release identity,
artifact roles and exact output digests. Cache reuse rechecks the current release,
request, mandatory checks and bytes. Diagnostic results stay diagnostic.

`qualify-intake.pi FP OUTPUT ITHON_HOST` writes `cases.tsv`, raw observations,
checked source hashes in `interface.tsv`, and an explicit scope statement.
Together with `qualify-admission.pi`, `qualify-cache.pi` and
`qualify-delivery.pi`, this is executable fixture material for downstream
T01-S01 → P02-S05 → A06-S04 → A02-S04 integrations. It does not replace those
owners' approval, closure, applicability or independent acceptance artifacts.

The active hosted route currently performs readiness only and exits 2 with a
BLOCKED result. It installs nothing, obtains no token and activates no service.
An active-looking readiness configuration also cannot execute. The retained
installed transport/supervisor is the sole candidate execution mechanism.
Re-enabling hosted submission requires eligible Cat Food runtime closure,
independent authority and requirement projection, installed-context promotion,
and operator-supplied TLS/actor configuration. Missing BC-A01/BC-A03 interfaces
remain conditional; hashes or fixture declarations cannot manufacture approval.

Full Kitchen generation, exporter worker diagnostics, authenticated hosted
submission and native ChatGPT origin require separate execution evidence.
The old source-development Kitchen workflow is preserved outside `.github`
for historical qualification only. Cat Food #131 excludes using it to release
the normal managed-runtime gate.
