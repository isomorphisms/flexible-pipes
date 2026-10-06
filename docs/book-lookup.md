# Book lookup through Kitchen

Flexible Pipes does not own AbeBooks or Internet Archive URL construction.

Kitchen owns the provider semantics:

- `tasks/book-lookup/abebooks.py`
- `tasks/book-lookup/internet_archive.py`

This branch pins the exact Git blobs in `registry/book-lookup-kitchen.json`.
The two Flexible Pipes wrappers verify:

1. `KITCHEN_ROOT` is a Git checkout whose origin is
   `isomorphisms/kitchen`;
2. the selected path at Kitchen `HEAD` has the pinned Git blob identity;
3. the current working-file bytes hash to the same Git blob;
4. only then is that exact Kitchen file executed with `python3`.

No AbeBooks search URL, Internet Archive query, favorites collection, or
`/details/<identifier>` construction is duplicated in Flexible Pipes. A
Kitchen edit therefore fails closed here until this registry and the wrappers
are deliberately repinned.

## Pipelines

AbeBooks:

```sh
KITCHEN_ROOT=/path/to/kitchen \
BOOK_TITLE='Citizen of the World' \
BOOK_AUTHOR='Maria Montessori' \
python3 scripts/run-pipeline book-lookup-abebooks
```

ISBN lookup:

```sh
KITCHEN_ROOT=/path/to/kitchen \
BOOK_ISBN=9780199207640 \
python3 scripts/run-pipeline book-lookup-abebooks
```

Internet Archive:

```sh
KITCHEN_ROOT=/path/to/kitchen \
BOOK_TITLE='Citizen of the World' \
BOOK_AUTHOR='Maria Montessori' \
python3 scripts/run-pipeline book-lookup-internet-archive
```

For a network-free inspection of the exact Archive queries:

```sh
KITCHEN_ROOT=/path/to/kitchen \
BOOK_TITLE='Citizen of the World' \
BOOK_AUTHOR='Maria Montessori' \
IA_PLAN_ONLY=1 \
python3 scripts/run-pipeline book-lookup-internet-archive
```

The existing pipeline runner records stdout, stderr, exit status, command argv,
and hashes in its normal receipt. The provider response is therefore preserved
as run evidence rather than being treated as timeless data.

## Ownership boundary

Kitchen remains the source of pasteable/provider-specific scripts. Flexible
Pipes owns the repeatable invocation and receipts. If another caller needs book
lookup, it should call the Kitchen script or these pinned FP wrappers; it should
not reconstruct provider URLs from memory.
