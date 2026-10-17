# Repeatable retained-source qualification

The registered `storage-retained-source-fixtures` pipeline invokes Kitchen's
host procedure and AICI's receipt verifier, using explicit absolute checkouts,
exact revisions and a verified Grease runtime. It exercises IB's actual
retained-source implementation with synthetic sources. It makes no Drive/SDF
network request, inspects no private corpus and cannot accept physical C67 work.
The inherited Flexible Pipes Python runner remains existing migration debt;
this registration adds no Python source or alternative storage protocol.

Required inputs: `GREASE`, `STORAGE_IB_ROOT`, `STORAGE_IB_REVISION`,
`STORAGE_KITCHEN_ROOT`, `STORAGE_KITCHEN_REVISION`, `STORAGE_AICI_ROOT`,
`STORAGE_AICI_REVISION`, `STORAGE_RECEIPT_DIR`. Put the verified Grease command
on the host PATH. Each run needs an unused explicit receipt directory.
Reproduce the same committed inputs; run timestamps/paths are observations,
not deterministic outputs. Receipt consistency proves only host fixture scope.

Actual source acquisition remains a separate explicitly authorized process:
Drive discovery/extraction → Cauldron retain → Pensieve distill/reindex.
Raw SDF transfer stays the existing cloud-storage-api command and its private
session/receipt path. No unattended private transfer is enabled by this fixture
pipeline. Cat Food issue 117 owns C67 and other deployment materialization;
Kitchen must prepare a mobile procedure after those dependencies exist.
