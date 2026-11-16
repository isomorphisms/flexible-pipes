# BC-FP01-S01 — source reconciliation; operation acceptance blocked

Authoritative assignment: [BC-FP01-S01](https://github.com/isomorphisms/ai-ci/blob/d6295a4da8fd3fab707905bb4ba8bb50695a4138/docs/build-campaign-01/wave2/FP01/jobs/BC-FP01-S01.md).
Owners: [FP24](https://github.com/isomorphisms/flexible-pipes/issues/24) and
[FP26](https://github.com/isomorphisms/flexible-pipes/issues/26).

The reconciled tree preserves live retained controller 442a33b, exporter
extension 3257e30 and current main d70159f. The merge has both the exporter tip
and main as parents; it does not reset either retained branch or change main.
It preserves current main's handoff parameter binding, explicit Grease runtime
selection, attachment handling, transfer code and receipts in the exploratory
runner, with `qualified_operation=false`. Existing callers explicitly select
that interface. The installed registered entry retains its fixed supervisor.

The admission repair binds signed event type to route, validates the exact
transport field set and binds run/attempt/control metadata. It rejects an
otherwise valid token reused with a different route's correctly shaped envelope.
Source/material preflight is separately executable without granting runtime
authority. The source contract and fixture interface are in
[registered-intake-v1.md](../../docs/registered-intake-v1.md).

## Actual local qualification

Initial source qualification executed at implementation merge
`22ae0f82ecc0de285b7eca1f8983c10cdd8c1890` using checked Ithon
`d6e83969f82512e920fb17b44326cb54f31d015c` on this disposable Linux container.
The later corrected route mutant supplies the other route's valid envelope,
so its only defect is the signed event mismatch. Final-head rechecks belong in
the review record; the evidence below retains its original source scope.

| Check | Actual outcome |
| --- | --- |
| Git-object intake and source/material preflight | 23 cases PASS; both operation schemas through both real data adapters |
| Signed admission and envelope binding | 31 cases PASS using disposable RSA keys |
| Cache/release/request/required-stage validation | 66 cases PASS; deployment preflight explicitly mocked by this retained suite |
| Client exact-byte delivery | 66 cases PASS; transport explicitly mocked by this retained suite |
| Filesystem authority protection | 9 cases PASS; 2 foreign-UID cases NOT_RUN |
| Existing pipeline preflight, Android refusal fixtures, fork renderer | PASS |
| Organization pin-preflight suite | BLOCKED: canonical Kitchen fixture checkout not materialized here |
| Signed event-check omission mutant | FAIL as required: `signed mutant accepted: event_name` |
| Signed route-check omission mutant | FAIL as required: `SIGNED_ROUTE_SUBSTITUTION_ACCEPTED` |
| Full Kitchen operation | BLOCKED before execution: single-UID namespace |
| Exporter diagnostic | 9 request rejections PASS, then BLOCKED before isolated worker execution: single-UID namespace |

Raw failure and stdout/stderr records, source hashes and case identities are in
`evidence/`. Mutant sources are deliberately rejected specimens. The original
route-mutant attempt and its corrected-envelope successor are both retained;
the successor establishes the actual route-substitution refusal.

## Unreleased boundaries

The historical Kitchen source-development workflow is inactive under
`deployment/`. The active source workflow deliberately ends with BLOCKED
readiness, and the public workflow performs readiness before installation,
token acquisition or execution. No historical Python-2 launcher or C++ binary
is bootstrapped to qualify the default managed runtime.

Kitchen's full operation still needs independently accepted compatible non-C++
Cat Food runtime closure and a multi-UID qualification host. BC-A01 requirement
projection and BC-A03 authority material remain conditional inputs. TLS endpoint,
certificate, actor set, installed-context promotion and authenticated hosted
request remain unconfigured. Native ChatGPT origin and client presentation are
separate NOT_RUN boundaries. No merge, release, managed installation, service
activation, live transfer or model-job dispatch was performed.

Current main's independently pinned native-handoff action still calls the older
generic path and consumes the excluded historical C++ artifact. That downstream
owner action must consume the released exploratory/interface boundary and
eligible runtime material before its qualification can pass. Its old pin is not
silently rewritten or counted as this controller's acceptance.

T01-S01 → P02-S05 → A06-S04 → A02-S04 may consume the documented source/fixture
interface; none may infer deployed operation acceptance from these local tests.
