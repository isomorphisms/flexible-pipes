# How to move the user's GitHub repository to a different organization

**Search terms:** move GitHub repo; transfer GitHub repository; change repository owner; move user repository to organization; gh api repos/OWNER/REPO/transfer.

**Operation:** GitHub's native **ownership transfer**. Not a fork, mirror, copy, or reinitialization.

Flexible Pipes calls Script Kitchen's Grease generator at
$KITCHEN_ROOT/tasks/github-repository-transfer/render-standalone-github-repository-organization-transfer.ysh.
The generator deterministically writes a **complete standalone Grease program**.
The public named pipeline
how-to-move-the-users-github-repository-to-a-different-organization now only
prepares the exact Kitchen bytes for a display-only handoff. It binds the source
owner, original and resolved repository spelling, destination owner, expected
login, immutable repository ID/upstream, and exact Kitchen commit. It stops at
AWAITING_HANDOFF_DELIVERY; it does not authenticate, preflight, run, or verify
the generated program.

A differing original/resolved name is an unresolved identity, not permission to
guess. For example, the historical considered/consider mismatch must be
resolved before this operation can prepare a recipe. The runner retains legacy
Python receipt machinery only as a named migration boundary; the maintained
recipe and effect controller use **Grease**, not Python or Bash. KITCHEN_ROOT
must name the checkout whose HEAD equals the bound Kitchen revision, with no
tracked changes in its transfer-generator sources.

Preparation is not delivery acceptance. Before sending this operation, the
existing FP controller requires AI-CI's
`transfer_command.delivery_gate(kitchen_root, grease_runtime, admitted_spec)`.
That gate compares supervisor-owned operation authority and regenerates the
recipe from independently checked Kitchen source. A generic transport gate
fails before the sink is called. The controlled sender also checks exact
readback and does not repeat an accepted presentation on restart.

The shell recipe contains redirection characters excluded by the generic plain
text/HTML check. Its supported fixture presentation explicitly selects
`presentation="literal"`, with no surrounding summary or extra command text.
Unsupported plain rendering fails before send. This does not establish current
Android CodeBlock support; actual chat presentation remains NOT_VERIFIED and
the unavailable platform profile remains blocked.

**Effectful transfer is separate:** the registered
execute-github-repository-organization-transfer operation accepts the
six-bound-identity session (source, repository, destination, expected login,
immutable ID, upstream). Its maintained FP session calls AICI protected
publication admission before preflight or an external effect. In the current
normal live profile that admission is unavailable, so the operation fails before
any transfer POST. Fixture execution remains a distinct, explicitly scoped test
path and is not user-visible delivery or production authority.

**Determinism boundary:** program bytes are deterministic for the same Kitchen
commit and bound values. Displaying those bytes is not execution. Actual
transfer execution is a network mutation and must not be called deterministic;
the current protected live path is blocked rather than reported as verified.

**Acceptance:** Kitchen's native-Grease fixture suite includes successful
fixture transfer, idempotent rerun, redirect, collision, wrong login, missing
administrator rights, inactive membership, rejected API mutation, real-style
REST error bodies, and unverified response. Flexible Pipes' display path checks
exact Kitchen bytes, immutable metadata, unresolved-name refusal, and zero
fixture POST attempts. The separate execute path checks protected-admission
failure before preflight/effect and the existing at-most-once recovery behavior.

## Physical C67 acceptance and lessons

The first accepted live batch ran on a physical MIRO C67 in Termux on 2026-10-09.
Ten Kitchen-generated programs moved ten repositories from `isomorphisms` to
`isomorphismes`. After the user reported successful execution, GitHub was read
independently: every destination was canonical and retained its original numeric
repository ID. The retained evidence is in
[`evidence/github-repository-transfer/2026-10-09-c67-live/`](../evidence/github-repository-transfer/2026-10-09-c67-live/).

The accepted path established several operational rules:

- Generate, parse, and hash all standalone Kitchen programs before the first POST.
- On the C67, use an actual bounded file read plus pinned blob/header identity;
  do not substitute a redundant `test -r` prediction for observed readability.
- Preserve a failed command's exit status and response bytes separately. Real
  `gh api` emitted a 404 REST body on stdout while returning nonzero.
- Run the real Grease runtime. A `grease` fixture that merely invokes `sh` does
  not qualify Grease behavior.
- Treat visible delivery, target execution, accepted mutation, per-repository
  verification, and aggregate verification as separate stages.
- Do not report success from generated text, a zero exit status, or an accepted
  POST. Success requires canonical destination and the same immutable repository
  ID for every requested repository.

The successful ChatGPT Android handoff used ordinary plain text because fenced
CodeBlock content had rendered as an unavailable component. That is positive
operational evidence for this conversation, not deployment of a generic trusted
chat-surface adapter. The exact final terminal transcript was not retained and
must not be reconstructed.
