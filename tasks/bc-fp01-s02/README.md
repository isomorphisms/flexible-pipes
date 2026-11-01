# BC-FP01-S02 — installed transport boundary and operator acceptance packet

This is a reviewable continuation of S01 (base: `sun/bc-fp01-s01`
at `5d080f645cb6b2e221ec7bd756ca42e1a3765d8c`). S01 owns the
reconciled immutable event/route mapping, verified execution engine and exporter
diagnostics. S02 changes only acquisition/installation and the before-token
boundary. Production deployment remains **inactive**.

## Candidate acquisition and fixed closure

`scripts/install-client.pi` accepts the existing privileged
`WORKSPACE LAUNCHER` interface and a clearly separate
`qualify WORKSPACE LAUNCHER DISPOSABLE_PREFIX` fixture interface. Both
read fixed Git checkouts for `flexible-pipes` and `ithon`, establish HEAD
revisions and require every copied source byte to equal `git show
HEAD:relative/path`. The installer checks all copied .pi sources with the
existing Ithon frontend.

The fixed installation contains the client event, adapter and delivery
sources **and** the retained supervisor, registered execution, admission,
worker and watchdog sources needed by `flexible-pipes.service`. It installs
the existing Ithon host/checker components and the chosen Grease launcher.
It does not acquire a runtime or choose/approve a Grease implementation.

It records a deterministic `manifest.json` of source commits, every installed
client/supervisor source hash, every installed Ithon file hash, host Python
digest, launcher digest and the **candidate-unpromoted** state. The manifest
is content-addressed and relocation-invariant. After installation,
`/etc/flexible-pipes/client.json` is forcibly **inactive**, has no endpoint,
CA or accepted release. Installation neither installs a service unit nor
enables a service, sends a request, or acquires a token. An existing
installation is not overwritten.

The production public client must receive the *independently approved*
manifest SHA-256 in `accepted_install_sha256`, plus
`ca_sha256` and the approved `accepted_release` contract. Before it asks
GitHub for an OIDC token, it checks the CA digest, HTTPS supervisor endpoint
`/v1/execute`, the pinned manifest, every source/checker/runtime file,
root ownership and unwritable ancestor directories, promoted authority,
control commit, canonical GitHub SHA/ref and event shape. A failure writes
a BLOCKED pre-token receipt and exposes no accepted artifact. The supervisor
still owns independent signed admission, nonce persistence and execution.

## Distinct evidence boundaries

| Boundary | What can establish it | Current claim |
| --- | --- | --- |
| Static source and fixture package | S02 hosted `qualify-installed-boundary.pi` | Candidate-only; inspect actual current CI run |
| Real diagnostic TLS, two public data-only routes, exact delivered bytes | S01/exporter hosted qualification, with isolated diagnostic supervisor | Verified there; not live trusted admission |
| Trusted client acquisition and suitable non-C++ managed runtime | Cat Food / BC-P02 independent runtime acceptance | **NOT VERIFIED** |
| Approved control and checker/release authority | BC-A01 and BC-A03 accepted materials | **NOT VERIFIED** |
| Production supervisor TLS and actor configuration | Operator-provided endpoint, certificate/key and authorized actor IDs | **MISSING** |
| Installed-context promotion and service/worker isolation | Separate operator acceptance on actual target | **NOT RUN** |
| Native ChatGPT-originated signed invocation with final visible receipt | Platform integration + captured live execution | **NOT RUN** |

A content hash measures identity, not approval. The fixture-only
`preflight(..., trusted=False)` validates bytes but does not assert
root ownership, a functioning TLS certificate or active authority.
`trusted=True` is restricted to canonical `/opt` installation paths and
requires root-protected control files and ancestors. Its result is a local
preflight, not a server/execution verdict.

## Operator-owned prerequisites (no activation performed)

1. Obtain independently accepted Cat Food runtime/Grease closure and worker
   UID isolation on the proposed host. A historic C++ executable or Python-2
   startup test cannot be substituted. Prove network and filesystem access
   restrictions and document runner architecture and privileges.
2. Obtain the accepted source, checker, contract, release and actor approval
   record. It must match the intended checkout, installed manifest,
   `accepted_release`, `control_commit`, registry generation and required
   outputs. The active client will reject any mismatched installation.
3. Establish the fixed TLS supervisor hostname, valid certificate chain,
   certificate digest, service host/key, network route, GitHub OIDC issuer and
   audience, workflow identity, canonical default-branch SHA and authorized
   actor IDs. The committed empty endpoint and certificate remain empty.
4. Install in a protected host through the existing installer, independently
   compare all source/runtime bytes with the authority packet, and promote
   `/etc/flexible-pipes/client.json` only through the authorized operational
   procedure. Add `accepted_install_sha256`, `ca_sha256`, promoted
   `accepted_release` and exact endpoint. Establish root-owned supervisor
   deployment and accepted store; installation alone cannot activate it.
5. Qualify actual signed dispatch and immutable request-branch intake against
   the selected supervisor, wrong CA/issuer/audience/actor, stale ref,
   replays, duplicate/nonces, response-request mismatch, truncated delivery,
   loss/restart and absent worker isolation. Capture and compare both
   delivered receipt schema and artifact digests. Only then consider enabling
   public hosted execution and native ChatGPT caller integration.

The maintained production workflow still performs **readiness only**, exits
with `DEPLOYMENT_INACTIVE`, and intentionally acquires no token. The previous
terminal `-f pipeline=<name>` syntax is obsolete: the public workflow now
accepts a data-only `-f request='<canonical JSON>'` argument; it cannot be
claimed to execute until the installed trusted deployment is operational.
No new scheduler, agent, fallback runner or endpoint convention is introduced.
