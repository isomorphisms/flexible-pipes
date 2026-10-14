#!/bin/sh
# Narrow pre-Grease boundary: pinned source fetch, Cat Food acquisition, exec.
# No GitHub mutation or transfer logic belongs in this POSIX file.
set -eu
umask 077
root=$(CDPATH='' cd -- "$(dirname -- "$0")/.." && pwd)
fail() { printf '\033[31mFAIL FP bootstrap: %s\033[0m\n' "$*" >&2; exit 2; }
case ${PREFIX:-} in /data/data/com.termux/files/usr) ;; *) fail 'ordinary authenticated Termux session required';; esac
for command_name in gh sha256sum mktemp mkdir dirname awk; do
    command -v "$command_name" >/dev/null 2>&1 || fail "Termux stage-zero base command unavailable: $command_name"
done
manifest=$root/tasks/catfood-fp-kitchen/source-material.tsv
[ -f "$manifest" ] || fail 'no qualified pinned source manifest; no operation attempted'
session=$(mktemp -d "${TMPDIR:-$PREFIX/tmp}/fp-transfer.XXXXXX")
tab=$(printf '\t')
while IFS="$tab" read -r repository revision remote_path digest local_path; do
    case $repository in ''|\#*) continue;; esac
    case $revision in *[!0-9a-f]*|'') fail 'invalid source revision';; esac
    [ "${#revision}" = 40 ] || fail 'source revision must be full length'
    case $local_path in /*|*..*|*[!a-zA-Z0-9_./-]*) fail 'unsafe materialization path';; esac
    destination=$session/$local_path
    [ ! -e "$destination" ] || fail 'duplicate source materialization'
    mkdir -p "$(dirname -- "$destination")"
    if gh api "repos/$repository/contents/$remote_path?ref=$revision" --header 'Accept: application/vnd.github.raw+json' > "$destination.partial" 2> "$destination.fetch.stderr"; then
        printf '0\n' > "$destination.fetch.exit"
    else
        code=$?
        printf '%s\n' "$code" > "$destination.fetch.exit"
        cat "$destination.partial" "$destination.fetch.stderr" >&2
        fail "source retrieval failed; retained $session"
    fi
    printf '%s  %s\n' "$digest" "$destination.partial" | sha256sum -c - >&2
    mv "$destination.partial" "$destination"
done < "$manifest"
runtime=$(sh "$session/catfood/catfood" ensure-grease)
[ -n "$runtime" ] && [ -x "$runtime" ] || fail 'Cat Food did not return an executable runtime'
runtime_directory=$(dirname -- "$runtime")
PATH=$runtime_directory:$PATH
export PATH
FP_APPROVED_PROGRAM_SHA256=$(cat "$session/approved-program.sha256")
export FP_APPROVED_PROGRAM_SHA256
state=${XDG_STATE_HOME:-$HOME/.local/state}/flexible-pipes/github-transfers
GREASE_BINARY=$runtime
KITCHEN_ROOT=$session/kitchen
AICI_ROOT=$session/aici
FP_TRANSFER_JOB_ROOT=$state
export GREASE_BINARY KITCHEN_ROOT AICI_ROOT FP_TRANSFER_JOB_ROOT
exec "$runtime" "$session/fp/scripts/how-to-move-the-users-github-repository-to-a-different-organization.ysh" \
    isomorphisms Museum_of_Shaders functorial-games isomorphisms \
    1412731191 conanwu777/Museum_of_Shaders
