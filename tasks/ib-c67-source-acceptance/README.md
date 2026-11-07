# FP-controlled host acceptance for ICU #35 / IB #152 / #153

This task stages existing implementation candidates through an actual Flexible Pipes pipeline. It does not claim their earlier GitHub commits originated inside FP. It pins exact source heads, validates the human-visible job file, runs independently pinned AI-CI source mutants, compiles Ike using qualified ICK and runs Ike recipes with a versioned execution receipt.

The Ike graph builds actual native ICU, canonical appendfat, verified Arena reader, and the PFD host tests from exact immutable pins. Rejection controls include non-HTML, malformed metadata, stale generations, hash mismatch and legacy v1 admission, with separate AI-CI readback.

The runner is GitHub Ubuntu x86_64. HTTP and HTTPS use actual ICU native socket/TLS but an explicitly fake Android app_process/Shizuku bridge; host PFD tests use Linux anonymous pipes rather than real Android Binder. Android ABI cross-build evidence remains in separate IB #152/#153 workflows. Physical C67, Android direct Idriç DEX, real Binder/PFD and GUI are NOT_RUN.

No Kitchen executable handoff or exact physical host-target preflight is claimed here. Kitchen's source-handoff/device task is a separate required stage before phone delivery. Passing these stages supports host code acceptance, not merged browser deployment or physical-C67 acceptance. FP receipts and independent AI-CI evidence remain subject to actual merge authority and repository-specific rules.
