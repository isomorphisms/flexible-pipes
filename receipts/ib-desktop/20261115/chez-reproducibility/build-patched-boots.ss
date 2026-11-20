;; Scheme-only instantiation of Chez10.4.1 s/build.zuo bootall steps.
;; Does not invoke configure, Make, Zuo, a C compiler or a linker.
(import (chezscheme))
(let ()
(define root "/workspace/scratch/2990a35631ac/chez-repro-probe")
(define source (string-append root "/csv10.4.1"))
(define build (string-append root "/boot-regeneration"))
(define s (string-append source "/s/"))
(define out (string-append build "/s/"))
(define base-files
  '("library" "prims" "mathprims" "record" "5_1" "5_2" "5_3"
    "strnum" "bytevector" "5_4" "5_6" "5_7" "event" "4" "front"
    "foreign" "6" "print" "newhash" "format" "date" "7" "cafe"
    "trace" "engine" "interpret" "cprep" "cpcheck" "cp0" "cpvalid"
    "cptypes" "cpcommonize" "cpletrec" "inspect" "enum" "io" "read"
    "primvars" "syntax" "costctr" "expeditor" "exceptions" "pretty"
    "env" "fasl" "vfasl" "pbchunk" "reloc" "pdhtml" "strip" "ftype" "back"))
(define compiler-files '("cpnanopass" "cpprim" "compile" "cback"))
(current-directory out)
(source-directories (list out s (string-append source "/unicode")))
(library-directories
  (list (cons (string-append source "/nanopass") out) (cons s out)))
(reset-handler (lambda () (exit 1)))
(base-exception-handler
  (lambda (condition)
    (display-condition condition (current-error-port))
    (newline (current-error-port))
    (exit 1)))

;; Preamble order and subset exactly from compilation-preamble-target.
(for-each
  (lambda (name)
    (printf "preamble=~a\n" name)
    (let ([output (string-append out name ".so")])
      (parameterize ([subset-mode 'system])
        (compile-file (string-append s name ".ss") output))
      (load output)))
  '("cmacros" "priminfo" "primvars" "env" "setup"))

(printf "preamble=nanopass\n")
(parameterize ([compile-imported-libraries #t])
  (compile-library (string-append source "/nanopass/nanopass.ss")
                   (string-append out "nanopass.so")))

;; Official default make-final-compile-script settings.
(optimize-level 3)
(debug-level 0)
(fasl-compressed #t)
(generate-inspector-information #f)
(run-cp0 (lambda (cp0 x)
           (do ([index 2 (fx- index 1)] [x x (cp0 x)])
               ((fx= index 0) x))))
(collect-trip-bytes (expt 2 24))
(collect-request-handler (lambda () (collect 0 1)))
(collect 1 2)

(for-each
  (lambda (name)
    (printf "boot-source=~a\n" name)
    (collect 1 2)
    (compile-file (string-append s name ".ss")
                  (string-append out name ".ta6le") 'ta6le))
  (append base-files compiler-files))
(apply #%$make-boot-file
       (string-append build "/boot/ta6le/petite.boot") 'ta6le '()
       (map (lambda (name) (string-append out name ".ta6le")) base-files))
(apply #%$make-boot-file
       (string-append build "/boot/ta6le/scheme.boot") 'ta6le '("petite")
       (map (lambda (name) (string-append out name ".ta6le")) compiler-files))
(display "scheme-only-boot-regeneration=PASS\n"))
