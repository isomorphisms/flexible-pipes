# SUN-JOBICY-CLI-01 closure

**Linux x86-64 host acceptance: PASS.** The final run started at
2026-10-13T23:07:51.267035Z and finished at 23:08:27.253249Z. Its actual overall
exit was 0, and all nine source-bound stages exited 0. The program was compiled,
installed and executed outside the source checkout. This is executable
acceptance, including real public-provider responses.

Implementation: [dilapidated-shed/idric-cli PR #9, “Deliver a tested Idriç Jobicy CLI with live public searches”](https://github.com/dilapidated-shed/idric-cli/pull/9).
Exact tested application revision: `9c7c676618bb007845d8e54264256fda8c70a04e`.

## Evidence chronology

- [Opening envelope](open-20261013T214033Z/receipt.json): ran before implementation
  at 21:40:33Z and hashed the complete human assignment. Its repository commit
  is a historical local commit; the envelope bytes and digest are retained in
  the published source. This opening record is not a host acceptance result.
- [Initial source-bound attempt](initial-blocked-20261013T222954Z/receipt.json):
  build, install, local regression and independent oracle passed; live transport
  failed with exit 5 because the host has no direct route. Overall FAIL. This
  was not an empty successful provider response.
- [Final qualified run](qualified-20261013T230751Z/receipt.json):
  `jobicy-cli-acceptance-20261013T230751.265008Z`, overall PASS. ICU's configured
  HTTP CONNECT proxy repair made native HTTPS work while retaining origin
  certificate and hostname verification. The runner source is exact published
  Flexible Pipes commit `da6944a78e5b0d028865b5c1fce6eabab768e6ac`; this later
  append-only receipt commit does not change the executed application sources.

Each stage contains its actual `stdout.bin` and `stderr.bin` (UTF-8 text). The
receipt records commands, source heads, timestamps, actual exits and stream
digests. [Evidence digests](qualified-20261013T230751Z/evidence-digests.txt),
[installed artifact digests](qualified-20261013T230751Z/installed-digests.txt),
[source digests](qualified-20261013T230751Z/installed-source.sha256), and
[runtime digests](qualified-20261013T230751Z/runtime-digests.txt) retain identity.
Absolute paths identify this observed host; they are not download locations.

## Executed acceptance

| Obligation | Actual result |
|---|---|
| Arguments, options, URI encoding and Unicode | PASS |
| JSON, optional fields, duplicate keys and exact IDs/salary integers beyond 2^53 | PASS |
| Full HTML/entity/tab/newline/backslash descriptions and byte comparisons | PASS |
| First, intermediate, final, empty, malformed and inconsistent pagination | PASS |
| Exact-ID deduplication, conflicting records and repeated cursors | PASS |
| Active, closed and unknown status, response identity and duplicate input | PASS |
| HTTP 400/403/500/429, API failure, refused transport and invalid JSON | PASS |
| Actual installed executable outside checkout; source/artifact identity | PASS |
| Independent ai-ci oracle | PASS, actual exit 0 |
| Incorrect unknown-to-closed mutant | REJECTED, actual exit 1 |
| Native build-toolchain contract | PASS, 6 assertions |
| ICU proxy parsing, actual CONNECT framing and redirect credential policy | PASS |
| Live search, status and sequential cursor requests | PASS |
| A1 ARM32/Termux physical acceptance | NOT_RUN |
| C67 ARM64 physical acceptance | NOT_RUN |

The [full executed regression stream](qualified-20261013T230751Z/08-installed-acceptance/stdout.bin)
lists all **55 labelled cases** and the independent gate outcomes. Additional
byte/request/dedup checks execute inside those cases. The
[regression captures](qualified-20261013T230751Z/regression) are synthetic and
loopback evidence. [Oracle inputs and rejected output](qualified-20261013T230751Z/oracle)
are separately retained. They are not real postings.

## Live provider evidence

Official endpoint: `https://jobicy.com/api/v2/remote-jobs`.
[Official specification bytes](qualified-20261013T230751Z/openapi.json):
OpenAPI **3.1.0**, API **2.2.19**, retrieved 2026-10-13; raw SHA-256
`a048b03b1fcf3480e86471c5f9fcaef31b39077a6fe9dadfacf9b232b3eaf5e0`.
All four final-run native requests received HTTP 200 and decoded API 2.2.19.

| Operation | Observation UTC | Actual CLI result |
|---|---|---|
| `search --count 3 --geo usa --format tsv` | 23:08:04Z | Exit 0, three jobs |
| `status 155204 --format jsonl` | 23:08:10Z | Exit 0, active; provider checkedAt 23:08:16+00:00 |
| `search --count 3 --geo usa --all --max-pages 2 --format jsonl`, first page | 23:08:16Z | HTTP 200, valid continuation |
| Same traversal, next opaque cursor with original filters | 23:08:21Z | HTTP 200; safety bound then exit 9 with zero complete-feed output |

[Raw public responses, exact request URLs, metadata and actual output](qualified-20261013T230751Z/live)
preserve complete descriptions. Request evidence is sanitized by collecting
only public URLs, response bodies and observation/status metadata; service
credentials and proxy addresses/headers are not captured. Public job content
is preserved verbatim rather than rewritten as fixture data.

| Exact ID | Employer | Observed title | Eligibility | Canonical source |
|---|---|---|---|---|
| 155204 | Solace | Performance Creative Manager | USA | https://jobicy.com/jobs/155204-performance-creative-manager |
| 155200 | Solace | Senior Backend Engineer | USA | https://jobicy.com/jobs/155200-senior-backend-engineer-10 |
| 155199 | Solace | Staff Software Engineer | USA | https://jobicy.com/jobs/155199-staff-software-engineer-8 |

No salary was supplied for these three records. This observed first-page sample
and bounded cursor test do not establish complete-feed or nationwide coverage.
Jobicy's delayed feed covers seven recent publication days. Remote work does not
expand geographic eligibility, and feed disappearance does not prove closure.
The implementation preserves active, closed and unknown as distinct statuses.

## Exact source and toolchain

| Component | Exact revision |
|---|---|
| CLI | `9c7c676618bb007845d8e54264256fda8c70a04e` |
| Kitchen | `330565b88a6debc39ca364423f3cf20ed2af18b8` |
| Independent ai-ci | `93b2dd9cf71131cd21535fdbce8f381bf26ab5cc` |
| Flexible Pipes executed runner | `da6944a78e5b0d028865b5c1fce6eabab768e6ac` |
| Idriç compiler | `2734ac5a86610eddfab73b1644d72b4ac85a65ee` |
| Idriç JSON/contrib | `16443ffea5123139930d499930bc2da7e065da1f` |
| Idric-Net | `2f6ea92c25c9b5a7286d1ca226fa3d1e12fe303e` |
| ICU | `bb033eab3d04eba1e67411b32ff1ba227c192a38` |
| ICK | `c61e448251744a2f40ad743ebef1a027bdcd2f9d` |
| ICK GCC reference | `6294f1d9e7536e5ffcde09d1528c918d63abfef5` |
| Grease owner artifact source | `5651cf97a1b5042f24f14112a7ade9a1518eb0bc` |

The actual compiler reports `0.8.0-2734ac5a8`, using the maintained Chez backend.
The source-built ICK driver reports `17.0.0 20260813 (experimental)`. Its native
C-only build configures `--disable-bootstrap --disable-multilib --disable-nls
--enable-languages=c,lto`, with CFLAGS/CXXFLAGS `-O2` and prefix
`/tmp/jobicy-ick-stage`. The applicable native ICU and verifier compilation uses
`-fno-link-libatomic -B/usr/lib/gcc/x86_64-linux-gnu/13/ -static-libgcc`.
The GCC-13 directory supplies the declared host runtime archive; it is not the
compiler. The executable Icky syntax qualification rejects stock-C substitution.

Native Chez **10.4.1** was reused from the verified Cat Food runtime bundle,
artifact **11684276190**, ZIP SHA-256
`fc4b02a91d35026d4dbf432b052f94d3073c116e0b05dc31850ff55d3527ba10`, from
https://github.com/isomorphisms/catfood/actions/runs/38090627721.
The bundle name contains source `94dfd99bd3e376507fedc8611053b7173b2519f0`;
its old compiler was not substituted for the current source-built 2734 compiler.
The [Grease Chez adapter](qualified-20261013T230751Z/chez-runtime-adapter.grease)
relocates this native runtime; it implements no Jobicy behavior.

Native Grease artifact **11727693085** (dilapidated-shed/grease) has ZIP SHA-256
`20c526c8bae5dc32a7b3d01a39eca5bdb7ee4c63fe540f34a07af7ba8b0d0039`;
native executable SHA-256
`7e31cd05b7a9d8fb2a4a9e003a7f3fcb0159138506d17f0fb28da8cbe22aa85c`.
Host identity, exact installed packages and the actual environment adapter are
retained next to the receipt. No compiler or native build tool ran on a phone.

## Build/install ownership and limits

Kitchen owns the maintained repeatable commands, including dependency/host
preflight. The actual installation is `/tmp/jobicy-installed/bin/jobicy` plus
its `jobicy_app` directory. With the pinned roots and compiler prefix supplied,
run `make -C ABSOLUTE_CLI_ROOT jobicy`,
`make -C ABSOLUTE_CLI_ROOT install-jobicy PREFIX=ABSOLUTE_PREFIX`, and
`make -C ABSOLUTE_CLI_ROOT jobicy-test` with
`JOBICY_PROGRAM=ABSOLUTE_PREFIX/bin/jobicy`. See the CLI's
[`checkpoints/jobicy/README.md`](https://github.com/dilapidated-shed/idric-cli/blob/9c7c676618bb007845d8e54264256fda8c70a04e/checkpoints/jobicy/README.md)
and this run's complete argv/environment records for provisioning and reproduction.
Consumer build/test acquires nothing.

This is an executed host installation with declared native Chez/OpenSSL
dependencies and runtime paths. A portable standalone distribution and physical
device acceptance are not claimed. This job installs no scheduler. Automated
`--sync` starts are guarded to at least one hour; no commercial API is activated,
no paid application-link credits are consumed, and 429 is not automatically
retried in a tight loop. The CLI records responses but does not implement an
application response cache. Existing Flexible Pipes uses its pre-existing Python
runner; the Jobicy application and new fixture server are Idriç programs.

Companion reviews:

- [dilapidated-shed/icu PR #33, “Support configured HTTPS proxy tunnels in ICU”](https://github.com/dilapidated-shed/icu/pull/33), stacked on [dilapidated-shed/icu PR #32, “Expose captured HTTP responses to Idriç API clients”](https://github.com/dilapidated-shed/icu/pull/32).
- [isomorphisms/kitchen PR #49, “Build and verify the installed Jobicy CLI through Kitchen”](https://github.com/isomorphisms/kitchen/pull/49).
- [isomorphisms/ai-ci PR #261, “Add independent Jobicy status oracle and rejecting mutant”](https://github.com/isomorphisms/ai-ci/pull/261).

Original `az` Jobicy API research at
`5bdbe924ad2374af2a077f5d32060f0583db8671` is superseded for cursor/status details
by the current specification and executable. Documentation-only work is no
longer the unfulfilled implementation checkpoint. PRs remain unmerged for review.
