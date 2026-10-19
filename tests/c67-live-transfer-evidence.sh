#!/bin/sh
set -eu
root=$(CDPATH='' cd -- "$(dirname -- "$0")/.." && pwd)
evidence=$root/evidence/github-repository-transfer/2026-10-09-c67-live
receipt=$evidence/receipt.tsv
repositories=$evidence/repositories.tsv

[ -f "$receipt" ] || { echo 'missing C67 live-transfer receipt' >&2; exit 1; }
[ -f "$repositories" ] || { echo 'missing C67 live-transfer repository ledger' >&2; exit 1; }
tab=$(printf '\t')

for required in \
    "schema${tab}flexible-pipes-live-operation-v1${tab}contract" \
    "source_owner${tab}isomorphisms${tab}request" \
    "destination_owner${tab}isomorphismes${tab}request" \
    "repository_count${tab}10${tab}request" \
    "delivery_surface${tab}ChatGPT_Android_plain_text${tab}user-confirmed" \
    "delivery_result${tab}PASS${tab}user-confirmed" \
    "code_block_delivery_result${tab}FAIL_UNAVAILABLE_COMPONENT${tab}user-screenshot" \
    "physical_command_execution${tab}PASS${tab}user-confirmed" \
    "exact_final_terminal_output${tab}NOT_RETAINED${tab}evidence-limit" \
    "live_postcondition${tab}PASS${tab}independent-GitHub-read" \
    "generic_trusted_chat_adapter${tab}NOT_DEPLOYED${tab}evidence-limit"
do
    grep -Fqx "$required" "$receipt" || {
        printf 'missing required receipt row: %s\n' "$required" >&2
        exit 1
    }
done

awk -F '\t' '
    NR == 1 {
        if ($0 != "repository\told_owner\tnew_owner\trepository_id\tpostcondition") exit 1
        next
    }
    NF != 5 || $1 == "" || seen_name[$1]++ || seen_id[$4]++ ||
        $2 != "isomorphisms" || $3 != "isomorphismes" ||
        $4 !~ /^[0-9]+$/ || $5 != "PASS" { exit 1 }
    { count++ }
    END { if (count != 10) exit 1 }
' "$repositories" || {
    echo 'invalid C67 live-transfer repository ledger' >&2
    exit 1
}

actual=$(mktemp)
expected=$(mktemp)
trap 'rm -f "$actual" "$expected"' EXIT HUP INT TERM
cut -f1,4 "$repositories" | sed '1d' > "$actual"
cat > "$expected" <<'EOF'
mapping-class	1412391052
montesinos	1412394512
Bulatov-Goodman-Strauss	1412402847
regina	1412463768
VanKoughnett	1412475989
zakharevich	1412476795
snaith	1412477737
kirby-calculus	1412481397
morava	1412482666
goodwillie	1412483445
EOF
cmp "$expected" "$actual" || {
    echo 'C67 live-transfer repository identities changed' >&2
    exit 1
}

echo 'PASS retained C67 live-transfer evidence: 10 canonical destinations with preserved IDs'
