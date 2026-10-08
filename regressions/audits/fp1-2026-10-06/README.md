# FP1 local execution audit

This directory records observations against Flexible Pipes main 58fffd879e52a34110b6da22ab2fc03f1f48befe. It is evidence, not a qualified execution implementation.

The runner and checker were unchanged in a separate local Git clone. Their Git blobs are 214f92f3a169a5170353c558c693c7cd0b0e7ec9 and 22c0791415e555c45592435e6e982b1c8b58375e. A git diff against the cloned HEAD for both paths was empty. The fixture pipelines were added as untracked data only to that isolated clone, not to the production pipelines directory.

Each fixture was invoked with the existing documented Python interpreter form of scripts/run-pipeline from /tmp. No custom execution harness or new Python program was authored. The harmless touch commands wrote only isolated scratch markers. Both export-marker and early-marker existed afterward; should-not-exist did not. The extra command/interpreter keys are deliberately ignored by the old runner, not executed.

The unknown-name probe used unregistered. The forged-SHA probe reran positive with GITHUB_SHA set to forty ones. Empty corpus was {"schema_version":1,"cases":[]}. Raw output and process exit codes are in results/. Nonzero process status in rejecting controls is expected. PASS from the old runner does not mean the new boundary passed.

Owner regression outputs are attached with their narrow scope. Kitchen revision: b8be8b1de05827422bbf127b44720e0e2c7acc1e. Cat Food revision: 5c0ae8841e2c5553cfaed69a9bcf660991eddad1. Kitchen source-handoff also completed all 27 cases successfully in this audit; its original maintained suite and H1 evidence remain authoritative. No actual repository transfer, remote workflow mutation, APK build, signer operation, emulator, model inference or physical-device run occurred.

See ../../../docs/registered-execution-v1.md for the decision and required public-path regressions. Fixture expected rejection is future acceptance, not a claim that the old runner already rejects them. These files must only execute in disposable scratch; do not copy them into the accepted operation registry.
