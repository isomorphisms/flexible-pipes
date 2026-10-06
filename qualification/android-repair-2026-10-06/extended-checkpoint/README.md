# Extended executed checkpoint

The public replay executed 77 required cases: 11 AICI diagnostic, 50 Kitchen capture, one historical Cat Food receipt and 15 request/terminal dispatch cases. Five additional tests exercised the actual immutable workflow/request adapters; two omitted/zero-suite mutants were rejected. Six selected-profile cases, two fresh acquired command runs, historical wiring and C gesture/geometry results are retained separately. These are independently expected host tests, not device acceptance.

Executed from this workspace with the delivered checked Ithon selected explicitly:

```grease
env ITHON_PYTHON=/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python3 FLEXIBLE_PIPES_ITHON=/workspace/scratch/97699b2c767e/ithon/ithon /opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python3 /workspace/scratch/97699b2c767e/flexible-pipes/scripts/run-pipeline regression-history-smoke --deployment /workspace/scratch/97699b2c767e/replay-extended.json --runs-root /workspace/scratch/97699b2c767e/replay-extended
```

The same runner's `android-native-apk` was executed with the replay's explicit build-blocked request and deployment. Expected and observed exit 1: `MISSING_RUNTIME: independently qualified AICI producer and Cat Food delivery are not deployed`, followed by `PRODUCER_PREPARATION_BLOCKED`. No compilation or delivery followed that preparation. The `valid-terminal` case executed `android-diagnostic-capture` with explicit request/deployment and produced all six required stages PASS, `artifacts: []`, and scope `private bounded observation; visual/physical correctness NOT_VERIFIED`. It called the actual Cat Food profile, Kitchen task and AICI checker using an identified HOST_FIXTURE channel.

The manifest records the exact inspected local commits/trees and tested bytes. Kitchen tested local 155f5fd76fdf78aa66476fced39a74cd7d7e2557 and published ede931c8fc9d95fb91f11c4230de28f1a97030bc have identical tree 9d50a3d290b1dde40d146f4e5557309460f97c85; publication does not change the test's observed identity. Later documentation and emulator-test commits do not inherit these results as new executions. The original 71-case checkpoint remains historical.

ARM native compilation and canonical packaging used published Crystal bab0fc8727a24d0dcff940332ae4f5451fd71d67, pinned r27c Clang/LLD, C/Lua/raylib and the existing public test key. Halite digest is 883c527fd6b11acb802a0ccb7f921d72def443d15f6b85c051c9eda6545c4275. Package inspection passed; authenticated producer verification and delivery remain BLOCKED. No substitute key or package identity was created.

The x86_64 emulator APK has different source and bytes, identified in emulator-apk.tsv. A real Android 34 software guest reached system services but failed the first 420-second boot budget before installation. Required-partition and invalid disposable-userdata setup failures were repaired; this is not an application or PowerVR diagnosis. Raw emulator/device captures remain private. A subsequent bounded retry is recorded separately when complete.

The first extended capture run's two PID-reuse expectations were wrong: the task returned the stronger `PROCESS_CHANGED:pid reused` result. Its failing ledger remains private at capture-extended-final. The corrected oracle and all 50 cases passed at capture-extended-qualified. No task behavior was weakened to satisfy that oracle.

Production operation definitions remain UNQUALIFIED; the installed transport client remains inactive. Original A1 signing authority/prior accepted artifact, independent producer release/isolation and TLS service activation are blockers. ARM command publication, phone installation/current service operation and physical visual acceptance are NOT_RUN. No phone configuration, rish pair or service was changed.
