# Venn compiler diagnostic regression

The existing Idriç attempt is `models/CollegeVenn.idric`. This recovery does not
replace it: Idriç still checks the semantic model and emits the evaluator.
The pinned compiler failed to load Prelude and returned zero; the archived
positive and negative logs therefore establish neither proof acceptance nor
semantic rejection.

This checked-Ithon adapter test exercises the inherited Python checker directly.
It cannot establish Idriç compilation, execution, or movie correctness. Its
foreign boundary is the existing Python function receiving a subprocess result.
The invariant is that zero exit status accompanied by a compiler error must
never count as a successful positive control. A clean zero result must pass;
nonzero status or an error diagnostic must fail. No fake compiler is used.

The source-less diagnostic is retained from workflow run 38344724204,
artifact 11788830525, SHA-256
`6df073d3576b3a61144b38fdaa0fb3f7619233f7bcb155191df95a76ae47e808`.
The tests also check that a failed attempt invalidates prior success records.
The real compiler, imported modules, all rejection cases, generated output,
and movie require their separate pipeline run.
