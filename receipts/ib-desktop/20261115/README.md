# IB Linux qualification continuation — November 15, 2026

This records actual direct execution during SUN IB-X64-01 continuation. It is
not a Flexible Pipes dispatch or a new pipeline acceptance verdict.

## Shared source replay

Unchanged IB `2425d21d984de21e5b65ae0d2e09c586120239ee` and independent AI-CI
`4cc61d96c02ebeff408c33dc065a4a6948696967` passed all 38 source/evaluator
cases with the delivered Idriç `5b55b4444fd66ab940cb8f9b74ee2f79043f148a`
compiler. Three actual production mutations failed their intended semantic
cases, and clean recovery passed. Source and material hashes remained unchanged.
The exact native Grease invocation and scoped evidence are in `source-replay/`.
No C/FFI, generated-program, Android, or physical acceptance follows from this.

## Compiler material recovery

The original October compiler artifact had expired. The existing Cat Food
package workflow now retains its candidate and receipt artifacts for 90 days.
[Renewed run 43745214326](https://github.com/isomorphisms/catfood/actions/runs/43745214326)
passed both packaging and the independent fresh-host Intervals consumer.
Artifact `14173913711` carries the renewed compiler source
`94dfd99bd3e376507fedc8611053b7173b2519f0`; its tar SHA-256 is
`eb3111f978a45c20871205967f63f5b61f5a48a53c00f3b7174b9b9834c4b6e6`.
All 1,241 payload checks passed locally. These rebuilt archive bytes are distinct
from the October archive and must not inherit its digest.

## Compiled Chez reproducibility

The retained real NativeFoundationOracle Scheme source still matches its
October receipt: SHA-256
`6b446268379dd9a6eb74d04d4688149aba96a0bec327ee92b2204baa90baca55`.
Fresh compilation under the admitted Chez 10.4.1 runtime reproduces differing
compiled bytes. The experiments and their exact limitations are recorded in
`chez-reproducibility/RESULTS.txt`.

A scoped deterministic `current-generate-id` experiment does not completely
fix the result: Chez's whole-program expansion separately creates a random
program identifier with a direct `gensym`. With uncompressed diagnostic output,
the remaining real-consumer differences are that same identifier repeated four
times. Relative source filenames separately remove build-root path differences.
Uncompressed output is diagnostic evidence; it is not normalized production
acceptance or a change to the selected compile-program mechanism.

Compiled-byte reproducibility remains FAILED. The scoped generator is an
experiment, not an accepted compiler/runtime change. Native C/FFI execution with
the renewed material, final packaging, desktop GUI/network/recovery, Android
followers, and physical-device work remain separate unfinished obligations.
