;; Diagnostic only: expose uncompressed FASL differences; no normalization.
(import (chezscheme))
(fasl-compressed #f)
(load "/workspace/scratch/2990a35631ac/chez-repro-probe/compile.ss")
