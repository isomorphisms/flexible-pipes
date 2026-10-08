The implementation is a candidate; no publishing authority is activated.

The maintained workflow runs on hosted Ubuntu. It installs only a fixed
transport client and its checked Ithon/Grease frontend. The committed client
configuration is inactive and produces a reviewable BLOCKED result before
requesting an OIDC token. The separate `registered-service.pi` TLS supervisor
owns the execution registry, admission checks and accepted output; a job runner
never receives that authority. `flexible-pipes.service` and
`transport-contract.json` describe the concrete service candidate. No service
unit is installed or enabled by qualification.

The TLS adapter tests execute the real Kitchen operation through both routes
and verify the delivered bytes. Disposable RSA fixtures exercise the exact
checked admission implementation, including old refs, wrong source, actor,
audience, issuer, expiry and forged signatures. These tests grant no production
authority. Activation requires an accepted installed-context promotion, the
actual TLS endpoint/certificate and an established authorized actor set.

Install the exact qualified release read-only at `/opt/flexible-pipes/current`,
qualified Ithon and Grease at `/opt/catfood/bin`, and a root-owned (0600)
`/etc/flexible-pipes/deployment.json`. Its materials and tool digests come from
the independent promotion record, not from requests. Set authority to
`deployed-trusted` only after qualification of the installed context. The
request processor and publisher run as a supervisor account capable of
dropping worker UIDs; workers receive no credentials. Accepted storage is
0700 and outside worker ownership. A publication credential is supplied only
to the supervisor's artifact export step.

Both dispatch adapters use the same checked engine. Request-branch intake
compares immutable objects against the currently admitted canonical-main
base and reads precisely one regular request blob. It executes no request
worktree. A workflow dispatched at an old ref is rejected against the active
control commit before generation. Distinct retries are authenticated transport
metadata, never executable fields in request JSON.

Local `qualify` mode deliberately emits candidate/diagnostic results and
excludes deployed execution. It is unavailable through `scripts/run-pipeline`.
Installing this configuration, configuring the supervisor and activating
publication remain deployment changes; neither is performed by qualification.

The production preflight now enforces root ownership and absence of group/other
write permission on control, material, runtime, contract, qualification and
state paths and their ancestors. The deployment file must be a nonsymlink 0600
file. A digest plus an unprotected filesystem path cannot provide authority.

The client also requires an independently installed `accepted_release` record,
derived from the approved deployment and contract, never the submitted request.
It binds control/release/contract identities, version, registry generation,
required checks and both output roles. Cache reuse requires that same identity,
complete evidence and unchanged bytes. The server returns immutable request
source provenance; the client matches it to the exact submission before export.

The inspected owner evidence supplies no production host, TLS endpoint,
certificate or approved actor set. Those specific choices belong to the
Flexible Pipes deployment maintainer/operator. After installed-context promotion,
the canonical-main registered workflow and data-only inbox baseline must be
installed, followed by an actual signed routed request. The native ChatGPT tool
and captured response adapter are separate caller integration requirements;
this repository cannot force every ordinary ChatGPT response through itself.
