# Paired conversation-runtime producer

The historical attempt ran `build.pi` with the pinned checked Ithon entrypoint and a producer-local
qualified ICK executable and NDK r29 (29.0.14206865). Source/target dependencies
are in `SOURCE.tsv`. The exact ICK executable qualified during this slice is
SHA-256 `952d3ae0d5916e4d3030064d81cb193e1cbe1f8e706c556195f3d93d0bd42ba1`,
target `aarch64-linux-gnu`; qualification is not inferred from a model/device.

Historical arguments: `--source`, `--source-revision`, `--targets`,
`--targets-revision`, `--ndk`, `--ick`, `--ick-revision`, `--output`. File paths
were explicitly supplied, not discovered by guessing another machine's layout.
That output contained stripped A1/C67 executables, ELF inspection, separate
compile/link/strip logs, the attempted ICK diagnostics, exact hashes/sizes and a
completion marker. Failed/incomplete results remain visible without a marker.

CF-A2-S6 retains that implementation and its evidence. Direct CLI production
now rejects before creating output. Its old arguments allowed caller-selected
compiler/runtime/target bytes and asserted revision strings without admission.
`android-conversation-paired-build` is reserved in the existing registered
controller and both public adapters; it fails closed until the exact S2 plan,
S4 shared policy, S5 Kitchen procedure and S3 consumer are available. This is
not yet an admitted producer or a deployment. A caller cannot enable it by
supplying a target, executable, shell command or fixture PASS receipt.

Primary A1: Android ARMv7, NEON Float32, API floor 21. Paired C67: native AArch64,
API floor 21. This is an off-device producer; neither phone receives build tools.
The known ICK ARMv7 target gap and C67 NDK-header admission failure are retained
per stage. Source C is the explicit native implementation, not generated-C or
RefC from another language.

The original stripped artifacts are 10016 bytes (A1) and 11424 bytes (C67).
Their model/index input comes from takeout-svm's trained exports, which contain
the complete raw-text encoder. A warmed dot product cannot satisfy acceptance.

For physical acceptance on each named phone, first verify private executable
placement against Cat Food's exact device facts. Then invoke that device's
stripped `infer` binary with four arguments: model file, index file, UTF-8 query
file, repetition count. Use one repetition for the first in-process request and
1000 for an already-loaded measurement. An external cold process timer must
separately include launch. Retain device identity/ABI, executable/model/index
digests, result/vector and load/text/model/scoring times, resident/peak RSS and
the cold/warm boundary. Do not claim disk-cache-cold measurements without a
separate procedure. No physical run or installed runtime is claimed here.

The x86 parity runner in takeout-svm separately verifies vectors/scoring and
negative admission cases; it cannot stand in for the ARM implementation's
timings. A1 and C67 physical acceptance remain required pending jobs for these
exact artifacts. Cat Food's broad follower verifier is unavailable in this
producer environment, so no canonical follower-ledger acceptance is invented.
