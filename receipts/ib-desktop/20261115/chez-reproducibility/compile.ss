;; Disposable runtime experiment, not an Idric compiler patch.
;; Usage: scheme --script compile.ss MODE KIND INPUT OUTPUT UNIT CLOSURE_SHA256
;; MODE = raw | scoped | constant-mutant; KIND = program | library.
(import (chezscheme))

(define arguments (cdr (command-line)))
(unless (= (length arguments) 6)
  (error 'probe "expected MODE KIND INPUT OUTPUT UNIT CLOSURE_SHA256"))
(define mode (list-ref arguments 0))
(define kind (list-ref arguments 1))
(define input (list-ref arguments 2))
(define output (list-ref arguments 3))
(define unit (list-ref arguments 4))
(define closure (list-ref arguments 5))
(unless (and (= (string-length closure) 64)
             (for-all (lambda (c) (or (char<=? #\0 c #\9)
                                     (char<=? #\a c #\f)))
                      (string->list closure)))
  (error 'probe "closure identity must be a lowercase SHA-256 hex digest"))
(unless (member mode '("raw" "scoped" "constant-mutant"))
  (error 'probe "unrecognized mode" mode))
(unless (member kind '("program" "library"))
  (error 'probe "unrecognized kind" kind))

(define original-generator (current-generate-id))
(define generator
  (let ([counter 0])
    (lambda (symbol)
      (let* ([index counter]
             [namespace (if (string=? mode "constant-mutant")
                            '("UNSAFE-CONSTANT")
                            (list "idric-chez-probe-v1" unit closure))]
             [result (if (string=? mode "raw")
                         (original-generator symbol)
                         (gensym (symbol->string symbol)
                                 (format "~s" (list namespace index))))])
        (set! counter (+ counter 1))
        (fprintf (current-error-port) "generated-id=~s\n"
                 (list index (symbol->string symbol)
                       (gensym->unique-string result)))
        result))))

;; Exactly the relevant original compiler settings, plus the isolated generator.
;; Do not reset the runtime's gensym or current-generate-id outside this extent.
(parameterize ([optimize-level 3]
               [compile-file-message #f]
               [current-generate-id generator])
  ((if (string=? kind "program") compile-program compile-library) input output))

