# Published-source host fixture evidence

The retained-source pipeline ran both required stages successfully on Linux
x86_64 at 2026-10-06T17:35:04Z. This directory preserves its existing runner
receipt, the Kitchen fixture receipt and the semantic output streams. Inputs:

| Owner | Exact executed revision |
| --- | --- |
| IB | b4d93c47327f112433b90c0a77a00b3ddcba0af4 |
| Kitchen | b93dcda3e0fdfea81d565ffda5daf330673b8ac8 |
| AICI | f46158ca3a0ba231acf7694d84937022d71b29f8 |
| Flexible Pipes | 3f131200333967e943b796d371a6a14e4aa66c80 |

The Grease native runtime came from dilapidated-shed/grease successful run
37476471876, artifact 11419782646, wrapper source
9a874c4e082d26f21b2cc807b5553e7e19d5f590 and pinned implementation
5651cf97a1b5042f24f14112a7ade9a1518eb0bc. The executable SHA-256 is recorded in
fixture-receipt.tsv. Execution uses that implementation's compatibility applet;
consumer interfaces remain named Grease. ASAN_OPTIONS=detect_leaks=0 suppresses
the container's unsupported process/leak inspection, not a fixture assertion.
The PATH launcher delegates to the same verified native interpreter.

Only synthetic decoder/history data was inspected. Retained bytes/provenance,
conversation graph/references, repeatable rebuild, ordinary/private index policy
and refusal fixtures passed. AICI validates receipt consistency and host scope;
it does not infer an authenticated source, policy authority or physical evidence.
No live Drive/SDF transfer, private corpus, physical C67 or model call was run.
