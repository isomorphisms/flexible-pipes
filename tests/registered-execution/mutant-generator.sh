#!/opt/catfood/bin/grease
# Deliberately broken fixture recipes. Never active production implementations.
var repository = ARGV[1]
var source = ARGV[0]
var destination = ARGV[2]
var name = "transfer-${repository}-from-${source}-to-${destination}.sh"
var mutation = ENV.FP_TEST_MUTANT
if (mutation === 'pass-printer') {
  echo 'echo PASS' > "$name"
} elif (mutation === 'failing-test') {
  echo 'exit 23' > "$name"
} elif (mutation === 'output-bound') {
  echo 'while true { echo FORGED_PASS }' > "$name"
} elif (mutation === 'time-bound') {
  echo '/usr/bin/sleep 61' > "$name"
} else {
  echo 'unknown mutant' >&2
  exit 2
}
/usr/bin/cp -- "$name" "transfer-${repository}-from-${source}-to-${destination}.paste.grease"
if (mutation === 'pass-printer') {
  echo 'echo KITCHEN_TRANSFER_CHILD_EXIT:0' >> "transfer-${repository}-from-${source}-to-${destination}.paste.grease"
  echo 'echo OWNERSHIP_TRANSFER_VERIFIED' >> "transfer-${repository}-from-${source}-to-${destination}.paste.grease"
} elif (mutation === 'failing-test') {
  echo 'echo KITCHEN_TRANSFER_CHILD_EXIT:23' > "transfer-${repository}-from-${source}-to-${destination}.paste.grease"
  echo 'echo OWNERSHIP_TRANSFER_NOT_VERIFIED' >> "transfer-${repository}-from-${source}-to-${destination}.paste.grease"
}
