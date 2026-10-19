#!/bin/sh
# Actual native Grease runs the batch plus each materialized Kitchen generator/candidate program.
set -eu
root=$(CDPATH= cd "$(dirname "$0")/.." && pwd)
: "${KITCHEN_ROOT:?Set KITCHEN_ROOT to the pinned companion checkout}"
: "${GREASE_BINARY:?Set GREASE_BINARY to the verified native Grease/YSH ELF}"
batch=$root/scripts/move-new-math-repositories-to-isomorphismes.ysh
tmp=$(mktemp -d)
trap 'rm -rf "$tmp"' EXIT HUP INT TERM
mkdir -p "$tmp/bin" "$tmp/state"

cat > "$tmp/bin/grease" <<'LAUNCH'
#!/bin/sh
exec "$GREASE_BINARY" "$@"
LAUNCH
cat > "$tmp/bin/sleep" <<'SLEEP'
#!/bin/sh
exit 0
SLEEP
cat > "$tmp/bin/gh" <<'GH'
#!/bin/sh
set -eu
state=${TRANSFER_TEST_STATE:?}
scenario=${TRANSFER_TEST_SCENARIO:-normal}
case ${GH_HOST:-} in github.com) ;; *) echo 'wrong host' >&2; exit 93;; esac
[ -z "${GH_TOKEN:-}${GITHUB_TOKEN:-}" ] || { echo 'tokens not cleared' >&2; exit 94; }

case $1 in
    auth)
        [ "$scenario" != unauthenticated ]
        exit $?
        ;;
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
        -f)
            [ "$2" = new_owner=isomorphismes ] || exit 96
            shift 2
            ;;
        --silent) shift ;;
        -H) shift 2 ;;
        *) [ -n "$path" ] || path=$1; shift ;;
    esac
done

id_for() {
    case $1 in
        mapping-class) echo 1412391052 ;;
        montesinos) echo 1412394512 ;;
        Bulatov-Goodman-Strauss) echo 1412402847 ;;
        regina) echo 1412463768 ;;
        VanKoughnett) echo 1412475989 ;;
        zakharevich) echo 1412476795 ;;
        snaith) echo 1412477737 ;;
        kirby-calculus) echo 1412481397 ;;
        morava) echo 1412482666 ;;
        goodwillie) echo 1412483445 ;;
        *) return 1 ;;
    esac
}

case $path in
    user)
        if [ "$scenario" = wrong-login ]; then echo other; else echo isomorphisms; fi
        exit 0
        ;;
    orgs/isomorphismes)
        echo isomorphismes
        exit 0
        ;;
    user/memberships/orgs/isomorphismes)
        if [ "$scenario" = not-member ]; then echo pending; else echo active; fi
        exit 0
        ;;
esac

