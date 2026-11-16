# Immutable intake qualification

BC-FP01-S01 extends the existing checked Ithon controller and its test family,
as required by the recovered assignment. No new Python or shell control program
is introduced. The retained Python runner is moved unchanged from current main,
apart from the pre-existing unqualified-receipt fields.

## Types and effects

Request bytes → bounded operation-specific request; signed claims + route +
transport envelope → checked admission or named rejection. Git commit + request
blob → exact request bytes and immutable provenance. Materials + source objects
+ observed file digests → source preflight, without execution authority.

The central fixture operations have types `git(list[str], bytes) → str`,
`intake(bytes, str) → None`, and
`record(str, str, Callable[[], None]) → None`. Effects are confined to a new
disposable Git repository and output directory. No fixture runtime/qualification
declaration is independently admitted production material. Equality means exact
request bytes and source digest agreement, not model or worker equivalence.

## Failed attempts and corrections

Pinned checked Ithon d6e83969 rejected the initial fixture's concatenation of
foreign `stderr.decode()` with a string. The reduced `foreign-result.pi` preserves
that failure. Explicit `str(...)` conversion fixes it. It also rejected an
`object` used as a callable; the fixture now declares `Callable[[], None]`.
Foreign join results and receipt comparisons require explicit result types;
the operation-fields loop requires `list[str]`. An empty artifact list requires
an explicit element type. The missing `isinstance` import in the event adapter
was caught and fixed by actually loading the adapter through checked Ithon.

No checker was bypassed and no fallback language was used. Keep these explicit
foreign result boundaries; a future typed `CompletedProcess`/Path interface
could remove the casts. Acceptance for that language work is this actual
fixture checking and running without a dynamic foreign-value escape.

## Evidence boundary

Local source/admission/cache/delivery controls execute. Both full operation
qualifiers refuse this container's single-UID namespace with exit 2 before
worker effects. Eligible managed Grease closure and installed promotion remain
unreleased. Operation acceptance and authenticated ChatGPT origin are NOT_RUN.
