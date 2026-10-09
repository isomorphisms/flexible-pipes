#!/bin/sh
# Real native Grease executes FP, Kitchen generator, and generated program.
set -eu
pipes_root=$(CDPATH= cd "$(dirname "$0")/.." && pwd)
: "${KITCHEN_ROOT:?Set KITCHEN_ROOT to the pinned companion checkout}"
: "${GREASE_BINARY:?Set GREASE_BINARY to the verified native Grease/YSH ELF}"
TRANSFER_WRAPPER=$pipes_root/scripts/how-to-move-the-users-github-repository-to-a-different-organization.ysh
export TRANSFER_WRAPPER
exec sh "$KITCHEN_ROOT/tests/github-repository-transfer-grease.sh"
