# Registered execution boundary, version 1 decision

Status: design selected; implementation and qualification pending. This is a source/evidence decision, not a deployed security boundary or a job prompt. Primary owners: [#24](https://github.com/isomorphisms/flexible-pipes/issues/24), [#26](https://github.com/isomorphisms/flexible-pipes/issues/26), [#2](https://github.com/isomorphisms/flexible-pipes/issues/2), [#28](https://github.com/isomorphisms/flexible-pipes/issues/28). Historical coverage: [#18](https://github.com/isomorphisms/flexible-pipes/issues/18).

## Decision

Keep the existing scripts/run-pipeline entry point and its two dispatch routes. Replace the execution trust model with a qualified operation allowlist, a data-only request, and a trusted supervisor/validator/publisher separated from the application build process. No scheduler, new language, model inference, model download, or arbitrary-command API is required.

An operation name selects a maintained adapter and an independently promoted version. It does not select executable definitions from the request checkout. The application source, recipe, runtime/tools, validation contract, and request have separate identities. An author can propose all of them, but cannot certify a proposal by supplying its own expected hash. The trusted release supplies expected identities and required checks.

A supported request is: select operation -> validate all inputs and prerequisites -> bind immutable source/recipe/policy/tool identities -> execute -> independently check actual outputs -> collect/authorize the exact result. Repairs create a new candidate and a new run; they never rewrite a failed run.

The smallest complete useful slice includes the boundary AND the Kitchen generator operation. Android qualification composes existing owners as a second slice. A schema-only runner remains incomplete.

## Retrieved source and moving work

The six repositories were cloned, including their advertised branch objects. These exact initial main revisions were materialized and inspected (later AICI refresh is recorded below):

| Canonical repository | Stable GitHub repository ID | Main revision |
|---|---:|---|
| isomorphisms/flexible-pipes | 1405888814 | 58fffd879e52a34110b6da22ab2fc03f1f48befe |
| isomorphisms/kitchen | 1397611140 | b8be8b1de05827422bbf127b44720e0e2c7acc1e |
| isomorphisms/catfood | 1342832897 | 5c0ae8841e2c5553cfaed69a9bcf660991eddad1 |
| isomorphisms/ai-ci | 1345324774 | b6885ca589f5d98f6bb30166e3abaa09245b20e5 |
| isomorphisms/android-NDK | 1392949435 | d4a4719fb97e8031476bf822697dce8423bc9030 |
| functorial-games/crystal | 1404850438 | 25b63837091c92e07738b1b51865603cc4b5e63d |

Do not substitute isomorphisms/crystal for the canonical owner. The operation registry must retain numeric repository identity across an authorized rename/transfer, while recording the observed canonical name.

Related work was inspected before design:

- [isomorphisms/flexible-pipes PR #27, “Add stable pipeline invocation and historical regression smoke”](https://github.com/isomorphisms/flexible-pipes/pull/27), merged; main above contains it. Request branch materialized at 124275f2d5ded53d5ea0d50b8e499b62aca3b9ae. No open FP PR existed at initial inspection.
- [isomorphisms/kitchen PR #22, “Prevent unverified and non-repeatable IB test handoffs”](https://github.com/isomorphisms/kitchen/pull/22), merged, head e2a7fa8ea7f4bb64be2618990654e47eaa235375.
- [isomorphisms/kitchen PR #25, “Generate descriptive GitHub repository transfer scripts”](https://github.com/isomorphisms/kitchen/pull/25), merged, head 3cec7cdbaa1a3cc3e8644d5de87f37500892c500. Current main includes the generator and source-handoff work.
- [isomorphisms/catfood PR #105, “Catch up IB checkout help and preserve the verified phone baseline”](https://github.com/isomorphisms/catfood/pull/105), merged, head 7aa6fe0934670248072a3211d0abe9d3b40a446a. Current main contains the isolated Git identity checks.
- [isomorphisms/android-NDK PR #15, “Add fail-closed direct NativeActivity APK packager”](https://github.com/isomorphisms/android-NDK/pull/15), draft, 7aa8e2dbb0e4d2726382e6c47994a710977563a6. This is real newer implementation, not a missing file or qualified production release.
- [isomorphisms/ai-ci PR #206, “Register canonical Crystal test signing identities”](https://github.com/isomorphisms/ai-ci/pull/206), draft, moved during retrieval from f99f2025fd085a3cda6d19e5e8a6deeeed7bcaf9 to 3f542ba91c86a0a66a4c16c779f205d075b02871. The latter proposes original package IDs with the stable public test certificate. It subsequently merged while this audit was active: main 6a87f20b39a71bd9e875061874c841f68c9db888 was fetched and inspected; its only change against the initial main is three original Crystal package registrations. This records merged registry state, not evidence that the original-device signer migration was authorized or completed.
- [functorial-games/crystal PR #7, “Build MIRO Halite, Quartz, and Bismuth APK prototypes”](https://github.com/functorial-games/crystal/pull/7), draft. Historical 7ce6f1bac907222d985da296316b09e24bc43000 was materialized and inspected; refreshed 52b657b562be1b1e32b326e1e971d8b28339938e was fetched and inspected. A third refreshed snapshot 8233886ef135a8935d5351dcde9ed07763993288 was then fetched and inspected. All three remain distinct.
- Ithon source was additionally materialized at dilapidated-shed/ithon@396d8b7af1417a0a61245db940fdb22ef9fbac51 through the Cat Food tools.tsv route. Its launcher reaches the host frontend; --help reports unsupported. This is source/entrypoint availability, not qualification for FP's needed imports and typed boundaries.

Open branches and PRs were enumerated for each owner; ai-ci branch enumeration required a second page. No separate producer-composite implementation appeared in the initial inventory. The later refresh found [isomorphisms/ai-ci PR #209, “Add mandatory Android producer composite gate”](https://github.com/isomorphisms/ai-ci/pull/209), branch android-producer-composite-gate at materialized 8fb5dc6eab010f2cb342129c3931f4fc28ad5bc5. Its check.sh, action.yml and README were inspected. Continue that implementation, not a competing gate. Later work must refresh again.

## What the current interface actually does

At the inspected FP main, scripts/run-pipeline and scripts/check-regression-cases are Python source, mode 100644. The documented local form uses python3; direct execution without an interpreter fails permission checks. Do not invent an existing fp run command.

The workflow_dispatch route runs run-pipeline.yml at its selected workflow revision. The push route checks out the triggering pipeline-requests revision. That revision supplies the workflow, runner, pipelines, and corpus checker. The request parser checks only pipeline and ignores other keys. Changing a request and executor together is not rejected. A non-main workflow_dispatch ref can also select old/different executor policy.

The runner validates each stage only when reached, takes argv from the same checkout, inherits environment/PATH/Git settings, and uses GITHUB_SHA in preference to observing Git HEAD. Cwd containment does not confine subprocess effects. It buffers output without a limit, supplies no stage timeout, and records its final receipt only at shutdown. GitHub reruns reuse GITHUB_RUN_ID without an attempt suffix. The existing receipt does not establish required check completion, qualified executable provenance, artifact promotion, or independent acceptance.

The existing smoke checks the shape of 13 corpus records, not any prose oracle. Empty cases also pass. [Existing hosted request run](https://github.com/isomorphisms/flexible-pipes/actions/runs/37334198791) was observed completed/success at request head 124275f2d5ded53d5ea0d50b8e499b62aca3b9ae; that is historical route/corpus evidence, not qualification of this design. No new hosted dispatch was made in this audit.

Repository rulesets returned an empty list. Branch-protection inspection returned 403 (integration cannot inspect that endpoint); no gh executable was available locally. Therefore this audit does not claim protected-main or credential separation is already configured.

## Language boundary

The existing Python runner/checker were exercised unchanged as explicitly named legacy debt. Do not add new maintained Python enforcement behind their extensionless names. Keep the public scripts/run-pipeline name; implement its new control logic through checked Ithon .pi source and the existing Ithon frontend, with a qualification receipt binding checked source to executed source. A thin launcher is ordinary runtime plumbing, not permission to hide new Python logic. Scope this transition to the runner/validator files that this change actually needs; do not migrate the repository, model tools or other owners first.

Ithon's materialized host frontend is a supported upstream runtime substrate, not proof that the whole future FP program already type-checks. The authoring job must test required typed foreign interfaces and record any actual gap; no success-printer or extension-only rename can satisfy that boundary. Do not require rebuilding CPython or a whole compiler fleet as a prerequisite.

New maintained shell code uses the actual verified Grease runtime. Existing POSIX source-handoff keeps its exact pre-Grease, temporary-source-test exception. That exception does not extend to transfer mutation, provisioning, Android packaging or FP orchestration. Existing Bash/POSIX owner candidates must be explicitly qualified/repaired under applicable policy, not treated as approved merely because they were committed.

## Failure/enforcement map

Labels: R = reported history/user account; H = prior audit with linked evidence; S = current source inspection; X = locally executed in this audit. A proposed regression is not an executed result. All 13 history.json IDs appear below. Original transcript URLs were not recovered for every historical case; those rows retain that limitation rather than citing a later summary as an original transcript.

| Failure and evidence | Earliest preventable boundary | Existing owner/mechanism | Missing enforcement | Executable regression required | Remaining limitation |
|---|---|---|---|---|---|
| Committed helper instead of transferring repository, R/H: [Kitchen #20](https://github.com/isomorphisms/kitchen/issues/20), incidents/2026-10-01-misread-gh-api-move-script.md | Intent -> operation selection | Kitchen transfer task | Separate generate-script vs execute-transfer operation/effect contract | Generate makes zero API mutations; transfer fixture must change canonical owner of same numeric repo ID | Language ambiguity needs reviewed intent; generation cannot count as transfer |
| crystal-reinvention, R: [FP #18](https://github.com/isomorphisms/flexible-pipes/issues/18) | Select source/recipe before authoring | Crystal implementation; FP #9 | Source/build-entrypoint identity bound to registered operation | Unrelated renderer/entrypoint rejected; requested implementation passes | Original offending turn unavailable; do not claim reproduced renderer substitution |
| Wrong executable/backend/branch, H: [FP #9](https://github.com/isomorphisms/flexible-pipes/issues/9) | Materialization/preflight | Cat Food inventory; AICI build-toolchain-v0 | Executable/tool closure and actual invocation witness | PATH-shadowed stock/stale executable; forbidden compiler; wrong branch/source | Behavior distinguishing custom compiler needs project-owned semantic fixture |
| Genuine NDK compile then Gradle package, S/H: [Crystal #8](https://github.com/functorial-games/crystal/issues/8), historical source 7ce6f1b... | Validate operation recipe and final promotion | Android-NDK #14; AICI #207/#175 | Whole compile/package path and mandatory producer composition | Real NDK .so plus Gradle-built APK must fail; direct path positive twin | New candidate changed route; historical failure does not prove latest source still uses Gradle |
| earth-moon-bootstrap, R/H: [FP #26](https://github.com/isomorphisms/flexible-pipes/issues/26), [Cat Food #107](https://github.com/isomorphisms/catfood/issues/107) | Before task side effects | Cat Food runtime/inventory; AICI host-context | Separate capability/acquisition probes | Missing checkout, executable, authentication, API permission, network and Lua each yield typed blockers, zero mutation | No capability probe proves another target's state |
| nonexistent-runner, R/H: [FP #9](https://github.com/isomorphisms/flexible-pipes/issues/9) | Before serving execution job | Cat Food target matrix #89 | Resolve retrievable executable/artifact, not a remembered pathname | Missing locator blocks before a job is issued; good published fixture runs | Original dmd-thumb2-test transcript not recovered; no new device run |
| transfer-tests-not-run, R/H/S/X: [Kitchen #15](https://github.com/isomorphisms/kitchen/issues/15), [#24](https://github.com/isomorphisms/kitchen/issues/24), [AICI #205](https://github.com/isomorphisms/ai-ci/issues/205) | Qualification of exact delivered bytes | Kitchen descriptive generator and current nine-case suite | Fresh-home actual-artifact twice, byte identity and independent API recorder | No prior K/cwd/checkout; two unrelated directories; generated bytes tested, not just helper | Nine current tests pass but still fake personal account as organization and do not prove phone delivery |
| handoff-wrong-context, H/S/X: [Kitchen H1](https://github.com/isomorphisms/kitchen/blob/b8be8b1de05827422bbf127b44720e0e2c7acc1e/incidents/h1-root-causes.md) | Producer materialization before command emission | tasks/source-handoff/1.sh; Cat Food where | Adopt gate in supported class; separate adapters elsewhere | Existing 27 cases cover unpublished/foreign/wrong-branch files, wrong origin, inherited Git, changed bytes, false green; rerun exact command with parent survival | Temporary-file POSIX source-test adapter only; not an admin sandbox/installer |
| Fixed clone path, hidden variables, partial/dirty state, top-level exit, H/S/X: same H1; Cat Food #107 | Acquisition/handoff boundary | Cat Food lookup and Kitchen emitted child command | Safe scoped acquisition and invocation | Arbitrary cwd, spaces/quotes, fresh home, repeated/interrupted/concurrent call; parent errexit survives, task still fails explicitly | Existing source-handoff coverage cannot qualify transfer/provisioning class |
| git-fetch-ref, R: [FP #18](https://github.com/isomorphisms/flexible-pipes/issues/18) | Resolve source before execution | Kitchen isolated source acquisition | Resolve one exact object using explicit refspec/fetch target | Disposable remote where FETCH_HEAD exists but expected remote ref does not; reject/refetch correctly | Original transcript unavailable; reproduce topology rather than pretending this history reran |
| grease-wrapper-false-pass, R/H plus generic X | Required completion before aggregate result | AICI suite/evidence contracts; Kitchen scoped completion | Independent required-check inventory and completion records | Inner setup/test fail or skip with outer zero; no-op test; forged PASS text; downstream publisher must not run | Exact original Grease source not re-executed; generic no-op omission reproduced here |
| branch-dex-separate, R/H: [FP #18](https://github.com/isomorphisms/flexible-pipes/issues/18) | Authoring qualification/source topology | AICI merge dependency/evidence contract | Reviewed ancestry predicate, not branch label | ARM-descended DEX candidate rejected; sibling positive; QEMU cannot satisfy ART | This is a task-specific historical topology constraint, not a universal ban on shared ancestry |
| merge-authorization, R/H: [AICI correction](https://github.com/isomorphisms/ai-ci/pull/141), failure ledger | Authorization before mutation | AICI merge/ authority collector/verifier | Bind operation/effects to established task authority | Existing task-context + continuation passes; isolated acknowledgement fails; new effects/objection blocks | history.json wording overstates fresh explicit approval; preserve contextual authority |
| blocker-unknown, H: [Cat Food original integration repair](https://github.com/isomorphisms/catfood/pull/48), AICI failure ledger | Result/authorization aggregation | AICI merge typed blockers | Keep UNKNOWN and first failing stage | Red/unknown mandatory stage plus later success remains non-PASS | Diagnosing causality may need judgment; it cannot waive a required failure |
| device-bundle-overclaim, R/H: FP #18; Cat Food android/acceptance | Acceptance aggregation | Cat Food per-target receipts; AICI evidence classes | Required case inventory and exact artifact/target binding | One failed/skipped/stale case prevents bundle PASS | Physical reports are not host fixtures; original complete transcript unavailable |
| Old baseline/new feature; host/emulator/physical conflation, H/S/X: H1; [FP #16](https://github.com/isomorphisms/flexible-pipes/issues/16) | Scope comparison before acceptance | Kitchen scope/exclusions; AICI merge evidence | Trusted acceptance-scope selection | Baseline offered for E2; emulator offered for MIRO A1; sibling/ancestor receipt fails | Observation authenticity is separate from checking receipt structure |
| Green receipt for changed source/recipe/artifact, S/X | Snapshot and promotion | FP receipt; AICI exact-artifact contracts | Immutable input/output snapshots and independent validator | Change source/contract/recipe after check; replace APK; stale target/acceptance scope; reject at public result path | Hash alone does not authorize expected identity |
| Ephemeral/wrong signer and package-ID workaround, H/S: [AICI #158](https://github.com/isomorphisms/ai-ci/issues/158), [#199](https://github.com/isomorphisms/ai-ci/issues/199), Crystal #8 | Before signing and again before export | Central android-signing registry, Android-NDK packager | Approved authority pin outside worker; no key generation; exact finished-APK comparison | Missing/wrong key; edited expected fingerprint/registry; .inspect rename/uninstall workaround rejected | Original key recoverability UNKNOWN; no authorized migration inferred |
| Same-byte reinstall presented as cross-build continuity, H: [AICI #137](https://github.com/isomorphisms/ai-ci/issues/137) | Stable-lane qualification and per-build prior-artifact check | AICI update-identity owner | Two distinct accepted APKs, trusted prior receipt and version comparison | Build A then distinct B; install A -> replace with B without uninstall; downgrade/wrong signer fail | Emulator replacement and physical replacement remain different claims |
| Install/launch presented as zoom/wireframe correctness, R/H/S: Crystal #8 | Claim/semantic acceptance | Crystal behavior tests; Cat Food evidence scopes | Observable input/visual contract | Nonblank/motion tests plus targeted wireframe/pinch invariants and broken controls | Screenshot difference alone cannot prove desired geometry/interaction |
| catfood-front-room, R: FP #18; [AICI #10](https://github.com/isomorphisms/ai-ci/issues/10) | Authoring contract/inventory review | Cat Food promoted menu/target matrix | Exact required surface and dependency allowlist | Omit curl/ICU/Grease/Idriç/IB or add undeclared moving dependency | Choosing the intended menu needs semantic review; no full original transcript recovered |
| grease-rejected-fixture, R and S: FP #18; catfood doctor.sh currently contains rejected expression | Authoring fixture review | Project fixture corpus + AICI language/evidence rules | Explicit forbidden fixture/approved positive twin | Reject the recorded literal/expression; permit ordinary value | Literal check cannot decide every semantically equivalent joke; source presence was observed, bootstrap not executed |

## Existing tests and audit probes

Local Linux x86_64 only; no mobile mutation, APK build, emulator, signing, model inference, or live transfer occurred.

- Kitchen main: tests/source-handoff.sh: 27/27 PASS; tests/github-repository-transfer.sh: 9 named scenarios PASS. These prove only their actual fixture scope.
- Cat Food main: tests/ib-handoff.sh: 14/14 PASS; tests/android-delivery.sh: exit 0. Existing Android package schema supports archive/file/dex-jni, not a first-class APK record.
- FP documented Python invocation: regression-history-smoke PASS with 13 corpus records.
- Unchanged FP runner copied by a local isolated Git clone; runner diff from inspected main empty. Seven synthetic pipeline data files exercised real scripts/run-pipeline. Unknown operation, forged metadata and empty corpus were additional probes.
- Positive command PASS. Nonzero child FAIL with downstream marker absent. Missing executable FAIL with child code 127. Unknown name rejects with exit 2.
- Omitted mandatory check: PASS and scratch export-marker created. No-op success printer as required-test: PASS. Unknown executable-related fields: ignored/PASS. Later invalid stage: FAIL but earlier scratch marker already created. GITHUB_SHA of forty ones: receipt reports that value despite actual HEAD. Empty corpus: exit 0.
- Raw local process outputs, fixture definitions and exit codes are preserved alongside this decision. These probes reproduce the current runner's limits, not the complete historical incidents. Altered remote workflow, interruption, bounded output, TOCTOU and Android hostile cases are source-derived risks/required future tests, not newly executed tests.

## Lifecycle and authority

| Transition | Permitted actor and evidence | Result |
|---|---|---|
| Author candidate | Authorized author, isolated branch; intended operation/effects/semantic contract | Unqualified version; cannot be served as accepted execution |
| Qualify candidate | Trusted qualification job running fixed tests outside candidate write scope; source and dependency closure; positive and hostile fixtures; semantic contract review | Bound qualification record, still not active |
| Promote version | Maintainer or delegated promotion identity with established authority, valid qualification and no unresolved blocker | Immutable release entry, monotonic generation, active pointer |
| Execute version | Driver with execute-only interface; validated data; authority covering that operation/effects | New immutable attempt, structured result |
| Repair failed operation | Separate authorized authoring task; failed attempt preserved; changed bytes requalified | New version and new run; links superseded attempt without changing its result |

No ceremonial approval per read, scratch creation or harmless internal step. Existing task authority persists. A change from generation to live transfer, build to uninstall/install, test signer to release signer, or approved package ID to a new identity is material and needs applicable authority. The authoring job cannot manufacture that authority.

Execution mode cannot edit source recipes, registry, contract, policy, qualification results or previous receipts. Application source is a resolved read-only input; requested source changes occur in authoring first. No caller shell, argv, environment, interpreter, compiler, signer fingerprint, acceptance skip or policy revision is accepted.

## Concrete trust layout and dispatch

Use four domains:

1. Request data: the inbox or workflow inputs, size limited and parsed strictly; never sourced or imported.
2. Application snapshot: numeric repository ID, canonical URL, approved branch/ref selector, observed commit/tree and required blobs. Source code is untrusted build input.
3. Qualified implementation snapshot: Kitchen recipe, Android-NDK packager and permitted application build adapter at exact promoted revisions, plus runtime/tool closure.
4. Trusted control release: FP supervisor, AICI validation/promotion machinery and approved registry/contract versions. The worker and ordinary driver cannot write this domain.

The implementation should use an unprivileged isolated worker on the declared hosted Linux target: read-only input/tool mounts, separate writable scratch/output, no host socket, no credentials, no writable control/evidence directory, and network denied after bounded acquisition. The trusted supervisor captures process exits/output/witnesses outside worker write scope. Tests execute against frozen produced outputs in a separate verifier context. The publisher runs after validation in a separate job with only the necessary destination credential. Private signing credentials never enter application build/test code. Public test certificates do not authenticate a trusted run.

Retain both user routes:

- workflow_dispatch on canonical main becomes a data-only request into the trusted release. Reject another ref for accepted execution. Deployments pin the accepted release independently, not from request input.
- pipeline-requests becomes an inbox. Its push workflow only signals submission, with no accepted-execution/publishing authority. A default-branch workflow_run handler reads the completed intake event and exact request blob as DATA from GitHub. It independently checks repository ID, branch, event, submitter authority, exactly one regular request file, size/schema, and an unchanged non-request tree against the approved inbox baseline. It never checks out or executes the request revision. Intake success or uploaded receipts are not trusted.
- Both paths call the same scripts/run-pipeline implementation from the pinned control release and produce the same result schema. workflow_run is a new adapter, not an alternative engine. Never use pull_request_target to execute source-controlled code with secrets.
- An altered request workflow may run its own untrusted job; it has no credentials accepted by the publisher and cannot produce an accepted receipt. Changed workflow/runner/pipeline bytes are rejected by the trusted intake. A branch name alone provides no such guarantee.

Prevent within the controlled deployment: caller command injection/selection, unchecked parameters, unqualified adapters, policy rollback, source/recipe TOCTOU, child-forged PASS, accepted export without required checks. Credential/file isolation makes those denials meaningful.

Detect only: leaf workflows omitting the shared path, unknown producers, drift between declared and observed executables, unapproved downloaded artifacts presented through another interface. AICI's producer inventory/scanner records missing coverage; it cannot stop a separately authorized user uploading a file.

Outside this boundary: an assistant retaining broad shell, GitHub write/admin, secret and upload permissions can attempt bypass. Full prevention requires the execution persona's surrounding permissions to expose only submit/status/artifact, and separate maintainer credentials for authoring/promotion. No AGENTS text, hash, filename, unprotected Git branch or self-signed sidecar solves that. Configure these permissions during controlled deployment; do not defer interface construction until every ChatGPT surface is restricted.

## Exact v1 data contracts

Use the existing JSON request/result transport, strict UTF-8 and duplicate-key rejection. Use plain TSV for the promotion/alias index and TOML for typed operation configuration; no new expression language or programmable steps.

Proposed request schema v2:

    {"schema_version":2,"request_id":"caller-unique-token","pipeline":"kitchen-transfer-script","inputs":{...}}

Only those four top-level fields. request_id is 1..80 ASCII letters/digits/._- and is scoped to authenticated caller. pipeline is an exact registered name or exact registered alias, never a path. inputs is an operation-specific object; unknown fields, wrong types and duplicate keys reject. At most 16 KiB serialized. There are no request fields for version, contract, expected digest, arbitrary output path, command, argv, interpreter, environment, toolchain, signer or acceptance flags.

The first adapter retains the pipeline CLI/workflow name for compatibility. Proposed local trusted interface: scripts/run-pipeline REGISTERED_NAME --request ABSOLUTE_REQUEST_FILE; this is a new interface to implement, not an existing working command. Local developer invocations without trusted authority context produce diagnostic results only. Existing regression-history-smoke remains explicitly corpus-validation, never behavioral-regression or operation qualification.

Promotion TSV exact columns:

    operation_id version generation state contract_repository_id contract_commit contract_path contract_sha256 qualification_sha256

state is candidate|qualified|active|revoked. Only trusted promotion identity writes it. Active generation must not decrease; execution resolves exactly one active nonrevoked version. aliases.tsv columns are alias,operation_id (tab separated); ambiguous/colliding aliases fail registry qualification. Human phrase interpretation selects the exact entry and permitted inputs; it never generates a recipe.

Each operation TOML record has ONLY:

- schema_version=1; operation_id; version; adapter enum (kitchen-transfer-generation|crystal-nativeactivity-build); intent_kind enum (generate-script|build-apk); summary; acceptance_scope; excluded_claims.
- source: repository_id, canonical_repository, allowed_refs, default_ref, required_paths. Ref selection is resolved once to commit/tree through the verified canonical remote. Branch membership/publishability checks are independent of the supplied hash. Detached arbitrary foreign/local objects cannot qualify.
- inputs: each name has type enum string|integer|enum|enum-list|source-ref, required boolean, optional explicit default, allowed values/pattern/limits. No executable template syntax.
- implementation: owner repository ID, exact commit, adapter entrypoint, required regular-file blobs, qualification record digest.
- dependencies: role, repository/artifact identity, immutable commit or content digest, verified runtime/tool paths; separate compiler and linker stages, NDK revision and exact ICK evaluated revision/gap/qualification.
- environment: build_host_profile, target_profile, ABI, runtime, uid/privilege class, permitted network acquisition endpoints, declared environment allowlist.
- effects: finite enum set, trusted output-root policy, artifact names/types, no caller absolute destination; user source/dirty work read-only.
- checks: fixed required check IDs, owner/validator revision and contract digest, observable postconditions, evidence class, timeout/output limits. A candidate cannot remove a required child or replace it with a no-op.
- bounds: per-stage seconds, run seconds, scratch bytes, artifact bytes and captured stdout/stderr bytes.
- rerun: effect class (pure-artifact|external-mutation), idempotency rule and state reconciliation rule.
- promotion: verifier identity, allowed artifact channel, required scope and prior-accepted-artifact source; Android package/lane authority references. Caller cannot replace these.

Qualification verifies the complete dependency graph before execution. Fixed adapters map these data fields to ordinary calls; executable invocation definitions belong to promoted implementation, never the request.

Result schema v2 has required fields:

- schema_version, request_id, request_sha256, run_id, attempt, operation_id, operation_version, registry_generation;
- control {repository_id, commit, executable_sha256, deployment_identity}; qualification_sha256; contract_sha256;
- source {repository_id, canonical_repository, requested_ref, resolved_commit, tree, material_blob_digests};
- implementation and dependency identities; observed build_host, target_profile, ABI; declared event metadata separately from observed checkout;
- stages[]: check_id, required, evidence_class, state, start/end, actual executable digest, exit/signal, output digests, observation/receipt digests; missing stages explicitly NOT_RUN;
- artifacts[]: name, type, size, sha256, scope, state (diagnostic|accepted), verified retrieval locator; Android package/version/certificate/native payload identities;
- status enum PASS|FAIL|BLOCKED|INTERRUPTED; acceptance_scope; excluded_claims; blockers[] with stage/code/detail; promotion {state, decision_sha256, trusted workflow/release identity}; timestamps.

Stage states are PASS|FAIL|BLOCKED|NOT_RUN|INTERRUPTED. UNKNOWN evidence maps to BLOCKED with reason, never PASS. Unsupported optional evidence remains NOT_RUN in excluded scope. All required stages must PASS for operation PASS. A failure is retained even if cleanup or later observation succeeds. Logs are bytes, not receipt syntax: a printed PASS cannot authorize anything.

A receipt must be fetched from the trusted run identity and verified against its protected release and immutable output digests. A SHA-256 field alone provides integrity, not origin or authorization. For artifacts handed outside GitHub, use a trusted publisher signature/attestation over the decision+artifact manifest and verify that identity, not candidate-supplied keys.

## Execution details

Preflight parses the WHOLE request/contract, verifies active qualification, resolves allowed source refs once, materializes into fresh isolated paths, confirms required blobs/tool digests/target, and checks mandatory capabilities before operation effects. Cheap private logging/scratch and authorized bounded fetches are preparation, not application mutations.

Use observed Git object identity, not GITHUB_SHA assertions. Remove inherited GIT_*, replacement refs, global/system config, include directives, credential helpers and URL rewrites; use explicit Git paths and reviewed acquisition credentials in the acquisition process only. Environment is allowlisted; PATH resolves only pinned tool directories. Do not inherit PYTHONPATH, LD_PRELOAD, shell startup settings or caller compiler overrides. Mirror/proxy configuration is explicit trusted deployment data, not a arbitrary URL rewrite.

Missing executable, absent source, source not published, missing authentication, insufficient API capability, unavailable transport, insufficient space, unavailable signer and unavailable qualified implementation receive distinct BLOCKED codes. No automatic install/bootstrap unless a qualified acquisition step is part of the operation and already authorized. Phones/tablets remain runtime consumers.

Run identity combines authenticated request identity plus a supervisor-generated unique attempt ID; GitHub run_id and run_attempt are recorded, not used alone for directory uniqueness. Identical request ID + identical bytes returns the existing status/result; same ID + different bytes rejects. Explicit retry creates a new attempt referencing the earlier attempt. Generation/build reruns use new isolated scratch. Future external-mutation operations must query canonical external identity before retry; accepted-but-unverified transfer cannot be resent blindly.

Journal admission and each stage atomically outside worker scope. On timeout/interrupt kill the whole worker process group, preserve logs/partial outputs as diagnostic, and never accept stale files. If a process dies before final receipt, the supervisor records INTERRUPTED; a journal without terminal decision cannot authorize delivery.

Outputs are written to fresh staging, checked as regular files (no escaping symlinks/hardlinks), sealed by copy to supervisor-owned storage, and rehashed there before verification and publication. The publisher uploads those same bytes without rebuild. No check-then-execute on writable candidates. Do not reset/clean/delete the user's checkout or reuse fixed clone destinations. Explicit size/runtime caps terminate the run, not silently truncate evidence and call it green.

A fixed procedure is not a reproducible artifact claim. Generator qualification compares exact output bytes for identical inputs. APK reproducibility requires two controlled clean builds and actual byte comparison, recorded separately. External API state, tool/runtime environment, timestamps and signing metadata can change outcomes.

## Initial operations

### A: kitchen-transfer-script

Aliases: generate-transfer-script, generate-repository-transfer-script. Intent is generate-script. It never transfers a repository.

Inputs: source_owner, repository, destination_owner, expected_login (required validated GitHub name strings), expected_repository_id (required positive integer), target_context (enum of actually qualified runtime profiles; no inferred default). Output name is derived by the recipe; no caller output path. Canonical implementation starts from Kitchen's maintained descriptive generator and next versioned transfer candidate, not copied into FP.

Effects: generation and fixture execution in private scratch, return one descriptive script and its identity manifest. No live GitHub token in the worker, zero real transfers. Qualification runs the actual delivered bytes twice from unrelated fresh homes/directories including spaces and quotes, under disposable API fixtures. Independently record every API attempt/method/endpoint/owner, numeric repository ID and visibility. Verify parent-shell survival, rerun/accepted-but-unverified state, personal/organization destination differences, download/partial payload, missing executable/auth/network, collisions and wrong identity.

Current generator takes four bound names and copies candidate 1.sh. It lacks expected_repository_id binding; its current mock hides the personal-account regression. It is not qualified by nine green cases. Repair the existing owner, preserving old numbered evidence. Source-handoff cannot be borrowed as its authorization adapter.

Current POSIX transfer code is inspected legacy, not covered by the pre-Grease source-test exception. New maintained shell adapter/code uses Grease under a qualified runtime. If that runtime/acquisition cannot be materialized, leave this operation unqualified with the exact blocker; do not silently broaden the POSIX exception. No unrelated fleet migration is required.

### B: crystal-miro-a1-apk

Alias: build-crystal, only once its version is promoted. Intent is build-apk, acceptance_scope=android-native-package; excludes install/launch/replacement/visual/physical unless their own evidence is present. Plain “Build Crystal” chooses this profile only after promotion makes it the explicit registered default. Before that, no active operation is a precise blocker.

Inputs: source_ref (optional, default is the promoted recipe's approved Crystal branch; resolve once), materials (enum-list halite|quartz|bismuth, default all three). The operation fixes MIRO A1, armeabi-v7a, NativeActivity C/Lua, direct packaging and test lane. Package IDs, signer, version policy, runtime, renderer and build lane are not caller overrides. Distinct targets or production release need separately qualified operations.

Compose application-owned compile/link path -> Android-NDK direct packager -> finished-artifact inspection -> AICI producer gate -> Cat Food artifact/target validator -> trusted accepted-artifact export. Build host is qualified hosted Linux; MIRO A1 is the artifact/runtime target, not the compilation host.

Preserve C/Lua/raylib application work; an existing cpp directory name is not evidence of C++ compilation. Declare each compile/link stage as NDK or qualified ICK with exact evidence. Pin raylib, Lua, NDK, build-tools, platform jar and all other material inputs. SDK apksigner's JRE dependency is permitted tooling; no Java/Kotlin application generation, Gradle packaging or d8 fallback.

The new Android-NDK packager candidate has useful real code, but qualification gaps remain: expected fingerprint and several tool paths come from caller environment; latest build-tools selection exists; final output is created before all checks and old output is removed; resources are not a generic input; hasCode=false/native library metadata and actual ELF ABI are not independently fully checked; source_commit may be unknown/asserted. Fix these in its owning PR, not a Crystal-local packager. Staging must withhold invalid APKs from accepted export.

At Crystal 52b657b..., workflow now consumes the packager candidate and labels retained output candidate. However build-miro.sh writes app/src/<flavor>/jniLibs/<ABI>/libcrystal.so while workflow asks for build/native/<flavor>/armeabi-v7a/libcrystal.so and build/receipts/*. The same quartz manifest is used for all flavors. Those were source-inspected integration mismatches, not a newly reproduced CI result. At later 8233886ef135a8935d5351dcde9ed07763993288, build/output paths are reconciled, the new Python checker is removed, raylib is commit-pinned and native stripping/size receipts are added. However, the workflow removes the build-toolchain action and replaces the named canonical signer-verification step with literal true. The uploaded files are explicitly candidate output; this is not accepted-producer evidence. Lua still downloads without a content digest and fixed scratch deletion remains. Preserve those intermediate findings as superseded where appropriate and refresh the active branch before repair.

AICI must complete composition of #137/#158/#175/#199 under #207 in the new existing draft #209. Existing signer comparison and build-toolchain declaration checks are reused; declaration is not execution trace. Policy verifier's own generic cc bootstrap is an unresolved conformance dependency: deliver a qualified host verifier or an independently authorized bounded bootstrap exception, not a silently blessed generic compiler.

The inspected new composite candidate 8fb5dc6e... usefully checks finished APK metadata/signature/digest and checks selected policy/packager commits are ancestors of fetched main. It is not yet the selected authority boundary:
- any historical main ancestor can be selected; active qualified-version/rollback policy is absent;
- AICI_POLICY_REF is checked/reported but not compared to the actual action_root source bytes/HEAD;
- Git and executable lookup inherit ambient configuration/PATH;
- packager checkout identity and matching sidecar do not prove that packager executed; compile/link execution and Gradle/key-generation witnesses are absent;
- no-DEX is caller-disableable; prior receipt is optional and not authenticated as previously accepted;
- same package/version/signature/digest in a self-written sidecar is not trusted provenance;
- generic cc and mutable build-tools selection remain;
- this branch's diff contains no public-path hostile tests.

These are source-inspected gaps, not newly executed exploits. Main ancestry alone is not a qualification decision, and claimed protected-main status was not verified here. Preserve the useful validator rather than copying it into FP; bind it to the trusted release and add the missing mandatory checks/tests.

Cat Food #109 must add first-class APK coverage and consume the authenticated producer decision, rehash actual bytes and verify MIRO target identity. Existing android/check.sh validates schema/declared stages but does not establish authenticated producer execution.

Crystal's original certificate differs from the proposed stable one. Key recovery is UNKNOWN per corrected issue #8, not proved impossible. Do not claim recovery, silently uninstall, rename to .inspect, or treat current proposal as authorized migration. Establish/approve a stable lane independently. Qualification requires accepted build A then distinct build B (different APK digest), same registered package/signer, nondecreasing version, and real replacement without uninstall. Fresh stable-lane update proof does not prove compatibility with the original differently signed install. Retain that migration incident separately.

## Public-path acceptance suite

Required tests enter through dispatch parsing -> bound execution -> result/promotion, with trusted expected outcomes outside candidate write access. Test both dispatch adapters and trusted local engine; unit helpers alone are insufficient.

1. Positive A generation reaches the real Kitchen adapter, delivers deterministic bytes, executes those exact bytes twice against disposable API fixtures, and makes no live mutation.
2. Positive B performs real compile/package/inspection, all mandatory gates and exact-artifact export. Omitted preparation or one missing child rejects before accepted export.
3. Unknown operation, extra command/argv/interpreter/compiler/env/policy fields, unqualified adapter and rollback version fail before operation effects.
4. Alter request-branch runner, pipeline, workflow, checker or non-request tree; trusted processor rejects. Change workflow_dispatch ref; it cannot become accepted execution. Both valid routes produce equivalent identity contracts.
5. Wrong-origin/unpublished/foreign source, wrong allowed branch, inherited GIT_DIR/config/replacement objects, PATH shadowing and forged GITHUB_SHA cannot change observed identities.
6. Mutate recipe/contract/source after qualification and output after validation. Immutable snapshots or mismatch reject; no publishable substituted bytes.
7. Missing executable/auth/API permission/network have different diagnostics and zero operation mutations.
8. Skip/fail required test, replace it with true or a PASS printer, forge receipt text in stdout, omit result file, forge validator identity: no accepted result.
9. Stale source/artifact/target/acceptance-scope receipt cannot pass. Host/emulator cannot grant physical acceptance.
10. Real NDK compilation followed by Gradle packaging fails. Missing/wrong signer, edited expected registry, unauthorized package-ID change, uninstall workaround and version rollback fail. Correct stable direct path passes.
11. Duplicate request, explicit rerun, interruption, concurrent isolated runs, timeout/output overflow and partial artifacts preserve prior attempts and dirty user work; no stale output is accepted.
12. Both distinct stable-lane builds are checked and replacement tested. No-op tests must be shown to disagree with independent expected observations.
13. Corpus validation, executable regression results and model-routing evaluation have separate names/status. No model download or inference in tests 1–12.

## Dependency-ordered ownership

1. FP #24/#26/#18: implement strict intake, registry/lifecycle, isolated executor, result authority and public-path hostile suite. Publish a concrete deployment configuration for separated request/author/promotion credentials. It is not active until configured and tested.
2. Kitchen #15/#24 plus AICI #205 and Cat Food #107: qualify the descriptive transfer generator and delivered artifact/runtime adapter. FP #2 only binds the qualified recipe. Repair personal-account/numeric-ID/rerun/byte-test gaps; preserve source-handoff scope.
3. Android-NDK #14 and existing draft packager: complete generic direct packaging/inspection/staging and qualified runtime dependency closure. No local Crystal substitute.
4. AICI #207 and existing draft #209 complete composition of existing child owners #137/#158/#175/#199, plus independent authority and producer publication decision. Process witnesses must be recorded outside candidate control. This can develop alongside steps 1–2.
5. Cat Food #109/#89: APK classification, trusted decision consumption, target/digest validation and stable delivery interface. Do not copy AICI checks.
6. Crystal #8 and its active branch: reconcile direct-packager integration, pinned C/Lua inputs, compile/link declarations, stable-lane authorization and two-build update test. Preserve application and behavior work.
7. FP #28/#16: register B only after owner qualification receipts exist. Execute through both public routes and return accepted artifact by digest. Lua/bootstrap and other adapters remain visible/unqualified until separately completed.

No execution-only Earth/Moon job is ready merely because this design exists. Authoring jobs may create the missing programs; execution jobs must receive freshly materialized qualified release IDs and dependency receipts.

## End-to-end “Build Crystal” acceptance

Given promoted operation crystal-miro-a1-apk and an authorized stable package lane, the driver sends only the registered name, request ID and permitted data. Trusted intake resolves the approved Crystal ref exactly once, verifies source/recipe/policy/tool snapshots and required capabilities, then executes the registered C/Lua native build and canonical packager. Independent checks inspect actual APK bytes, enforce producer policy and prior version/signer identity, and Cat Food checks digest/target coverage. The publisher returns only the sealed verified APKs and result manifest.

The driver reports source/version/APK digests and the actual acceptance scope. It does not invent commands, edit policy, switch package ID/signer, substitute Gradle, repair a failed build within the same attempt, or claim pinch/wireframe/physical correctness without separate evidence. Missing qualification or mandatory evidence returns a precise blocker and retained failed attempt, not an alternative APK.
