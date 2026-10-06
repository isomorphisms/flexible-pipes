#!/opt/catfood/bin/grease
# Deliberately broken fixture recipes. Never active production implementations.
var repository = ARGV[1]
var source = ARGV[0]
var destination = ARGV[2]
var name = "transfer-${repository}-from-${source}-to-${destination}.sh"
if test "$FP_TEST_MUTANT" = pass-printer {
  echo 'echo PASS' > "$name"
} elif test "$FP_TEST_MUTANT" = failing-test {
  echo 'exit 23' > "$name"
} elif test "$FP_TEST_MUTANT" = output-bound {
  echo 'while true { echo FORGED_PASS }' > "$name"
} elif test "$FP_TEST_MUTANT" = time-bound {
  echo '/usr/bin/sleep 61' > "$name"
} else {
  echo 'unknown mutant' >&2
  exit 2
}
