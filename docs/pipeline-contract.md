# Pipeline contract: deterministic shell, explicit model flexibility

`flexible-pipes` should make the boundary between deterministic computation and model inference impossible to miss.

## Stage kinds

### Deterministic stage

A deterministic stage is an ordinary program or pure transform. Its receipt should identify:

- executable or source identity;
- argv;
- declared environment inputs;
- input content hashes;
- output content hashes;
- stdout, stderr, and exit status.

Given the same declared inputs and execution environment, this stage is expected to reproduce the same outputs. A failed determinism check is a real pipeline failure.

### Model stage

A model stage is a controlled source of flexible output. Its receipt must identify at least:

- model catalog key;
- provider/repository identity;
- resolved immutable model revision;
- inference runtime and version;
- prompt/messages after templating;
- input content hashes;
- generation parameters, including seed where the runtime supports one;
- raw returned output and its hash;
- stderr and exit status.

Fixing these fields does **not** justify claiming bit-for-bit deterministic inference across runtimes or hardware.

### Recorded replay stage

A recorded replay does not call the model. It re-emits the exact previously accepted model output named by a receipt. This is the bridge that lets the rest of a pipeline replay deterministically.

## First execution rule

A model stage may propose text, code, a plan, labels, structured data, or another bounded artifact. A later deterministic stage decides how that artifact is parsed, validated, compared, executed, rejected, or passed onward.

Do not hide deterministic policy inside a model prompt when it can be expressed as ordinary code.

Do not hide model judgment inside an ordinary stage when the output actually depends on an LM.

## Pythia's role

Pythia is both a usable worker and a measurement family. Its checkpoint series lets the same pipeline be evaluated across training time and model size. That gives us a way to ask which apparent pipeline properties are structural and which are accidents of one strong model.

The first catalog therefore includes two large Pythia sizes. Smaller and intermediate checkpoints can be added when an experiment needs them; the initial bootstrap does not need to mirror the entire Pythia suite.

## Near-term implementation target

The next useful slice is deliberately small:

1. a pipeline file describes ordered stages and their declared inputs/outputs;
2. deterministic stages run as subprocesses;
3. model stages use a small common stdin/stdout boundary;
4. every stage emits a machine-readable receipt;
5. an accepted model receipt can be replayed without inference;
6. pipeline success is fail-closed when a stage, receipt, hash, or parser does not match its contract.

Graph scheduling, retries, distributed workers, model voting, and automatic optimization come later.
