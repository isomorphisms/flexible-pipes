# Historical v1 pipeline invocation — superseded

The forms below describe the historical interface and are not current Android dispatch instructions. Use [registered-android.md](registered-android.md). The maintained Python pipeline-name interface is preserved; workflow dispatch now requires a complete data-only `request`, not an optional `pipeline` input.

A pipeline name refers to a checked-in `pipelines/<name>.json` file. The runner resolves that file in the repository checkout; neither the user nor an assistant should reconstruct its steps from memory.

## Terminal

After `run-pipeline.yml` is on the default branch, the canonical terminal form is:

```sh
gh workflow run run-pipeline.yml \
  -R isomorphisms/flexible-pipes \
  -f pipeline=regression-history-smoke
```

The local equivalent, useful inside a known checkout, is:

```sh
python3 scripts/run-pipeline regression-history-smoke
```

## ChatGPT request form

Use the explicit request:

```text
Run flexible-pipes pipeline regression-history-smoke.
```

That sentence is a naming convention, not privileged model syntax. The required behavior is mechanical: resolve the canonical repository and exact pipeline spec, submit that pipeline to its declared runner path, then inspect the resulting receipt/artifact. Do not replace it with an improvised local procedure.

Where direct GitHub workflow dispatch is unavailable to the current ChatGPT surface, a dedicated `pipeline-requests` branch can carry one request JSON per commit:

```json
{"pipeline":"regression-history-smoke"}
```

A push of that file triggers the same workflow. The request path is only a dispatch adapter; pipeline logic remains in the checked-in pipeline spec and scripts.

If neither dispatch route is available, report the run as blocked and return the exact terminal command. Never describe an unsubmitted pipeline as running or completed.
