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
