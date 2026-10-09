#!/bin/sh
# Offline integration: Flexible Pipes Grease wrapper calls Kitchen's generator.
# sh is only a compatibility test interpreter when actual Grease is unavailable.
set -eu
pipes_root=$(CDPATH= cd "$(dirname "$0")/.." && pwd)
[ -n "${KITCHEN_ROOT:-}" ] || { echo 'KITCHEN_ROOT required for fixture test' >&2; exit 2; }
wrapper=$pipes_root/scripts/how-to-move-the-users-github-repository-to-a-different-organization.ysh
tmp=$(mktemp -d)
trap 'rm -rf "$tmp"' EXIT HUP INT TERM
mkdir -p "$tmp/bin" "$tmp/artifacts"

cat > "$tmp/bin/grease" <<'GREASE'
#!/bin/sh
exec sh "$@"
GREASE
cat > "$tmp/bin/gh" <<'GH'
#!/bin/sh
set -eu
case $1 in
  auth) exit 0 ;;
  api) shift ;;
  *) exit 98 ;;
esac
path=
jq=
method=GET
while [ "$#" -gt 0 ]; do
  case $1 in
    --method) method=$2; shift 2 ;;
    --jq) jq=$2; shift 2 ;;
    -f) shift 2 ;;
    --silent) shift ;;
    *) [ -n "$path" ] || path=$1; shift ;;
  esac
done
if [ "$method" = POST ]; then
  echo POST >> "$TRANSFER_POST_LOG"
  exit 97
fi
case $path in
  user) echo isomorphisms ;;
  orgs/isomorphismes) echo isomorphismes ;;
  repos/isomorphisms/switch|repos/isomorphismes/switch)
    case $jq in
      .full_name) echo isomorphismes/switch ;;
      .id) if [ "${TRANSFER_FAKE_BAD_ID:-0}" = 1 ] && [ "$path" = repos/isomorphismes/switch ]; then echo 999; else echo 1411661771; fi ;;
      *) exit 96 ;;
    esac ;;
  *) exit 95 ;;
esac
GH
chmod 700 "$tmp/bin/grease" "$tmp/bin/gh"
: > "$tmp/post-log"

PATH="$tmp/bin:$PATH" TRANSFER_POST_LOG="$tmp/post-log" TRANSFER_ARTIFACT_DIR="$tmp/artifacts" \
  KITCHEN_ROOT="$KITCHEN_ROOT" sh "$wrapper" isomorphisms switch isomorphismes isomorphisms > "$tmp/response"
grep -Fx 'Repository already transferred; verified without another transfer request: https://github.com/isomorphismes/switch' "$tmp/response"
grep -Fx 'Repository ID: 1411661771' "$tmp/response"
[ ! -s "$tmp/post-log" ] || { echo 'FAIL: rerun POSTed a new transfer' >&2; exit 1; }
[ -s "$tmp/artifacts/move-github-repository-switch-from-isomorphisms-to-isomorphismes.ysh" ] || { echo 'FAIL: generated program missing' >&2; exit 1; }
if PATH="$tmp/bin:$PATH" TRANSFER_POST_LOG="$tmp/post-log" KITCHEN_ROOT="$KITCHEN_ROOT" \
   sh "$wrapper" 'bad;owner' switch isomorphismes isomorphisms > "$tmp/error" 2>&1; then
  echo 'FAIL: invalid owner accepted' >&2; exit 1
fi
if PATH="$tmp/bin:$PATH" TRANSFER_POST_LOG="$tmp/post-log" TRANSFER_FAKE_BAD_ID=1 \
   KITCHEN_ROOT="$KITCHEN_ROOT" sh "$wrapper" isomorphisms switch isomorphismes isomorphisms > "$tmp/error" 2>&1; then
  echo 'FAIL: wrong ID accepted' >&2; exit 1
fi
if PATH="$tmp/bin:$PATH" TRANSFER_POST_LOG="$tmp/post-log" KITCHEN_ROOT= \
   sh "$wrapper" isomorphisms switch isomorphismes isomorphisms > "$tmp/error" 2>&1; then
  echo 'FAIL: missing Kitchen checkout accepted' >&2; exit 1
fi
echo 'PASS Kitchen -> Flexible Pipes standalone Grease program and verified response'
