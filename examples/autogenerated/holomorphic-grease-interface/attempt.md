# Canonical Grease entrypoint for the Holomorphic host producer

BACKLOG-REPAIR-02 integrated the host/generation operation, then source-policy
review found that consumer shell steps still invoked the underlying ysh engine
path. That naming breaches the current consumer-facing Grease contract; the
old successful host semantics do not retroactively accept the interface.

Reuse the already published portable bin/grease launcher and the exact same
qualified x86_64 engine bytes. The portable archive is verified in full and
only its launcher is extracted; its Android payload is never selected for this
host. The host engine stays inside the staged Grease package as bin/ysh, which
is an implementation/provenance boundary. Every consumer invocation, custom
shell, recipe runner and test input now uses bin/grease. Record launcher and
engine identities separately in tools.tsv; the unchanged accepted Kitchen6
preflight requires that engine to be adjacent to the launcher.

Type/effect sketch: source pins, mathematical corpus, compiler/API, Kitchen
recipe, Ike and independent checker are immutable inputs. Stage zero only
acquires/hash-checks the selected engine and published launcher. Existing
Grease owns preparation, admission, producer and checker execution. No new
shell wrapper or language substitute is authored; no FP2/C++-free claim is made.
The existing exact-literal-block test passes locally through the recorded
Grease entrypoint, including pin/cache-key execution and the contained/sibling
path counterexample with spaces. Diff checks pass. Current-head hosted full
host/generation qualification remains required before merging. Physical GPUs,
sustained performance and M1 holds stay open.

Engine ZIP12192502970 SHA256295329ec3bb419d90364fcb5937eafe4306b03f68b7aaa63089dadde8082ffb5;
engine bytes7e31cd05b7a9d8fb2a4a9e003a7f3fcb0159138506d17f0fb28da8cbe22aa85c.
Published portable archive SHA2563ddb962ef313e528e525fa03518f494577e921c2201ecb49f7a11f2fbf4e82b2;
launcher bytes37088097c36a2f82cf45aaea9392e4a4cf16155fecb9da87d08a9c7fb4d92e4a.

The published interface repair commit is5f9ea480ac6623e45c2299d401eccba4492b497c; root tree07f5dd8d72d6cbe2a8c201c27d776c208bc7e3b4.
This source-bound note starts real combined-host qualification, with no
transfer of acceptance from the prior ysh-facing head.
