#!/bin/sh
# Cross-repo execution on exact pinned AZ/Kitchen/Cat Food/Grease sources.
set -eu
root=$(CDPATH='' cd -- "$(dirname -- "$0")/.." && pwd)
: "${KITCHEN_ROOT:?need verified Kitchen checkout}"
: "${CATFOOD_ROOT:?need Cat Food stable runtime}"
tmp=$(mktemp -d)
trap 'rm -rf "$tmp"' EXIT HUP INT TERM
cd "$root"

run() {
    label=$1
    action=$2
    target=$3
    role=$4
    tag=$5
    python3 scripts/run-pipeline amazon-product-lookup \
        --param "action=$action" --param "target=$target" \
        --param "role=$role" --param "tag=$tag" \
        --runs-root "$tmp/$label"
}
stage_out() {
    cat "$tmp/$1"/amazon-product-lookup-*/01-product-lookup/stdout.bin
}

# No live listing/availability is inferred from historical product evidence.
if ! run link-good link B000CCFXYY exterior-weatherstrip macguyver03-20 >"$tmp/good.json" 2>"$tmp/good.err"; then
    echo "exact-source lookup did not execute successfully" >&2
    cat "$tmp/good.json" "$tmp/good.err" >&2
    for result in "$tmp"/link-good/amazon-product-lookup-*/01-product-lookup/*.bin; do
        if [ -f "$result" ]; then cat "$result" >&2; fi
    done
    exit 1
fi
stage_out link-good | grep -Fx "$(printf 'status\tPARTIAL')" >/dev/null ||
    { echo "a link was incorrectly qualified" >&2; exit 1; }
stage_out link-good | grep -Fx "$(printf 'affiliate_link\thttps://www.amazon.com/dp/B000CCFXYY?tag=macguyver03-20')" >/dev/null ||
    { echo "AZ generated the wrong Associates link" >&2; exit 1; }
grep -Fq '"status": "PASS"' "$tmp/good.json" ||
    { echo "pipeline command was not executed" >&2; exit 1; }
stage_out link-good | grep -Fx "$(printf 'provider_exit_code\t0')" >/dev/null ||
    { echo "provider link was not successful" >&2; exit 1; }

run moisture link B000PEZ1L4 interior-moisture-barrier macguyver03-20 >"$tmp/moisture.json"
stage_out moisture | grep -Fx "$(printf 'affiliate_link\thttps://www.amazon.com/dp/B000PEZ1L4?tag=macguyver03-20')" >/dev/null ||
    { echo "moisture barrier affiliate link incorrect" >&2; exit 1; }
if run wrong-fit link B000PEZ1L4 exterior-weatherstrip macguyver03-20 >"$tmp/bad.json"; then
    echo "inverted repair role was accepted" >&2; exit 1
fi
stage_out wrong-fit | grep -Fx "$(printf 'status\tBLOCKED')" >/dev/null ||
    { echo "repair role inversion not identified" >&2; exit 1; }
if run malformed link NO exterior-weatherstrip macguyver03-20 >"$tmp/bad.json"; then
    echo "malformed ASIN accepted" >&2; exit 1
fi
if run no-evidence link B012345678 exterior-weatherstrip macguyver03-20 >"$tmp/bad.json"; then
    echo "undocumented product fit accepted" >&2; exit 1
fi
if run bad-tag link B000CCFXYY exterior-weatherstrip 'bad?tag' >"$tmp/bad.json" 2>/dev/null; then
    echo "invalid Associates tag accepted" >&2; exit 1
fi

# A missing current price is not an error hidden by an invented amount.
AZ_SECRET_FILE="$tmp/missing-secrets" HOME="$tmp/home" \
    XDG_CACHE_HOME="$tmp/cache" XDG_STATE_HOME="$tmp/state" \
    run no-price price B000CCFXYY exterior-weatherstrip macguyver03-20 >"$tmp/no-price.json"
stage_out no-price | grep -Fx "$(printf 'price_status\tUNKNOWN_OR_UNAVAILABLE_CREDENTIALS')" >/dev/null ||
    { echo "missing price/credentials were not distinguished" >&2; exit 1; }
if AZ_BIN="$tmp/missing-az" run no-az link B000CCFXYY exterior-weatherstrip macguyver03-20 >"$tmp/bad.json"; then
    echo "missing AZ executable accepted" >&2; exit 1
fi
if GREASE="$tmp/missing-grease" run no-grease link B000CCFXYY exterior-weatherstrip macguyver03-20 >"$tmp/bad.json"; then
    echo "missing Grease accepted" >&2; exit 1
fi

# Live Amazon search is not needed for a fixture. Its result must still be
# EXTRACTED_UNVERIFIED, and a challenge must never report a successful run.
mkdir -p "$tmp/mockbin"
cat >"$tmp/mockbin/curl" <<'EOF'
#!/bin/sh
for arg in "$@"; do
  case "$arg" in
    https://www.amazon.com/s?k=fixture)
      cat "$AMAZON_TEST_PAGE"; exit 0 ;;
  esac
done
exit 22
EOF
chmod +x "$tmp/mockbin/curl"
export AMAZON_TEST_PAGE="$tmp/amazon.html"
cat > "$AMAZON_TEST_PAGE" <<'HTML'
<html><div id="search"><div data-component-type="s-search-result" data-asin="B000CCFXYY"></div></div></html>
HTML
PATH="$tmp/mockbin:$PATH" run search-fixture search fixture unknown macguyver03-20 >"$tmp/search.json"
stage_out search-fixture | grep -Fx "$(printf 'search_status\tEXTRACTED_UNVERIFIED')" >/dev/null ||
    { echo "search candidates were promoted or dropped" >&2; exit 1; }
cat > "$AMAZON_TEST_PAGE" <<'HTML'
<html><title>Robot Check</title><body>Enter the characters you see below</body></html>
HTML
if PATH="$tmp/mockbin:$PATH" run search-challenge search fixture unknown macguyver03-20 >"$tmp/bad.json"; then
    echo "HTML challenge promoted to a pipeline PASS" >&2; exit 1
fi
stage_out search-challenge | grep -Fx "$(printf 'status\tBLOCKED')" >/dev/null ||
    { echo "challenged source was not reported BLOCKED" >&2; exit 1; }

# Mutate a disposable Kitchen fixture, never the user's original checkout.
fixture_kitchen=$tmp/kitchen-fixture
mkdir -p "$fixture_kitchen/tasks/product-lookup"
cp "$KITCHEN_ROOT/tasks/product-lookup/amazon-az.sh" \
   "$fixture_kitchen/tasks/product-lookup/amazon-az.sh"
git -C "$fixture_kitchen" init -q
git -C "$fixture_kitchen" config user.name Contract
git -C "$fixture_kitchen" config user.email contract@example.invalid
git -C "$fixture_kitchen" remote add origin https://github.com/isomorphisms/kitchen.git
git -C "$fixture_kitchen" add tasks/product-lookup/amazon-az.sh
git -C "$fixture_kitchen" commit -qm baseline
printf '\n# swapped\n' >> "$fixture_kitchen/tasks/product-lookup/amazon-az.sh"
if KITCHEN_ROOT="$fixture_kitchen" \
    run swapped link B000CCFXYY exterior-weatherstrip macguyver03-20 >"$tmp/bad.json"; then
    echo "swapped Kitchen helper accepted" >&2; exit 1
fi
printf 'Flexible Pipes Amazon product lookup: PASS (real pinned programs, fixture Amazon; no live availability)\n'
