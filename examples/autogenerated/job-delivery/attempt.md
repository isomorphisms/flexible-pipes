# Job delivery: type and runtime boundary

The domain values are an authoritative assignment, its exact UTF-8 bytes,
an audience/model, a human request, and separately observed visible/dispatch
events. `compose : Assignment → Request → Handoff`; `deliver : Handoff →
VisibleSink → DeliveryReceipt`; `dispatch : DeliveredHandoff → Dispatcher →
DispatchReceipt`. Explicit dispatch-only authority admits dispatch without a
visible event. Recovery preserves the assignment identity and records the old
failure. Byte equality is required; a model opinion cannot supply equality.

Effects belong to trusted sink/dispatcher adapters, never to generated job text.
The runtime needs bounded byte I/O, SHA-256, and a capture of the actual response
accepted by the visible sink. The desired dependent type would make dispatch in
a display mode require delivery evidence for precisely the same assignment.

The Idriç slice below isolates that authorization relation. The available
compiler checkout has no built compiler executable; the emitter reports that
the compiler is missing. No Idriç execution is claimed. The existing pipeline
controller is Python migration debt, and registered controller work uses checked
Ithon. This extension therefore uses checked `.pi` at that established boundary,
without adding a Python implementation. Runtime SHA-256 and transport adapters
remain the first concrete Idriç integration gap. Acceptance for removing this
boundary is an Idriç program that hashes actual captured bytes and rejects a
mutation before dispatch through a maintained backend.
