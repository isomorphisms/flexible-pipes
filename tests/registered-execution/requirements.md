# FP2 runtime qualification requirements

This is a prerequisite suite, not operation acceptance. The selected contract
is FP1 at `6a72e6bec36f0021e5ee87fb23be99b7ff133ad7`.

Before writing an effectful supervisor, exercise the actual Ithon frontend with
typed source using the interfaces the supervisor needs. Each failing program
starts with `EFFECT_BEFORE_CHECK` so an unsupported construct must be rejected
before that marker executes. Failed checks must not emit successful check
receipts. Retain the original failed source and diagnostic.

Required capabilities:

- typed JSON mapping construction and indexing for request/result contracts;
- exception recovery for malformed input, process interruption and OS errors;
- guaranteed cleanup for locks, streams and worker lifetime;
- bounded process polling and termination;
- checked local calls plus explicit foreign filesystem/hash/process boundaries.

A valid control must run through the same frontend, with a check receipt whose
source SHA-256 matches the executed `.pi` bytes. An invalid local call must
reject before top-level execution. A static check is not proof of sandboxing.

Grease qualification must execute the current implementation at the top-level
gitlink. Presence of `bin/ysh`, or a different shell, does not qualify it. Do not
install a runtime or build it via an undeclared compiler as part of this probe.

The request-gate candidate must reject extra executable fields, duplicate JSON
keys, wrong types, unknown operations, unsafe names, non-positive repository
IDs and unqualified contexts. A structurally valid request must remain BLOCKED
while the implementation lacks qualification. It must make no API calls and
must never emit operation PASS, accepted artifact metadata or transfer commands.

Completion still requires the actual Kitchen generator, sealed artifact,
independent API observation, both public adapters and all FP1 hostile cases.
Passing these prerequisite tests cannot satisfy those requirements.
