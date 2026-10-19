# Holomorphic GPU repair execution

This pipeline continues the registered envelope
https://github.com/isomorphisms/flexible-pipes/issues/227. It runs the retained
reference, independent checker qualification, native runtime-source-binding
tests, E1 producer sampler and independent phase/log-modulus comparison through
Kitchen/Grease/Ike. The maintained Ubuntu workflow obtains the native ICK
compiler through the pinned independent `ick-host` action and builds Ike with
that compiler. The host driver links the ICK-produced objects explicitly.

The run handoff binds exact source commits, executable hashes and source-file
hashes. It is a materialized per-run input, not a second checkout registry.
Kitchen's `test-admission.grease` rejects relative contexts, unknown phases,
missing handoffs, changed materials and changed executable identities before
any producer executes. Source input files must belong to the declared commits.

The hosted input pins use published commits in
`tasks/holomorphic-gpu-repair/source-pins.tsv`, including the retained checked
shader compiler f32f27a37a176a7b2c580aa703c5d33df9511728. Reconciled newer
compiler work is not adopted by this host test. The tested preparation is
[isomorphisms/kitchen PR #69, “Prepare Holomorphic mathematical qualification through Grease and Ike”](https://github.com/isomorphisms/kitchen/pull/69).
The minimal dated host receipt records the local commits actually exercised and
the separately published commits with identical trees; it does not claim that
the future hosted workflow has already run.

`classifications.tsv` starts every evidence boundary as NOT_RUN. The retained
reference and AICI checker can pass before a missing ICK blocks actual compiled
tests on a local host. Missing numerical output cannot count as success. The
native binary64 reference is distinct from generated shader and GPU execution.

The final generated-compiler stage currently stops explicitly: the reconciled
compiler still needs actual checked-generation/API qualification followed by
an APK, selected-source readback, numerical readback and independent acceptance.
An intentional nonzero blocker means the pipeline has not completed the user's
end-to-end objective. A future numbered Kitchen candidate must supply that real
path before this stage can pass. No stage fabricates shader or device evidence.

The emulator's fixed `/usr/bin/sh` boundary delegates its maintained procedure
to the published, digest-verified Grease engine. Launch/source-binding receipts
remain separate from numerical parity. A1/GE8322, C67/GE8320 and TAB_P10/Mali-G57,
thermal behavior and sustained performance require separate real receipts.
