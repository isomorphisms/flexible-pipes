# SUN SUBRIEMANNIAN-01 execution

The `subriemannian-01` pipeline compiles the Idriç Kitchen producer, builds the
geometry/test/figure/AICI programs through Idriç's existing Chez runtime, runs
the actual mathematical tests, regenerates the figure, and invokes independent
AICI acceptance as a separate required stage. Any nonzero stage exit fails the
pipeline. The JSON file is the existing FP runner's external interface.

The producer owns source and compiled-artifact receipts. AICI hashes and executes
the actual Chez compiled artifact directly, rather than trusting source text or
the generated launcher. This is Linux host evidence, not direct-x86-backend or
Android evidence. The explicit user's Idriç/runtime selection governs this task;
no C consumer compiler, RefC, Java, or generated-C application path is used.

Use the subriemannian repository's `Reproduce.idric` controller and immutable
dependency pins to supply the absolute parameters and compiler environment.
An existing artifact directory is rejected so a run cannot inherit old success.
The FP receipt records each stage's arguments, exit, stdout and stderr hashes.
This bounded implementation does not claim to fix FP's general historical
job-submission/non-bypassability obligations.
