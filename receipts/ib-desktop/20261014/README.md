# Executed first-wave evidence — 2026-10-14 UTC

Source execution commit: FP 69a4436c5a8c5b990a662a04f7e66c2d618d2aad.
Receipt publication is a later data-only commit; it does not relabel execution
as a different source revision. Initial local opening commit 2bafcec precedes
implementation and is historical local provenance, not a published branch head.

| Input | Exact revision |
| --- | --- |
| IB | 2425d21d984de21e5b65ae0d2e09c586120239ee |
| AI-CI | 4cc61d96c02ebeff408c33dc065a4a6948696967 |
| Kitchen | 1a1c31236947ed3df50e94342276d1ae1280f986 |
| Idriç bundle source | 94dfd99bd3e376507fedc8611053b7173b2519f0 |
| ICK source | c61e448251744a2f40ad743ebef1a027bdcd2f9d |
| GCC source | 6294f1d9e7536e5ffcde09d1528c918d63abfef5 |
| Native ICK producer recipe | AI-CI ba3ff90023b09e525313793554edecf2141ff95b |

Target: disposable Ubuntu 24.04.3 Linux x86_64, kernel 6.18.44, eight CPU quota,
8 GiB memory limit. This is not the Hetzner, Void, graphical desktop, Android
emulator, MIRO A1 or TAB_P10 target. Native graphical/network/physical acceptance
was not performed. Compiler/Grease artifact provenance remains bounded as below.

Final source run: ib-linux-shared-core-20261014T125525.953909Z (the exact directory
name is retained below runs/). PASS: clean 38-case oracle, disposable-tab,
UTF-16-width and source-binding mutations rejected for their intended cases,
and clean restoration. Final native run:
ib-linux-native-foundation-20261014T125525.948815Z. PASS: actual 46-case generated
Chez program, ICK C FFI, compiled C mutation rejection, missing-library failure,
restoration and launch after relocation into a Unicode/apostrophe directory.
No fallback browser implementation or producer-owned expected assertion list.

The final-native/ and final-core/ directories retain input hashes, exact source
heads, named results, refusal/recovery outputs, generated-program source, ABI
inspection, dependency results, Ikefiles and Ike receipts. The compiled Chez
program digest is bba174481696726c34cfded5f9d05b7ce00b17eed1274952bbca3f6893cbf704.
Its ICK library is 7dcbba3a9a6b0e90a21f356991edd82292a90bd9691b657a48caddddcab4edc7.
The program/runtime closure was executed locally; no release artifact is claimed.

The independent follower verifier was compiled from the actual AI-CI source by
qualified ICK with -fno-link-libatomic -std=c17 -Wall -Wextra -Werror -pedantic -O2.
Verifier SHA-256: 31df9890f4361171db0f582e97d43ba141ecff9ad19c4bd11a8097d6363847dc;
source SHA-256: 86c9ad14d74cf9a5051290f9f228a6e984ec8c8c7cf21ab249f86e4d8bb1b4fb;
parity wrapper SHA-256: 83fefdf4f4a2563d067b803158b01ca18770259098a50447498d4e6470ff37a8.
This independent admission check ran directly: accepted Linux, then exit 4 with
shared-core-parity=BLOCKED for the phone. The ledger and pending table are retained.
Synthetic acceptance fixtures belong to AI-CI only; no fake device receipts are
present in the real follower ledger.

All opening/package/bootstrap/failure and successful FP runs are retained below
runs/. Large compiler stdout streams are gzip-compressed without timestamps;
decompression reconstructs the exact stdout.bin bytes whose hashes appear in
their original receipt. All other captured streams retain their original bytes.
The initial ICK build timed out at thirty minutes; the same pinned build resumed
with six workers, qualified -O0/-O2 and rejected its division mutant. Package UID
and cache failures, native Grease dialect/quoting failures, and the compiler's
Unicode-path failure were not erased. Workspace-specific package profiles are
observed receipt inputs, not reusable pipeline registrations.

Native Grease diagnostic artifact SHA-256
7e31cd05b7a9d8fb2a4a9e003a7f3fcb0159138506d17f0fb28da8cbe22aa85c,
source gitlink 5651cf97a1b5042f24f14112a7ade9a1518eb0bc. ASAN_OPTIONS=detect_leaks=0
disables LeakSanitizer inspection in this restricted container; full native
Grease producer/release acceptance is not claimed. Ike artifact SHA-256
ba29bda0300da0ada3795df96c008bb47f12f476aab071e563f0811c3e736569,
source 71178c348dd4621bd999ebdb6b0b60bac03fc85d. Idriç tar SHA-256
0be57deab9410e8d4c09c7198bf7e8ee0ec3e24121f76640147efa4a53d120da;
Chez 10.4.1. Compiler/support producer toolchain debt remains open.

Two fresh consumer output builds had identical generated Scheme/launcher/C
library bytes but different compiled Chez program hashes. Byte reproducibility
and fresh-host compiler qualification are not accepted. Non-ASCII build roots
also remain blocked by https://github.com/isomorphisms/Idric/issues/138; Unicode
program text/FFI and runtime relocation have separate successful evidence.

SUN IB-X64-00/01/08 are IN_PROGRESS / PARTIAL_IMPLEMENTATION. GUI, HTTP(S), disk
restart, deliberate worker/renderer termination, Pensieve workbench and physical
Android acceptance remain open. The first integrated ib-desktop milestone is
NOT_RUN. A source/receipt draft PR is not an active default-branch CI gate.
