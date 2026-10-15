#!/bin/sh
# Refuse a pipeline stage whose supplied source identity does not match Git.
set -eu
if [ "$#" -ne 16 ]; then
  printf '%s\n' 'usage: check-nhtsa-source-pins.sh [NAME ABSOLUTE_CHECKOUT REVISION] x8' >&2
  exit 2
fi
for name in idric-cli ICU Idric Idric-JSON Idric-Net ICK Kitchen ai-ci; do
  : "$name"
done
# Eight pairs: CLI, ICU, Idriç, Idriç-JSON, Idric-Net, ICK, Kitchen, ai-ci.
for name in cli icu idric json net ick kitchen aici; do
  root=$1
  expected=$2
  shift 2
  case "$root" in
    /*) ;;
    *) printf 'FAIL: %s checkout must be absolute\n' "$name" >&2; exit 2 ;;
  esac
  if ! printf '%s\n' "$expected" | grep -Eq '^[0-9a-f]{40}$'; then
    printf 'FAIL: %s pin must be a 40-character SHA\n' "$name" >&2
    exit 2
  fi
  test -d "$root/.git" || {
    printf 'FAIL: %s checkout missing\n' "$name" >&2
    exit 1
  }
  observed=$(git -C "$root" rev-parse HEAD)
  if [ "$observed" != "$expected" ]; then
    printf 'FAIL: %s source pin mismatch expected=%s observed=%s\n' "$name" "$expected" "$observed" >&2
    exit 1
  fi
  if [ -n "$(git -C "$root" status --porcelain)" ]; then
    printf 'FAIL: %s checkout has uncommitted changes at %s\n' "$name" "$observed" >&2
    exit 1
  fi
  printf 'PIN_OK\t%s\t%s\n' "$name" "$observed"
done
