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

## CF-A2-S6 integration attempt

Domains: data-only requests, Cat Food approved immutable plans, exact procedure
and runtime bytes, stage observations, independent decisions and per-device
acceptance. A plan belongs to Cat Food; FP cannot derive one from a target name.
Desired signatures: admit : Request × ApprovedPlan × InstalledRegistry →
Admission | Blocked; execute : Admission → IO Attempt; publish : Attempt ×
IndependentDecision → SealedOutput | Blocked. Physical acceptance is indexed
by device instance even when output bytes coincide.

This revision reconciles existing checked-Ithon controllers and preserves the
paired producer. It does not create another runner or another plan schema.
S2's immutable plan, S4's qualified decision and S5's exact procedure family
are not published at the inspected predecessor refs. Consequently the paired
route is a registered blocked reservation, not an admitted operation. Production
Android paths remain closed until those contracts and installed authority exist.
Qualification may still exercise the historical bounded diagnostic path, with
all request/plan/profile/runtime/code inputs bound to each stage and rechecked.

The existing FP1 choice of checked Ithon remains authoritative here. New work
requires the same hashing, process, exception and filesystem foreign interfaces
as the preserved attempt above; no new language fallback is introduced.
