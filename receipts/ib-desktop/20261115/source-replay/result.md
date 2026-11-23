# Shared-core current-compiler replay

November 15, 2026. The unmodified Kitchen `7.grease` source/evaluator recipe
completed with process exit 0 using the admitted Idriç
`5b55b4444fd66ab940cb8f9b74ee2f79043f148a` compiler material and the explicit
external native Grease invocation adapter. The exact command, source/material
identities, stdout, stderr and source snapshots are retained alongside this note.
The old `94dfd99bd` compiler archive was not used.

| Source variant | Typecheck | Aggregate evaluation | Intended rejection |
| --- | --- | --- | --- |
| Clean | PASS | True; all 38 named cases True | — |
| Ordinary tabs made disposable | PASS | False | ordinary-tab-is-durable=False |
| Non-BMP width reduced to one UTF-16 unit | PASS | False | utf16-boundary-4=False |
| Source-revision binding bypassed | PASS | False | changed-decoded-revision-refused=False |
| Clean recovery | PASS | True; all 38 named cases True | — |

All compiler/evaluator commands completed successfully as required by the
recipe; the deliberately broken source variants were rejected by their actual
semantic outputs. Original IB/oracle input hashes were checked unchanged, and
the recorded compiler, runtime, Grease, adapter and recipe hashes still match.

This establishes current material source typechecking/evaluator behavior only.
Generated native programs, C/FFI execution, byte reproducibility, desktop GUI,
network, disk recovery, Android runtime and physical devices remain separate.
No FP dispatch or Ike stage is claimed by this direct checking replay.
