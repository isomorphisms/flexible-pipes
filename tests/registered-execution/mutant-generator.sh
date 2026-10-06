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
