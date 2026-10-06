# Registered Android operations

The installed runner preserves the existing Python pipeline-name interface. These are real implementations with data-only requests.

```grease
python3 /opt/flexible-pipes/current/scripts/run-pipeline android-native-apk --request /private/build-request.json --runs-root /private/android-runs
python3 /opt/flexible-pipes/current/scripts/run-pipeline android-diagnostic-capture --request /private/diagnostic-request.json --runs-root /private/android-runs
```

Required request fields: `pipeline`, `request_id`, `repository`, immutable 40-character `ref`, `target`, `application`, `permitted_actions`, `requested_result`. Current consumer values: `functorial-games/crystal`, `miro-a1`, `halite`. Build admits `build,package,verify` and `verified-apk`. Capture admits `observe` and `private-capture`, with `diagnostic_plan` naming an absolute private experiment-file path. Its claim contract identifies package, installed APK digest, device instance, task digest, observed symptom, candidate explanation, observable/producer and prepared input. Missing data produces a named missing-input result.

Chat form: “Run Flexible Pipes operation android-native-apk with this request JSON” or “Run Flexible Pipes operation android-diagnostic-capture with this request JSON.” Supported dispatch: `run-pipeline.yml` **request** input, or one JSON-only commit on `pipeline-requests`. The signed event traverses installed `github-event.pi`, admission, immutable selection and the Android controller. The sentence alone does not submit a request. A separately provisioned registered self-hosted runtime is required; no checkout is needed on the requesting machine.

Production uses fixed `/etc/flexible-pipes/android-deployment.json` and installed controller/verifier revisions. Caller `--deployment` and `FLEXIBLE_PIPES_ITHON` are qualification-only. They cannot activate policy, signing or publication. Build calls the existing authenticated AICI supervisor and Cat Food delivery, composing all seven child checks. Diagnosis calls Cat Food profile, AICI preparation, Kitchen capture and AICI evidence validation. Preparation never certifies future APK bytes; capture never certifies visual correctness.

Current definitions remain UNQUALIFIED. Original A1 signing authority, isolated producer qualification and independently provisioned runtime closure/deployment remain blockers. Build preparation blocks before compilation. Published source is distinct from a published runtime archive, installation, service availability and physical verification. Refreshed PR31 uses hosted Ubuntu as an unprivileged client and a separate TLS supervisor; the inactive client returns DEPLOYMENT_INACTIVE. Qualification adapter mode uses a separately named caller-owned configuration and never activates this service.

The executed replay form is `python3 scripts/run-pipeline regression-history-smoke --deployment ABS_CONFIG --runs-root NEW_PRIVATE_ROOT`. `tests/replay-deployment.pi` produces caller-owned HOST_FIXTURE configuration. Four fixed suites execute 11 + 44 + 1 + 15 independently expected cases. `tests/replay-coverage.pi` rejects omitted and zero-coverage suites through this same entrypoint. Caller digests are not policy approval.

The acquired command is `kitchen-android-capture --plan ABS_PLAN --profile ABS_PROFILE --runtime ABS_RUNTIME --output NEW_PRIVATE_DIR`. Existing Cat Food archive acquisition supplies prebuilt launcher/helper, checked Ithon frontend and the exact committed task. No phone compilation or source checkout fallback exists. Current tests qualify host delivery only; ARM bytes are compiled candidates, not physically accepted commands.
