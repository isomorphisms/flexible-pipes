# Organization pin eligibility through Kitchen

Public operation: `github-organization-pin-preflight`; maintained policy:
`isomorphisms/kitchen@f37a33ac9693623cfafc16fb68c4eb10f83cf961`, task
`tasks/github-organization-pin-preflight/1.py`.

The action `.github/workflows/github-organization-pin-preflight.yml` checks out
Kitchen at that exact SHA **inside** the FP workspace, tests Kitchen's fixture
suite and the FP pipeline receipt, and invokes the registered `scripts/run-pipeline`
with declared arguments. It preserves receipts even on expected `BLOCKED` failures.

Example hosted invocation:

```text
gh workflow run github-organization-pin-preflight.yml -R isomorphisms/flexible-pipes -f organization=isomorphismes -f repositories=isomorphismes/wegert,functorial-games/spinor
```

This request is expected to produce a **failed eligibility stage**:
`spinor` currently belongs to `functorial-games`. Neither a repository
transfer nor a profile-pin change occurs. The pipeline does not report either
action as complete; when every repository is owned by the target organization
it returns `PENDING_UI` rather than `PINNED`.

GitHub currently does not provide a supported mutation to set organization
profile pins. An organization owner completes the pin selection in the GitHub
profile interface, then verifies the rendered profile independently. Do not
reinterpret PASS on an eligibility stage as the GitHub UI mutation.
