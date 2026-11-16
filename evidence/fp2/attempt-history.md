FP2 qualification retains failures and partial state. No run below is deployed
trusted execution. Prompts remain in chat. Owners remain FP #24/#26/#2/#18,
Kitchen #15/#24, AICI #205 and Cat Food #107.

| Run | Observed first failure / outcome |
| --- | --- |
| 37408882004 | Invalid dynamic workflow shell expression; no jobs |
| 37409075392 | Root Git ownership check; rejected before source execution |
| 37409359486 | Worker could not read runner-home runtime; partial upload permissions |
| 37409602491 | Worker runtime path permissions; retained artifact 11388457103 |
| 37409984412 | Grease reserved FD 100 exceeded RLIMIT_NOFILE 64; limit corrected to 256 |
| 37410229422 | Candidate 2 discarded API arguments; fixture peer died and timed out |
| 37410427425 | Required Ithon frontend passed; same candidate 2 failure |
| 37410978324 | Candidate 3 confused Grease word and expression parameters |
| 37411542415 | Candidate 5 dispatch passed; disposable bare Git ownership failed |
| 37411836901 | Both routes and hostile suite passed for candidate 5 |
| 37412477520 | Grease mutation fixture used an undefined shell variable instead of ENV |
| 37413891487 | Candidate 6 fixture suite passed, later invalidated by mock exit-code audit |
| 37416168577 | Untyped permission-probe bitwise flags rejected before operation effects |
| 37416602662 | Candidate 7 lost HTTP 404 bytes in a failing command substitution; zero POST |
| 37416992770 | Candidate 8 tried lookup scratch in read-only artifact directory; zero POST |

Raw records for the superseded candidate 6 and the later failed attempts live in
their numbered directories in each owning repository. Earlier job logs and
partial artifacts remain attached to the numbered Actions runs. Initial local
runtime failures are preserved under `evidence/fp2-runtime-qualification`.

The original scratch workspace lost regular files during this session. Published
sources were recovered into separate checkouts; no dirty work was reset or
cleaned. Unpublished lost local diagnostics are not presented as durable proof.
Concurrent user fixture and legacy-test changes were retained; expected-parent
publication rejected stale updates before the newer work was incorporated.
