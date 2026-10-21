# Registration qualification

The native Grease refusal suite exercises missing FP parameters, a corrupted
runtime/recipe material set, and an actual mismatched producer commit. Each
refusal must occur before build or evidence creation; unrelated runtime errors
do not count as the expected refusal.

[Initial hosted attempt](https://github.com/isomorphisms/flexible-pipes/actions/runs/39084845356)
materialized every pinned repository, verified the real runtime and Kitchen
digest, and installed the declared ICK bootstrap prerequisites. GitHub's custom
shell lookup then searched `_subpixel/ysh` beneath PATH entries and failed before
running the refusal suite. The workflow now uses the absolute `/usr/bin/env`
driver with the checked runtime path as its argument. This changes the runner
interface, not the script interpreter. The failed attempt is not a build pass.

Kitchen's versioned notes retain the native Grease strict-errexit/environment
findings and exact generated-output boundary. Version 4 was the local-patch
baseline. Version 5 selects the accepted whole-path/font sources and requires
both independent markers. Its positive marker fixture passes; legacy-only and
path-only logs reject for their respective missing gates.

A matching native-runtime probe also established that inherited variables are
read through `ENV`, not as implicit shell locals. The workflow now binds
`ENV.GITHUB_WORKSPACE` before invoking the recipe; no Bash environment syntax is
being counted as Grease execution.

Version 2 uses the authenticated published Grease launcher and x86_64 engine.
A fresh exact-head registered run must exercise the source compiler build,
producer and independent oracle before host qualification is accepted. Conway
bridge acceptance and physical-device evidence remain separate.
