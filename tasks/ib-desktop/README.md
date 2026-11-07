# IB Linux first wave

first-wave.txt is the immutable opening envelope, including the initial job
status text. The local opening commit 2bafcec71e7a73ff3d6d341690c294340a2a7493
preceded implementation. Its envelope hash, actual pipeline bytes, source/runtime
identities, exits and stdout/stderr hashes are retained in receipts. It is not
the current status of the implementation jobs.

Current state: SUN IB-X64-00/01/08 have an implemented bounded shared-core and
native qualification slice. They remain in progress. The integrated desktop
milestone and Android parity are not accepted. No merge/release/issue closure.
The opening text included an unverified human timezone; machine receipts use UTC.

Registered command pipelines use the existing scripts/run-pipeline controller,
whose Python implementation remains declared migration debt. No new Python
program or invented FP dispatch interface is introduced. Pipeline JSON is the
existing external FP schema; jobs, policy and evidence use ordinary text/TSV.

ib-linux-native-ick explicitly invokes Kitchen's ick-4.grease producer wrapper,
using pinned AI-CI ba3ff90023b09e525313793554edecf2141ff95b, ICK
c61e448251744a2f40ad743ebef1a027bdcd2f9d and GCC
6294f1d9e7536e5ffcde09d1528c918d63abfef5. Host bootstrap tools build ICK only;
the new C consumers use its qualified output. Package provisioning is separate.

ib-linux-shared-core invokes Kitchen 7.grease through native Grease/Ike: clean
38-case AI-CI oracle, three actual IB source mutations and clean restoration.
ib-linux-native-foundation invokes Kitchen 8.grease: 46-case actual generated
Chez program, ICK C ABI, native mutation/library-loss refusal, recovery and
Unicode-path relocation. Explicit source/path/runtime parameters are required;
there are no workspace-specific paths in these registrations.

The selected compiler currently refuses non-ASCII build roots because of its
executed Unicode-path defect (Idriç issue 138). That is distinct from successful
Unicode source text/FFI and relocation. Compiled Chez program hashes differed
across fresh output roots; byte reproducibility remains unresolved. Current
diagnostic native Grease runs disable LeakSanitizer inspection in the restricted
container (ASAN_OPTIONS=detect_leaks=0); this does not qualify its full producer
or release. Compiler/support producer debt is also still open.

Actual exact-trigger follower jobs and receipts live below followers/. They
refer to the maintained IB target catalog and distinguish this Linux build
container, MIRO A1 ARM32 and TAB_P10 ARM64. Accepted fixtures in AI-CI are only
admission tests and must never become actual device receipts. The parity wrapper
must remain blocked while the real Android obligations are pending/blocked.

Source branches/receipts are reviewable draft work; this registration is not an
active required default-branch desktop CI gate. SUN IB-X64-08 still owns hosted
Ubuntu provisioning, graphical/network/restart lanes and packaging/performance.
