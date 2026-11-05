# Amazon product lookup (candidate)

The named operation is \`amazon-product-lookup\`, registered in
\`pipelines/amazon-product-lookup.json\`. This is a checked-in **draft**
implementation of [issue #260](https://github.com/isomorphisms/flexible-pipes/issues/260)
and is **not** a claim that an Amazon price, stock, seller, delivery estimate or
Honda CR-V substrate/EPDM bond compatibility has been verified today.

## Responsibilities

- **Cat Food** supplies a verified stable \`az\` and \`grease\` runtime and
  canonical source checkout for host executions; on Android, it supplies
  packaged runtime products only, never a source/compiler bootstrap.
- **Kitchen** prepares the exact AZ invocation and refuses unverified
  executable bytes, mismatched Git source, missing Grease or changed argv.
- **AZ** performs \`search\`, \`link\` and optional \`price\`. Its search TSV
  includes unverified candidate ASINs; \`AZ_SEARCH_STATUS_FILE\` separately
  classifies candidate extraction, empty results, HTML drift and challenges.
  An \`az link\` result alone does not contact Amazon.
- **Flexible Pipes** chooses one checked-in operation, executes the existing
  \`scripts/amazon-az\` adapter, filters documented product roles, preserves
  stage streams/statuses and SHA-256 receipts, and emits a separate shopping
  verdict from the machine execution result.
- **ai-ci** must independently accept the exact shipped cross-repository
  revisions and their receipts. Hosted fixtures are not live service checks.

The product-fit ledger \`registry/amazon-product-fit.tsv\` records source
issue references and historical identity claims. For this example, it records
\`B000PEZ1L4\` as 3M Strip-Calk 08578 for an *interior door moisture barrier*
and \`B000CCFXYY\` as 3M Black Super Weatherstrip Adhesive 03602 for
*compatible exterior rubber weatherstrip bonding*. These are not substitutes.

Unknown year/trim/door/substrate/EPDM compatibility, seller, actual price,
availability and delivery remain unknown until independent current evidence
is supplied. No historical ASIN observation can qualify a current sale.

## Workbench invocation

With checkout/runtime identities established and \`KITCHEN_ROOT\` set to the
verified Kitchen checkout and \`CATFOOD_ROOT\` set to Cat Food's workbench
root (which provides \`bin/grease\`, \`bin/az\`, and \`az/bin/az\`):

\`\`\`sh
python3 scripts/run-pipeline amazon-product-lookup \
  --param action=link \
  --param target=B000CCFXYY \
  --param role=exterior-weatherstrip \
  --param tag=macguyver03-20

python3 scripts/run-pipeline amazon-product-lookup \
  --param action=link \
  --param target=B000PEZ1L4 \
  --param role=interior-moisture-barrier \
  --param tag=macguyver03-20
\`\`\`

For candidates, use \`action=search\`, \`target='Honda CR-V ...'\`,
\`role=unknown\`. For an AZ Creators/cached price observation, use
\`action=price\` with a named candidate ASIN; missing credentials or price
produce \`UNKNOWN_OR_UNAVAILABLE_CREDENTIALS\`, not an invented amount.

The *pipeline* receipt \`PASS\` means its command finished without an
execution error, **not** that the offer is qualified. The result's
\`status=PARTIAL\` means only the source-pinned command/link or candidate
result was established. \`status=BLOCKED\` indicates rejected source, ASIN,
tag, wrong repair use, non-executable dependency, challenged HTML, or missing
evidence. \`QUALIFIED\` is reserved for evidence of an actual inspected
listing and verified repair fit; this draft does not claim to produce that
status.

Affiliate disclosure: the operator of the \`macguyver03-20\` Associates
tag may earn from qualifying purchases; no assumption about self-purchases
earning commissions is made.

Each outer run's \`receipt.json\` preserves pipeline spec hash, commit, input
parameters, runner platform, stage argv/exit and raw stdout/stderr hashes.
The shopping stage also emits underlying AZ invocation command, exit, and
stream hashes. The underlying \`stdout.bin\` and \`stderr.bin\` are retained.
No private credential contents are intentionally placed in the receipt.

## Dispatch boundary and acceptance

The candidate \`.github/workflows/run-pipeline.yml\` accepts the same named
operation and parameters from \`workflow_dispatch\` and from a strict
\`pipeline-requests\` request-file branch. Both go to the same local runner
and checked-in pipeline specification, not an assistant reconstruction.

Until that workflow **and** the pipeline exist on the default branch and a
real dispatch produces a receipt, they are **not** a working public dispatch
surface. The proposed terminal dispatch, once deployed, is:

\`\`\`sh
gh workflow run run-pipeline.yml -R isomorphisms/flexible-pipes \
  -f pipeline=amazon-product-lookup \
  -f action=link -f target=B000CCFXYY \
  -f role=exterior-weatherstrip -f tag=macguyver03-20
\`\`\`

The exact PR candidate's integration harness is
\`sh tests/amazon-product-lookup.sh\` with preinstalled Cat Food/Grease,
pinned Kitchen/AZ checkouts and the declared environment. Its fake Amazon
search/price tests are **fixtures**, not current availability verification.
API 29/34, C67, and tablet runtime-only deployment require independent
packaged-binary tests; the host workbench checkout cannot be substituted for
device acceptance. No Java/Kotlin/Gradle or SQLite dependencies are introduced.
