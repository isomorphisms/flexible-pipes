# How to move the user's GitHub repository to a different organization

**Search terms:** move GitHub repo; transfer GitHub repository; change repository owner; move user repository to organization; gh api repos/OWNER/REPO/transfer.

**Operation:** GitHub's native **ownership transfer**. Not a fork, mirror, copy, or reinitialization.

Flexible Pipes calls Script Kitchen's Grease generator at
$KITCHEN_ROOT/tasks/github-repository-transfer/render-standalone-github-repository-organization-transfer.ysh.
The generator deterministically writes a **complete standalone Grease program**.
Flexible Pipes saves that program, runs it under Grease, independently verifies
canonical destination and immutable repository ID, and only then renders a response.
The generated program and its SHA-256 are retained and reported.

For the already-transferred switch example, execute from a verified
flexible-pipes checkout with KITCHEN_ROOT set to a verified Kitchen checkout:

~~~console
grease scripts/how-to-move-the-users-github-repository-to-a-different-organization.ysh isomorphisms switch isomorphismes isomorphisms
~~~

Or use the equivalent named pipeline
how-to-move-the-users-github-repository-to-a-different-organization
through the existing pipeline controller (which still uses Python for its
legacy receipt machinery). The transfer implementation and deterministic program
generator use **Grease**, not Python or Bash. KITCHEN_ROOT is mandatory; never
guess a checkout location. Set TRANSFER_ARTIFACT_DIR to an existing directory
if a specific receipt destination is needed; otherwise a private temporary
directory is created and retained.

**Safety:** validates arguments, checks the authenticated login, source canonical
ownership, organization and active membership, permissions, destination collision,
and transfer POST error; verifies final identity. If the old URL already redirects
to the new canonical repository with the same numeric ID, it reports
already_transferred and **does not POST again**. On failure it prints a refusal
instead of success. It does not require a model to decide whether to transfer.

**Determinism boundary:** program bytes are deterministic for the same Kitchen
candidate and parameters. Actual transfer execution is a network mutation and
must not be called deterministic; responses are conditioned on verified state.

**Acceptance:** Kitchen's offline test includes successful transfer, idempotent
rerun, redirect, collision, wrong login, missing administrator rights, inactive
membership, rejected API mutation, and unverified response. Flexible Pipes'
integration test checks Kitchen generation, stable identity, no duplicate POST,
artifact retention, unsafe input rejection, and missing checkout refusal.
