# Installed-path source regression

The original `installed_client.pi` at
`25589c499517da22b2919c7797b3a1a74595e809` checked only the ancestry of
`Path(path).resolve()`. Its declared canonical prefix therefore did not protect
the lexical route used to reach those bytes.

The retained counterexample uses the actual fixed
`/opt/flexible-pipes/current/manifest.json` path on a disposable hosted runner.
`current` points to an approved root-owned, unwritable tree while its lexical
parent `/opt/flexible-pipes` is group-writable. The former implementation
accepts the resolved protected target; the repaired implementation must reject
the lexical path with `CLIENT_PATH_UNPROTECTED`. The test retains the former
implementation as a named hostile control and also requires a protected twin.
The same root-owned generation alias first passes with its lexical parent at
mode 0755. Changing only that parent to 0775 must then refuse. Protected aliases
are not forbidden: each link's ownership and both its lexical and resolved
target ancestry are checked, including runtime leaf-link target chains.

The test will copy and execute the installed Ithon client with production path
validation enabled. A missing-token sentinel distinguishes successful preflight
from refusal before token acquisition. No token, TLS service, service unit,
managed installation, production promotion or Grease execution is supplied by
this fixture. The hosted runner's candidate configuration is restored inactive.

`qualify-installed-paths.pi` retains a second real-filesystem twin without
writing anything: `/usr/bin/python3` and `/tmp/../usr/bin/python3` resolve to
the same bytes, but the latter traverses writable `/tmp`. The old algorithm
accepts both; the new check must reject the lexical route. This fixture also
requires a real root-owned host hierarchy rather than mocking ownership.

The local execution host is uid 1000, has no `sudo`, and presents `/` as owned
by uid 1000 and system files as uid 65534. The pinned Ithon frontend checks the
new source successfully, then the canonical fixture refuses with
`S02_DISPOSABLE_ROOT_REQUIRED` and the existing-path fixture refuses with
`S02_TRUSTED_HOST_ROOT_REQUIRED`. Neither refusal counts as filesystem
qualification. Actual root-owned execution requires the disposable hosted
runner; local source/type checks do not replace that evidence.

Local checks used the existing checked Ithon host at
`d6e83969f82512e920fb17b44326cb54f31d015c`: importing the repaired
`installed_client.pi`, cache/retry regressions, signed-admission controls and
client-delivery regressions all passed. `git diff --check` passed. The new
filesystem fixtures passed whole-module static checking before their explicit
host/root refusals. Canonical filesystem behavior, copied-client execution and
the retained old-algorithm counterexample remain **NOT_RUN** until the new
hosted workflow completes at the published repair head.

The S02 workflow now runs for every pull request and for main/retained-S02
pushes. Its eligibility no longer omits client, worker, admission, deployment
or fixture inputs from the installed-source assertion.

## Eager dependency execution counterexample

`tests/registered-execution/fixtures/prior-eager-client.pi` preserves the actual
client from `71ec5a91ca3994f79fa0e729bf4db3e637af8b7f` before the lazy-import
repair. It is an explicitly unaccepted specimen, never a maintained entrypoint.
The hosted test copies that exact file beside the installed scripts and appends
a harmless marker write to installed `delivery.pi`. The specimen's readiness
call must create the marker despite returning `DEPLOYMENT_INACTIVE`, retaining
the original import-before-validation counterexample. It then clears the
marker and requires the current copied client to return
`CLIENT_SOURCE_CHANGED: scripts/delivery.pi` while the marker remains absent.

The current client delays event and delivery imports until the manifest closure
has been checked. `installed_client.pi` checks that closure before lazily
loading the shared delivery release validator. The pinned Ithon loader and the
installed bootstrap checker remain explicit trusted inputs; these checks do
not authenticate a substituted loader/checker or supply independent deployment
authority.

The local actual-Ithon copied-source experiment reproduced the eager specimen:
readiness returned `DEPLOYMENT_INACTIVE`, exit 2, and the marker existed. The
current copied client returned the same inactive receipt with the marker absent.
This is source-level import ordering evidence, separate from the hosted
installed active-client refusal.

## Disposable protected filesystem

Hosted diagnostics at repair source
`23c93c2008d5acb1d0c0bef139f320e3630ea120` observed root ownership with `/opt`
mode 0777; `/`, `/etc` and `/usr` were root-owned 0755. The production guard
correctly refused that inherited writable ancestor. The fixture must not chmod
the existing host `/opt` or relax the guard to manufacture a positive.

The hosted wrapper now selects a private mount namespace. Before mounting, the
fixture requires its namespace identity to differ from PID 1 and requires no
shared mount propagation tags. It records the original filesystem metadata,
then mounts an actual private tmpfs at `/opt` with root-owned mode 0755 and
records the resulting metadata and mount table. Canonical client paths are
created only after this check; pre-existing `/etc/flexible-pipes` and
`/var/lib/flexible-pipes` still cause refusal. Only fixture-created paths are
removed. Namespace or mount failure remains a concrete blocker with no fallback.
The private mount disappears with the bounded fixture process; no service is
installed or activated.

The observed installer also left newly created intermediate directories
world-writable on that host. `install-client.pi` now creates each missing
directory with explicit mode 0755, without changing existing directories or
overwriting an existing final installation path. This repairs producer output;
the fixture does not chmod installed outputs to obtain acceptance.
