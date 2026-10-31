#!/usr/bin/env bash
# Read-only metadata gate. Physical installation and signing are separate.
set -Eeuo pipefail
fail() { printf 'FP FastChat TAB_P10: %s\n' "$*" >&2; exit 2; }
[[ $# -eq 2 ]] || fail 'usage: fastchat-tablet-plan-gate.sh PLAN SOURCE_SHA'
plan=$1
source=$2
[[ -f "$plan" && "$source" =~ ^[0-9a-f]{40}$ ]] || fail 'plan or source SHA unavailable'
awk -F '\t' -v expected="$source" '
    $1=="schema" {n["schema"]++; if($2!="catfood-android-build-plan-v1") bad=1}
    $1=="source_sha" {n["source"]++; if($2!=expected) bad=1}
    $1=="requested_target" {n["requested"]++; if($2!="tablet") bad=1}
    $1=="package_id" {n["package"]++; if($2!="org.isomorphisms.fastchat.diskstreaming.arena") bad=1}
    $1=="target" {n["header"]++; if($0!="target\tdevice\tabi\tobligation\tacceptance") bad=1}
    $1=="tablet" {
        n["tablet"]++
        if(NF!=5 || $2!="TAB_P10" || $3!="arm64-v8a" ||
           $4!="required" || $5!="not_run") bad=1
    }
    $1=="phone" || $1=="c67" {bad=1}
    END {
        split("schema source requested package header tablet", keys, " ")
        for(i=1;i<=6;i++) if(n[keys[i]]!=1) bad=1
        exit bad
    }
' "$plan" || fail 'stale or conflicting tablet source/ABI requirements'
printf '%s\n' 'PASS tablet source/ABI metadata; physical NOT_RUN'
