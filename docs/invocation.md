# Public invocation and qualification boundaries

The retained registered-operation branch and the default branch have different
entrypoints. Source presence, fixture qualification, deployment and an actual
routed request are separate evidence. Do not advertise a candidate interface as
the currently deployed command.

## Registered operation candidate

On this branch, `.github/workflows/run-pipeline.yml` accepts a data-only `request`
input. Its canonical-main event adapter and immutable `pipeline-requests`
intake submit to the same separate supervisor. Requests cannot select the
runner, checker, recipe, policy or approval requirements.

The only registered operation is `kitchen-transfer-script`. Its explicit inputs
are source owner, repository, destination owner, expected login, numeric
repository ID and qualified target context. It generates and checks a script;
it does not execute a live transfer. Kitchen owns the recipe, AICI the independent
API observation validator, and Cat Food the sealed-artifact validator.

The installed `scripts/run-pipeline` takes `github-event EVENT_FILE`. It requires
the fixed installed Grease/Ithon client and authenticated GitHub event context;
it is not an arbitrary-directory terminal generator. `deployment/client.json`
is inactive. The candidate returns `DEPLOYMENT_INACTIVE` before token acquisition.
See `deployment/README.md` for the unfulfilled activation boundary. Do not
silently activate it or promote diagnostic qualification to deployment.

## Existing generic execution

`scripts/run-pipeline-legacy.py NAME` keeps exploratory, caller-supplied pipelines
available. Its `PASS` means the supplied commands completed successfully, not
that a separately approved operation or exact human handoff was accepted.
Receipts explicitly carry `qualified_operation: false` and the narrower scope.
The historical workflow is retained as `deployment/run-pipeline-legacy.yml`;
it is not installed as a second active authoritative workflow.

At the October 8 audit, default branch
`9775aa324f523cbc6c758e89461915484a5a0fc7` still uses the generic runner at
`scripts/run-pipeline` and accepts a `pipeline` workflow input. This branch's
registered entry must not be invoked using that older interface. Integration
must preserve subsequent generic-runner and human-delivery work from main.

## ChatGPT and unavailable execution

“Run flexible-pipes pipeline NAME” is a naming convention. It is not a mandatory
ChatGPT hook, and repository instruction files are not automatically loaded by
every conversation. An actual producer must invoke the registered path and
enforce its accepted result. Cockswain's supervisor is not such an active caller
while its dispatch boundary remains unimplemented.

When direct execution is unavailable, a supported maintained Kitchen generator
may still produce a checked terminal handoff. Label it generated, not submitted,
executed or transferred. Do not retype or shorten its checked bytes. The retained
generator currently targets `linux-x86_64-grease-v1`; a compact fresh-Termux paste
unit and its target acceptance remain work under Kitchen #15/#24 and AICI #205.
An inactive supervisor is not a reason to forbid all generation, and a fixture
script is not proof that the user's current terminal can run it.
