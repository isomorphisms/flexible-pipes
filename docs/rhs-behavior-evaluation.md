# RHS claim-versus-behavior pipeline

The existing Flexible Pipes pipeline runner invokes `grease scripts/rhs-behavior-evaluation.ysh`. Its environment supplies absolute `RHS_SOURCE_ROOT`, `RHS_EVIDENCE_ROOT`, `RHS_PROFILE_ROOT`, `ITHON_ENTRYPOINT`, and `FLEXIBLE_PIPES_ROOT` paths. `ITHON_PYTHON` selects the Cat Food foreign model runtime. `grease` must be on PATH.

RHS owns claims, observer transformations, explicit relations, findings and independent grading. Cat Food owns host acquisition, build/provision pins and compiler receipts. This pipeline sequences those boundaries. The causal-model command receives only the candidate packet directory, never grading labels or checker outputs. It preserves prompts, token IDs, responses, execution and immutable model/tokenizer revision. An encoder is not used as an instruction model.

`scripts/run-pipeline-legacy.py` preserves the existing Python migration debt. The command and domain adapter execute through the pinned Ithon frontend. The runner receipt reports caller-supplied command execution with `qualified_operation: false`; it does not grant registered-operation acceptance or establish completion of FP2's compact-interpreter work.