case $path in
    repos/isomorphisms/*/transfer)
        method_name=${path#repos/isomorphisms/}
        name=${method_name%/transfer}
        ;;
    repos/isomorphisms/*)
        name=${path#repos/isomorphisms/}
        ;;
    repos/isomorphismes/*)
        name=${path#repos/isomorphismes/}
        ;;
    *) echo "unknown path: $path" >&2; exit 95 ;;
esac

id=$(id_for "$name") || exit 95
src=isomorphisms/$name
dst=isomorphismes/$name

if [ "$method" = POST ]; then
    [ "$path" = "repos/$src/transfer" ] || exit 96
    echo "$name" >> "$state/post.log"
    [ "$scenario" != rejected ] || { echo 'HTTP 422 rejected' >&2; exit 1; }
    touch "$state/$name.done"
    exit 0
fi

case $path in
    repos/isomorphisms/*)
        case $jq in
            .full_name)
                if [ -f "$state/$name.done" ]; then echo "$dst"; else echo "$src"; fi
                ;;
            .id)
                if [ "$scenario" = wrong-id ] && [ "$name" = morava ]; then echo 999; else echo "$id"; fi
                ;;
            .permissions.admin)
                if [ "$scenario" = no-admin ] && [ "$name" = snaith ]; then echo false; else echo true; fi
                ;;
            *) exit 95 ;;
        esac
        ;;
    repos/isomorphismes/*)
        [ -f "$state/$name.done" ] || {
            if [ "$scenario" = destination-error ]; then
                echo '{"message":"Forbidden","documentation_url":"https://docs.github.com/rest/repos/repos#get-a-repository","status":"403"}'
            else
                echo '{"message":"Not Found","documentation_url":"https://docs.github.com/rest/repos/repos#get-a-repository","status":"404"}'
            fi
            exit 1
        }
        case $jq in
            .full_name) echo "$dst" ;;
            .id) echo "$id" ;;
            *) exit 95 ;;
        esac
        ;;
esac
GH
chmod 700 "$tmp/bin/grease" "$tmp/bin/sleep" "$tmp/bin/gh"

PATH="$tmp/bin:$PATH"
TRANSFER_TEST_MODE=1
TRANSFER_TEST_STATE=$tmp/state
export PATH TRANSFER_TEST_MODE TRANSFER_TEST_STATE KITCHEN_ROOT GREASE_BINARY

cd "$tmp"
status=0
grease "$batch" > "$tmp/first.out" 2> "$tmp/first.err" || status=$?
if [ "$status" -ne 0 ]; then
    cat "$tmp/first.out" "$tmp/first.err" >&2
    exit "$status"
fi
grep -F 'BATCH MATERIALIZATION: generating ten standalone Kitchen programs; no mutation has occurred' "$tmp/first.out"
[ "$(grep -c '^PROGRAM   ' "$tmp/first.out")" -eq 10 ]
grep -F 'BATCH COMPLETE: 10/10 repositories are under isomorphismes with preserved IDs' "$tmp/first.out"
[ "$(wc -l < "$tmp/state/post.log" | tr -d ' ')" = 10 ]
printf '%s\n' \
    mapping-class montesinos Bulatov-Goodman-Strauss regina VanKoughnett \
    zakharevich snaith kirby-calculus morava goodwillie > "$tmp/expected-posts"
cmp "$tmp/expected-posts" "$tmp/state/post.log"

status=0
grease "$batch" > "$tmp/second.out" 2> "$tmp/second.err" || status=$?
if [ "$status" -ne 0 ]; then
    cat "$tmp/second.out" "$tmp/second.err" >&2
    exit "$status"
fi
grep -F 'BATCH COMPLETE: 10/10 repositories are under isomorphismes with preserved IDs' "$tmp/second.out"
[ "$(wc -l < "$tmp/state/post.log" | tr -d ' ')" = 10 ]
[ "$(grep -c 'action=already_transferred' "$tmp/second.out")" -eq 10 ]

rm -rf "$tmp/state-wrong-id"
mkdir "$tmp/state-wrong-id"
TRANSFER_TEST_STATE=$tmp/state-wrong-id
TRANSFER_TEST_SCENARIO=wrong-id
export TRANSFER_TEST_STATE TRANSFER_TEST_SCENARIO
if grease "$batch" > "$tmp/wrong-id.out" 2>&1; then
    echo 'wrong repository ID was accepted' >&2
    exit 1
fi
grep -F 'identity mismatch for morava' "$tmp/wrong-id.out"
[ ! -e "$tmp/state-wrong-id/post.log" ]

rm -rf "$tmp/state-destination-error"
mkdir "$tmp/state-destination-error"
TRANSFER_TEST_STATE=$tmp/state-destination-error
TRANSFER_TEST_SCENARIO=destination-error
export TRANSFER_TEST_STATE TRANSFER_TEST_SCENARIO
if grease "$batch" > "$tmp/destination-error.out" 2>&1; then
    echo 'non-404 destination API error was accepted' >&2
    exit 1
fi
grep -F 'cannot determine whether destination exists' "$tmp/destination-error.out"
[ ! -e "$tmp/state-destination-error/post.log" ]

echo 'PASS native Grease batch: ten transfers, idempotent rerun, preflight ID refusal, real-style 404 classification'
