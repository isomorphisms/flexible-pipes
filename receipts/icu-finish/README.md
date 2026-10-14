# SUN ICU-FINISH-01

Host acceptance: PASS. Merge integration: pending final exact-head merge.
The actual installed Idriç programs ran on Linux x86-64.

## Source and tools

| Component | Immutable source |
|---|---|
| ICU accepted head | c056ca2d588329272580ca30a8b619c6ebdf455d |
| ICU accepted tree | 3084878d421261f3c493410fd8e4a7a2afa3f287 |
| Idriç compiler | 2734ac5a86610eddfab73b1644d72b4ac85a65ee |
| Idric-Net | 2f6ea92c25c9b5a7286d1ca226fa3d1e12fe303e |
| ICK | c61e448251744a2f40ad743ebef1a027bdcd2f9d |
| Idriç JSON/contrib | 16443ffea5123139930d499930bc2da7e065da1f |
| Jobicy CLI | 9c7c676618bb007845d8e54264256fda8c70a04e |
| Indeed CLI | a6230ee2f42bc07ea5223b445a9b21899d2f3087 |
| Kitchen recipe | 78f11a5388a5601332ac890992dcf37cf8238399 |
| Independent AICI | 6f3af447c0cae573a0f0b7a2a8e3f1fc686faf85 |
| Existing AICI Indeed oracle | c1f74aec9400204ce4540c5b2147022d7c8755b7 |

Publication through Git objects verifies equality of complete local and
published source trees. Local commit identities can differ from connector
publication identities; source bytes, trees and artifact digests do not.
The fresh published-head checkout is ICU c056ca2d588329272580ca30a8b619c6ebdf455d,
not a synthetic merge checkout. The fresh build log records that exact head.

The host reused the already-qualified native ICK build, Idriç source build,
Chez 10.4.1 runtime and Grease source 5651cf97a1b5042f24f14112a7ade9a1518eb0bc.
Pinned runtime/provisioning provenance is retained in the earlier
[Jobicy receipt](../jobicy-cli/README.md). Existing FP's Python runner is
unchanged legacy orchestration; ICU, probes and API clients remain Idriç.
New command recipes use Grease. Native socket/OpenSSL remains the existing
transport boundary.

## Executed results

| Evidence | Result |
|---|---|
| Fresh checkout against installed pinned Idric-Net | PASS |
| Compiled ICU and binary/text response probe installed outside checkout | PASS |
| Independent AICI HTTP/HTTPS/proxy suite | PASS, 47 cases |
| Actual compiled native size-limit mutant | REJECTED |
| Jobicy and Indeed installed fixture suites | PASS, 125 labelled checks |
| Separate AICI client oracles and rejecting classification mutations | PASS |
| Live public Jobicy search and status | PASS |
| Two sequential live Jobicy cursor requests | PASS |
| Live Indeed | NOT_RUN: no authorized service credentials |
| A1 physical Android | NOT_RUN |
| C67 physical Android | NOT_RUN |

Capture acceptance covers binary NUL/high bytes, exact 8 MiB success,
declared/streamed overflow refusal, invalid UTF-8/encoding/charset, empty 204,
401/403/429/500, malformed status/framing, length mismatch, HTTP/TLS timeouts,
certificate trust, refusal, same/cross-origin credentials, stdout compatibility,
private files under permissive umask, repeated requests and owned-file cleanup.
Proxy acceptance executes IPv4/IPv6 CONNECT tunnels, uppercase precedence and
lowercase fallback, rejected CONNECT, refused endpoints, invalid authenticated
proxy configuration without value disclosure, original-hostname verification,
trust rejection after tunneling, loopback bypass, encrypted origin credentials
and redirect stripping. Curl is a separately executed oracle.

The actual installed native library SHA-256 is
737f9318f67f0f0476e0a4994973b7e155179e2a65f3f98157689addcc78dc2a
for ICU, the probe, Indeed and Jobicy. Full launcher/application/library
identities are in artifacts/. No curl or process-execution symbols appear in
that library; native loader witnesses bind execution to it. System-call
tracing was refused by the host and is NOT_VERIFIED, not PASS.

The live run occurred 2026-10-14T01:17:59Z–01:18:20Z (2026-10-13 evening
America/Detroit). Four native HTTPS requests returned HTTP 200 with API 2.2.19.
The cursor safety bound caused the expected CLI exit 9 and withheld incomplete
complete-feed output; the operation receipt itself is PASS. This demonstrates
two sequential real pages, not a complete feed or a population total.
Raw public response bytes, exact public URLs and observation metadata are
retained under live/. Credentials and proxy values are not recorded.

## Reproduction and failures

Use the checked FP pipelines icu-finish-build, icu-proxy-acceptance,
icu-native-mutant, icu-client-integration, icu-independent-clients and
icu-live-jobicy with the recorded host environment. Each run records exact argv,
pipeline digest, actual stdout/stderr digests, start/end and exit. The build
pipeline's icu-root parameter selects the exact fresh checkout.

The earlier failed compiler/layout, Grease syntax, unavailable syscall-trace
and privacy-fixture attempts remain under runs/ with their real FAIL status.
The privacy fixture originally mixed unrelated host captures; its next PID
attempt hit mismatched /proc namespaces. Its corrected per-run response marker
identifies the owned capture. Neither failure is relabeled as product success.

## Integration and remaining work

[dilapidated-shed/icu PR #32, “Expose captured HTTP responses to Idriç API clients”](https://github.com/dilapidated-shed/icu/pull/32)
was merged by another concurrent session at
2d37c3e523a1d55f6a5a1bda91cba8222f0e36b5 before
[dilapidated-shed/icu PR #33, “Support configured HTTPS proxy tunnels in ICU”](https://github.com/dilapidated-shed/icu/pull/33),
merged at 05446e958599c297481b05f12fe7f05fc2144750.
This job's additional capture/proxy hardening is
[dilapidated-shed/icu PR #34, “Finish binary response capture and verify installed HTTPS proxy transport”](https://github.com/dilapidated-shed/icu/pull/34).
Its exact head is c056ca2d588329272580ca30a8b619c6ebdf455d and base is
05446e958599c297481b05f12fe7f05fc2144750.
All four hosted workflows reported success; their legacy checkout is synthetic
merge evidence. Independent FP/Kitchen/AICI acceptance uses the actual head.

Keep the existing provider until
[Idric-Net issue #11](https://github.com/dilapidated-shed/Idric-Net/issues/11)
passes equivalent installed-client fixtures behind its existing interface.
Move reusable connect/TLS/framing/byte-streaming there; keep ICU result
interpretation here. No whole migration was undertaken.
Add a bounded resolver before claiming an ICU-wide DNS deadline; current socket
operations are bounded to 15 seconds. Unsupported transfer encodings fail
explicitly; compressed-text decoding remains unimplemented.
For Android, build/cross-compile the same source on a host with the declared
ARM32/ARM64 artifacts and runtime dependencies, publish through Cat Food, then
record A1 and C67 installation/launch/behavior separately. No device compiler
installation or physical execution occurred in this job.
