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

The hosted fixture copies and executes the installed Ithon client with production path
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
host/root refusals. Later exact-head hosted runs
[43794987449](https://github.com/isomorphisms/flexible-pipes/actions/runs/43794987449)
and [43794977572](https://github.com/isomorphisms/flexible-pipes/actions/runs/43794977572)
passed all 12 canonical-path/copied-Ithon cases at
`d453b88a46dedd4c2dde72e4d00a76990df5c8c7`. These are prior-head results; they
do not qualify the subsequent installer preservation repair below. Successor
canonical hosted qualification remains pending.

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

## Installer output preservation

The actual installer at
`d453b88a46dedd4c2dde72e4d00a76990df5c8c7` overwrote an existing regular
`client.json` sentinel and followed a dangling configuration symlink to create
an outside-prefix file, reporting `CANDIDATE_INSTALLED` in both cases. The exact
unaccepted factory is retained as
`tests/registered-execution/fixtures/prior-output-installer.pi`, SHA-256
`fee55a8ec83f2ef8f18462e85b440a0048b7881cfbc9024cfdbd453d1444d319`
(original Git blob `b72ca133f0b6b59ff65ac0654e85d197fe9ec2e8`). The new
preservation suite executes that specimen to retain both original
counterexamples rather than substituting a model of its behavior.

The repaired factory checks existing configuration, declared candidate subtrees
and unsafe routes before candidate effects. It walks directory descriptors
without following symlinks, verifies production ownership/modes including `/`,
and checks fixture routes from the explicit prefix inward. It changes modes
only for directories it creates. The inactive configuration is reserved before
the candidate source tree. Every regular output leaf uses actual exclusive
creation with `O_CREAT | O_EXCL | O_NOFOLLOW` below its anchored parent
descriptor. Runtime symlink creation also uses an anchored parent descriptor.
Copied source/runtime payloads are the same bytes verified against Git, rather
than a later reread. Export-directory modes are set through the newly created
directory descriptor.

Exclusive creation preserves a competing writer's bytes, including one arriving
after preflight. A later collision can leave an inactive partial candidate;
this is a failed install requiring review, not rollback or promotion. The
factory does not overwrite or remove an existing leaf to make retries pass.

`qualify-install-preservation.pi` passed 12 actual-Ithon cases against repaired
factory SHA-256
`a0bae4beec51fdc9f60ce70774c596791627f7703f602c405d6f9a8ccc491f86`:
two old-factory counterexamples, four pre-effect refusals (existing regular or
dangling configuration, symlink parent and writable parent), a fresh inactive
positive, and five competing-writer cases covering regular/symlink
configuration, copied source, Ithon launcher and manifest. The original
16-case `qualify-installed-boundary.pi` suite also passed against those same
factory bytes through pinned Ithon
`d6e83969f82512e920fb17b44326cb54f31d015c`. `git diff --check` passed.

The competing-writer fixture interposes only deterministic timing at the actual
installer's `os.open` boundary. It runs the complete checked installer through
the ordinary Ithon runner, delegates every open to the saved real builtin and
independently checks filesystem sentinel bytes, symlink identity and absence of
the outside-prefix target. It does not mock the installer, filesystem authority,
producer result or write syscall. This is bounded competing-writer source
qualification, not proof against an arbitrary actor with the installer's own
privileges. Hosted qualification of the successor source is still required;
runtime eligibility, operational installation and service activation remain
separate.
