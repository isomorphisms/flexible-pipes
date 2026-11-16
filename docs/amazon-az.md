# Amazon product lookup through AZ

Flexible Pipes owns repeatable invocation and receipts for the user's local AZ
Amazon backend. Kitchen owns the provider-facing command itself.

The canonical AZ source repository is `Ashtray-Archer/az`. The former
`isomorphisms/az` location must not be used as a fallback. Phone execution
uses the installed `$PREFIX/bin/az` backend through Grease.

The exact Kitchen helper is pinned in
`registry/product-lookup-kitchen.json`:

```
tasks/product-lookup/amazon-az.sh
blob d2c71bdbb64467d063b6b97c2727880a7931ad11
```

Before execution, `scripts/amazon-az` verifies:

1. `KITCHEN_ROOT` is a Git checkout whose origin is
   `isomorphisms/kitchen`;
2. the selected path at Kitchen `HEAD` has the pinned Git blob identity;
3. the working-file bytes hash to that same blob;
4. only then is the exact Kitchen helper executed.

Flexible Pipes must not reconstruct an Amazon URL or bypass AZ when this
checked-in command pipeline is being used.

This pipeline uses `scripts/run-pipeline-legacy.py`. Its receipt reports
caller-supplied command execution with `qualified_operation: false`; it does
not grant registered-operation acceptance.

## Search

```sh
KITCHEN_ROOT=/path/to/kitchen \
AZ_COMMAND=search \
AMAZON_QUERY='MIRO A1 LCD digitizer screen assembly' \
python3 scripts/run-pipeline-legacy.py amazon-az
```

`AZ_COMMAND=search` is the default, so it may be omitted.

## Link

```sh
KITCHEN_ROOT=/path/to/kitchen \
AZ_COMMAND=link \
AMAZON_TARGET=B0ABC123 \
python3 scripts/run-pipeline-legacy.py amazon-az
```

## Price and history

Use the same `AMAZON_TARGET` input with `AZ_COMMAND=price` or
`AZ_COMMAND=history`.

## Doctor

```sh
KITCHEN_ROOT=/path/to/kitchen \
AZ_COMMAND=doctor \
python3 scripts/run-pipeline-legacy.py amazon-az
```

The pipeline runner's normal receipt captures command execution, output, exit
status, and hashes. The Amazon response remains run evidence rather than
timeless repository data.

## Ownership boundary

Kitchen owns the exact Grease/AZ invocation and the pasteable user procedure.
Flexible Pipes owns repeatable command execution and receipts. Product
compatibility analysis belongs above this layer; a caller should use AZ for the
Amazon candidates and links, then verify that the candidate actually fits the
requested device before recommending purchase.
