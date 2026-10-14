# Checked exporter intake attempt

Purpose: exercise both maintained intake adapters without publishing a request
branch or claiming signed production admission. The immutable Git object fixture
resolves the same request bytes, source digest and cached verified execution.

The type sketch is `tuple[bytes, dict[str, object]]` for intake and
`dict[str, object]` for foreign metadata. Ithon's foreign `engine.digest(raw)`
call is inferred as object, so even a string conversion on the left operand
failed checking with `comparison operands need statically known types`.
The retained `1-foreign-digest.pi` isolates that rejected attempt. The maintained
qualification converts both foreign digest values to string before comparison.
No unchecked or Python fallback was introduced. Source checking now passes;
isolated local execution still correctly refuses the single-UID namespace.

The TLS delivery extension exposed the same precision issue for an inline
`hashlib.sha256(delivered).hexdigest()` comparison. Its maintained version names
the digest with a `str` annotation before comparing it. The delivery fixture also
required an explicit `dict[str, object]` annotation for copied foreign input
metadata. Both failed checks were caught before execution and corrected in
checked Ithon, without changing any acceptance expectation.

The existing owner-selected checked Ithon controller is retained. This exercise
exposes foreign-return precision as language work; it does not certify Idriç
support or manufacture a runtime result.
