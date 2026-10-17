# Modified Lua runtime qualification

`scripts/qualify-icky-lua.grease` is a producer capability check extending the
existing exact-executable and bootstrap contracts, FP issues 9, 3 and 51. It
does not select a scheduler or install a runtime on a handset. Supply the clean
`isomorphisms/lua` checkout, exact ICK driver and frontend directory, and a fresh
output directory. The checked script fixes the qualifying source, source tree,
literal fixture, and compiled producer identities; callers cannot replace the
expected digests.

The fork is Lua 5.5.1 at `87306483cec50f8c750a22dda1d0742246fad756`. Its untouched
`testes/symbolic-assignment.lua` fixture exercises both assignments, comparisons,
`λ`, `ƒ`, multiplication, division and subtraction through the real parser.
The source probe SHA-256 is
`cb5c129fb2ab4c61fea7c48725b54eb0227c2ce3352734081fe8dbe7f3540b3a`.

The qualified host compiler comes from FastChat run 37589849631, artifact
11468256648, exact source `d09978739c54858adf8a619ed4ba02cf312863ce`. That workflow
builds ICK source `515c0f29fe6e2e96e10495fbaf25da93532e7722`. The download ZIP
SHA-256 is `03a86b94e862b1d726ffc369407168145485a055322fda46370a99ccde2e0475`.
The original frontend is 489064136 bytes with SHA-256
`5aff3188c58cae7cfffb20bdade56ec3e9ab89667ff6feafcfeed066350f9400`.
The explicitly permitted debug-stripped frontend is 59602864 bytes with SHA-256
`1ffd0ef82f43fe94384702811b8bb0f2680cd0dd3146eb7a1af8f1315e4abf51`.
It was produced by GNU objcopy `--strip-debug` from that checked member; machine
code is unchanged. The driver and link-driver remain the original artifact
bytes. No compiler from PATH participates. System GCC-13 supplies the host
CRT/header/library search directory, GNU binutils assemble/link, and ICK's actual
frontend compiles all maintained C and the foreign Lua runtime. This is the
qualified ICK host stage, not a generic GCC source-compilation fallback.
`-fno-use-linker-plugin` explicitly disables optional LTO plugin discovery: the
qualified compiler artifact carries no LTO plugin and these builds use no LTO.

The producer writes an interpreter and an actual `MAKE_LIB` runtime object from
the same selected source. An Icky C bridge links that exact object, embeds the
unaltered fixture with `.incbin`, and loads it using `luaL_loadbufferx(...,"t")`.
The finished executable's source section is extracted and compared byte for
byte with the source fixture. Its dynamic dependencies must contain no second
Lua library. The receipt binds source paths, tree/blob digests, compiler/linker,
runtime object and executable digests. Downstream builds must use that object
and rehash it before and after linking; a passing interpreter does not qualify
an unrelated embedded library.

`tests/modified-lua/negative-controls.grease` compiles stock source from the same
fork's unchanged upstream parent `0b29f408433e92953cc72b1d3e06c7ac8139e439`.
It prints the same Lua 5.5.1 release but fails the literal semantic fixture.
The controls also exercise an older symbolic fork, a stock interpreter earlier
in PATH, a stock linked object, replaced ordinary-Lua fixture bytes, a missing
compiler and a stock compiler executable. No fixture translates glyphs.

`receipt.tsv` has one final `status` field (`PASS` or `BLOCKED`) and separate
`NOT_RUN` Android/physical fields. Negative controls record each required case
in `negative-controls.tsv`; an unexpected success fails the script. Source,
runtime-object and host execution evidence do not establish an Android link,
APK, installation or physical-device result. The Android path still needs its
own exact-ABI ICK object or declared NDK gap/stage evidence.

The CI uses Grease's existing three-line launcher unchanged from its exact owner
source. The narrow POSIX launcher only chooses the inherited implementation
applet; the qualification and control programs are Grease. Temporary GitHub
producer artifacts are checked dependencies, not a permanent release shelf.
Expiry or denied retrieval remains a blocker and must restore the exact source
build through the existing bootstrap owner rather than admit a stock runtime.
