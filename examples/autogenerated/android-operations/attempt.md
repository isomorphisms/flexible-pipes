# Android operation control

Values: an immutable request, a trusted deployment, candidate source, stage
observations, and sealed outputs. Preparation returns either missing inputs or
a finite admitted plan. Execution returns exit/signal/timeout/output-limit
observations. Verification returns a claim-specific decision. Delivery requires
both that decision and independently promoted deployment authority.

Types: Request → Deployment → Preparation; AdmittedPlan → IO StageObservations;
StageObservations → Verification; Verification → DeliveryPermission.
Application source cannot select policy, signer, package identity, stage commands,
or verifier versions. A screenshot cannot inhabit the type PhysicalVisualPass.

Idriç is not installed on this host. The selected FP1 contract requires checked
Ithon at this control boundary; its existing failed probes identify missing
Try/With/While/mapping-index support. The implementation uses checked Ithon
with finite for-loops and typed foreign method calls, and a native C subprocess
boundary for bounded execution and interruption. No unchecked Python helper or
shell-language replacement is introduced. C is built using NDK clang on the
build host; phone delivery is prebuilt only.

Required language work: native typed bounded process actions and filesystem
sealing, so these foreign boundaries can eventually move into Idriç. Acceptance
must preserve a child failure behind successful output formatting and kill its
whole process group at a deadline.
