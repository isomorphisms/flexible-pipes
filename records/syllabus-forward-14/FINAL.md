# SUN-SYL-FORWARD-14 — execution report

Overall: **PARTIAL**. The qualified PR stack and actual source collection slice are merged. The full seven-institution campaign, FSU originals and class-analysis/model gate are incomplete.

## Merges verified

| Change | Result |
|---|---|
| [bl4ckb4ll/syllabus PR #36, “Reconcile syllabus evidence, reading records and missing coverage”](https://github.com/bl4ckb4ll/syllabus/pull/36) | COMPLETE. Merged to main at e43af06ef2bd3749d346f696f34ad2525ca1cba1. |
| [bl4ckb4ll/syllabus PR #37, “WARC-02: fail-closed Ithon replay and exact-head self-tests”](https://github.com/bl4ckb4ll/syllabus/pull/37) | COMPLETE. Merged into the campaign at 2123d6a51f9a47d2e72154f580e6d0d58a0c0de8, then reached main through the campaign merge. |
| [bl4ckb4ll/syllabus PR #35, “Start syllabus collection campaign with coverage ledger and CDX/WARC replay”](https://github.com/bl4ckb4ll/syllabus/pull/35) | COMPLETE for its qualified source/implementation slice. Retargeted to main and merged at 725a8ac84ed44ccf5d238c3115f05b9ee9f4a587. |

The destination was fetched and verified. Main contains both prior merges. Its tree, 3f657c3cc8a156a172dc755c58ba7f13f7ab7dd2, exactly matches tested PR head 948f44cd00146f5ce577b4cfc2f875aeb463eb60. No school, major or term is declared fully covered.

The historical inventory remains a pinned snapshot: nine normalized course records, 29 reading slots, 28 starter cells and reverified source hashes. Its 12 consumer and 11 independent AICI rejection controls pass. The immutable verifier dependency is now also merged: [isomorphisms/ai-ci PR #260, “Independently check source evidence ledgers”](https://github.com/isomorphisms/ai-ci/pull/260).

## Newly retained original documents

All are Fall 2026 University of South Florida syllabi. The archive receipt for the successful three-document acquisition is [run 39333675595 / artifact 12226621504](https://github.com/bl4ckb4ll/syllabus/actions/runs/39333675595/artifacts/12226621504), ZIP SHA-256 47fbcfc22fa2970b07461f0e65bf7bbf900fdb14e669225eadb189ca2fb63495.

| Verified course | Instructor | Original bytes | Original HTML SHA-256 |
|---|---|---:|---|
| [PHM 6267, section 901 — Continental Philosophy III](https://usf.simplesyllabus.com/doc/10e8ekbh6/Fall-2026-PHM-6267-%28AC-PHI%29-901-Continental-Philosophy-III%3A-Struc-Deconstruc?mode=view) | Joshua Rayman | 72077 | eb038eb7ac76f2e82809fafae57e44c78fa2cc1e8f23c2615c7d2735eb38e608 |
| [ENC 1101, section 064 — Composition I](https://usf.simplesyllabus.com/doc/01zbfm1ij/Fall-2026-ENC-1101-%28AC-ENG%29-064-Composition-I?mode=view) | Anita Wholuba | 166705 | b7059702acb049036b802c873864597e3032f23854cd9060eec99d230db1c670 |
| [EUH 3401, section 001 — Classical Greece](https://usf.simplesyllabus.com/doc/06spksbji/Fall-2026-EUH-3401-%28AC-HTY%29-001-Classical-Greece?mode=view) | Jesse Obert | 157824 | afd00ad7af9297ccdcaa8e7a7a5f15019694b3b3b8445f448fdd9279be1f0b56 |

The original bodies, vendor metadata, request receipts and legacy derived JSON are retained separately from curated source-checked TSVs. Final HTTP status is unknown for the legacy USF capture client; a transport exit code is not relabelled HTTP 200. EDG 7067 remains education.

## Assigned readings actually observed

The root bookshelf gained 29 distinct work-level records: **27 named works plus two author-based selections with unknown work titles**. Required/recommended/bundle distinctions, exact assignment evidence, dates/ranges, ISBNs, edition statements and missing evidence remain course-specific. These are work records, not enrollment-weighted student exposure.

Philosophy, four required works:

- Michel Foucault — Society Must Be Defended: Lectures at the Collège de France, 1975–1976; ISBN 9780312203184; lectures I–II.
- Michel Foucault — Archaeology of Knowledge; ISBN 9780394711065; introduction pp. 3–21 and The Unities of Discourse, with two later chapter/page ranges unspecified.
- Gilles Deleuze — Difference and Repetition; ISBN 9780231081580; preface/introduction, chapter 1, chapter 5 pp. 222–261, conclusion pp. 262–304.
- Gilles Deleuze — The Logic of Sense; ISBN 9780231059831; preface and specified series.

Additional scheduled philosophy reading: Foucault, Order of Things — foreword/preface, Las Meninas, The Four Similitudes, chapter 10 sections 1–4 pp. 344–373. No edition is guessed from these page numbers. [Exact philosophy provenance and schedule](https://github.com/bl4ckb4ll/syllabus/tree/main/course%20information/usf/fall-2026/philosophy).

English: Let’s Talk, 2e Ebook, and the included Little Seagull Handbook ebook. Authors/ISBNs and the handbook edition are not supplied. InQuizitive software and unspecified optional Purdue OWL material are excluded. [Exact English provenance](https://github.com/bl4ckb4ll/syllabus/tree/main/course%20information/usf/fall-2026/english).

History primary readings: Herodotus selections (work title not specified), Thucydides selections (work title not specified), Xenophon’s Anabasis and Hellenika, Plato’s Apology, and Demosthenes’ Third Philippic. Loeb translations are preferred for quiz questions; other translations are permitted. Exact translators/volumes remain unknown.

History secondary readings:

1. Peregrine Horden and Nicholas Purcell — The Corrupting Sea, introduction.
2. Ilse Schoep — Crete.
3. Kim Shelton — Mainland Greece.
4. Joseph Maran — Ceremonial Feasting Equipment, Social Space and Interculturality in Post-Palatial Tiryns.
5. A. J. Mazarakis Ainian — Early Greek Temples: Their Origin and Function.
6. Marc Van de Mieroop — A History of the Ancient Near East ca. 3000–323 BC, third edition, chapter 13.
7. Richard Janko — From Gabii to Gordion to Eretria and Methone: The Rise of the Greek Alphabet.
8. Kurt A. Raaflaub and Robert W. Wallace — ‘People’s Power’ and Egalitarian Trends in Archaic Greece.
9. Alain Duplouy — Citizenship as Performance.
10. Anton Powell — Sparta: Reconstructing History from Secrecy, Lies and Myth.
11. Josiah Ober — ‘I Besieged That Man’: Democracy’s Revolutionary Start.
12. Kurt A. Raaflaub — The Breakthrough of Dēmokratia in Mid-Fifth-Century Athens.
13. Josine H. Blok — Perikles’ Citizenship Law: A New Perspective.
14. Timothy Doran — Spartan Oliganthropia.
15. Eduard Rung — The Persian King as a Peacemaker. The Ideological Background of the Common Peace Treaties in 4th Century Greece.
16. Emily Mackil — Creating a Common Polity, chapter 2.

[Exact history assignments, source bibliography and missing evidence](https://github.com/bl4ckb4ll/syllabus/tree/main/course%20information/usf/fall-2026/history). Scheduled source spellings and uncertainty are preserved rather than silently resolved.

## Genuine Common Crawl path

COMPLETE for the bounded witness: exact CC-MAIN-2026-39 query → actual ICU range acquisition → checked native Ithon gzip/WARC replay → HTML recovery → explicit unrelated-page classification → no assignment promotion.

- Target: https://www.reed.edu/ ; capture timestamp 20260906235851.
- Compressed source: crawl-data/CC-MAIN-2026-39/segments/1788492699693.82/warc/CC-MAIN-20260906231007-20260907021007-00742.warc.gz.
- Offset 843666201, length 9367. Actual HTTP 206; Content-Range bytes 843666201-843675567/952222438.
- Compressed SHA-256 f9652a22cff1d6b5649b6bf9420b9c7c6c7058019348e8d201cb03ed42cf5d58.
- CDX/WARC payload SHA-1 CRUA4JE526YD3EO5RF4CDHNE66MZFXQW.
- Recovered entity: 49214 bytes; SHA-256 1c7f0300f3ed38ba847dace7cb95443c6a865f12396e561f37ba5166a619f894.
- Clean published ICU/Idric-Net sources rebuilt through Kitchen with actual Idriç and ICK, then acquired identical compressed bytes again.
- warcio 1.7.5 and hash-pinned jwarc 0.37.0 independently validate and extract identical entity bytes.
- Independent capture/proxy/range controls pass. The reader rejects unsupported encoding, malformed headers/indexes, wrong target/status/digest, truncated or extra data, aliases and stale output. A killed-after-publication retry control passes.

[Original compressed fixture and complete bounded index response](https://github.com/bl4ckb4ll/syllabus/tree/main/parsers/fixtures/common-crawl/reed-20260906235851). It is a homepage, not a syllabus: **zero Reed courses or readings are inferred**. This engine witness and the three real reading-bearing USF documents are distinct evidence.

## Exact integrated-head CI receipts

All five passed at 948f44cd00146f5ce577b4cfc2f875aeb463eb60 before merge:

- [Inventory/source integrity and 23 rejection controls](https://github.com/bl4ckb4ll/syllabus/actions/runs/39337083878).
- [Native Ithon, authentic WARC, both foreign oracles, independent assignment checks, source classification and reproducibility](https://github.com/bl4ckb4ll/syllabus/actions/runs/39337083925). Artifact 12227091983, ZIP SHA-256 7bc4ceb8f9899f347d26b13693adeab9ed047cb5351fad04b9394d141a0fd930.
- [Grease/parser regression](https://github.com/bl4ckb4ll/syllabus/actions/runs/39337083862).
- [Retained legacy ingestion regression](https://github.com/bl4ckb4ll/syllabus/actions/runs/39337083805).
- [Repaired bounded live acquisition](https://github.com/bl4ckb4ll/syllabus/actions/runs/39337083880). Artifact 12227896088, ZIP SHA-256 8671fd6194c7013f914f0322f44c012d72e8960159964c6d31e003c1d556709c.

The native gate checks source receipts and refuses missing native ELF; no CPython fallback satisfies it. Legacy USF .py parsing is explicitly migration debt and is not relabelled checked Ithon. These are pre-merge exact-head results; destination tree/ancestry verification is separate.

## Coverage, failed stages and next actions

PARTIAL: 3 new observed courses / unknown course population; three cells with new originals / 28 starter cells. No denominator-based coverage percentage, enrollment exposure or complete term is claimed.

All 28 cells received a capped CC-MAIN-2026-39 query: page 0, one index block, limit five, explicit discipline URL filter. Seven returned bounded no-match responses; **21 FAILED at HTTP discovery with 502/503/504**. [Exact queries, bodies, metadata and hashes](https://github.com/bl4ckb4ll/syllabus/tree/main/acquisitions/network-20261019/panel). Other pages/blocks/collections remain unsearched; 25 cells still need newly acquired original syllabi.

BLOCKED: both FSU current PDF URLs return 404. PHI 3670 exact historical queries in CC-MAIN-2023-50 and CC-MAIN-2020-50 returned 504; PHI 3700 returned bounded no-match responses. Internet Archive availability returned 200 with empty archived_snapshots for each exact HTTPS URL. This does not prove historical absence. [Exact availability responses and receipts](fsu-availability/).

Next executable actions:

1. Retry the failed PHI 3670 requests serially with backoff; inspect historical HTTP/HTTPS URL variants and FSU CMS migration paths. Recover the original before upgrading anthology mappings.
2. Verify department-specific source URLs at Miami (Ohio), MVSU, Ole Miss, Reed and Chicago, then capture one real dated syllabus. Do not rerun broad filtered queries in a burst.
3. Verify actual area/regional programs and cross-lists; do not invent area-studies departments.
4. Enumerate a declared course/term population before frequency or institutional coverage comparison.
5. Complete public ICU range-command/pagination admission, general PDF/encoded-content recovery and checked-Ithon migration of the retained USF extractor.
6. Continue the class-analysis gate: [four source-grounded evaluation seeds](https://github.com/bl4ckb4ll/blackball-training-gym/blob/64f8dc0a7ec981f464a998b559d90cfd034e01b6/evaluations/class-college/usf-2026-source-cases.md) are prepared outside trainer records. At least eight further distinct reviewed scenarios and actual model/scorer export/execution remain required. Training, inference and measured improvement are NOT_RUN; comparative interpretive publication remains blocked.

Initial native-frontend bypass, PYTHONHOME contamination and stale fixed-count failures were FAILED attempts and have been repaired; their failure receipts are retained. Institutional rhetoric and material questions are kept separate from private motive claims.

Closed as satisfied: syllabus issues 23 (inventory) and 24 (WARC), Flexible Pipes issue 108 (bounded inventory envelope). Updated but open: syllabus 25–34 and training-gym 7. Companion ICU/Idric-Net/AICI/Kitchen/Flexible Pipes implementation changes are preserved on draft branches; local candidate qualification is not their main-branch or public-release admission.
