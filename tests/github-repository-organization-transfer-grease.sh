#!/bin/sh
# Fixed CI shell boundary; the test implementation is maintained Grease.
set -eu
root=$(CDPATH= cd "$(dirname "$0")/.." && pwd)
: "$KITCHEN_ROOT"
: "$GREASE_BINARY"
case $GREASE_BINARY in
    /*) ;;
    *) echo 'GREASE_BINARY must be absolute' >&2; exit 2 ;;
esac
exec "$GREASE_BINARY" "$root/tests/github-repository-organization-transfer-display.grease" "$KITCHEN_ROOT" "$GREASE_BINARY"
