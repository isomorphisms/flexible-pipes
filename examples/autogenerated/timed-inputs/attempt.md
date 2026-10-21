# Timed mathematical inputs

WIGGLE-VIDEO-01, 2026-10-21. Target: Linux x86_64 offline production.

## Types and effects

Time is a nonnegative rational number of seconds, independent of render wall
time. Frame index and frame count are whole numbers. A control has its own
semantic path, value kind, units, bounds and interpolation law. Discrete events
retain their order; they are never interpolated. Source samples identify exact
integer positions in a retained input. A frame request includes all events
since the preceding request and the sampled state of every continuous track.

Central actions: validate a timeline; sample a continuous track at a frame
time; deliver ordered events to the application's real engine; retain numbered
frames; invoke the pinned Kitchen builder; obtain separate AI-CI acceptance.
Failures include invalid control types/ranges, reordered events, unsafe paths,
input/source hash changes, partial frames, interrupted producers and encoders.

The Idriç slice establishes the discrete-interpolation admission law. Media
decoding, SHA-256, filesystem transactions and managed subprocess interfaces
are not implemented by that slice. The existing FP controller is inherited
Python migration debt; the new filesystem/media orchestration uses checked
Ithon, not additional Python source. C adapters only call the existing owner
engine and renderer; they do not implement alternate mathematics or encoding.

## Verification

Compiler: relocated Idriç 94dfd99bd3e376507fedc8611053b7173b2519f0, Chez host
backend. Exact execution results are retained in the execution receipt.

The admission program compiled and ran successfully. The initial absolute-path
compile failed because its module name was interpreted relative to the wrong
source directory. Compiling the same bytes as `TimedInputs.idric` in the
isolated source directory repaired the invocation; no alternate backend ran.

The initial orchestration attempts are retained as `*.pi.rejected` and are not
maintained executable modules. The actual Ithon frontend rejected the first
at `parameter 'path' needs a static type`. The replacement uses explicit typed
boundaries and has been checked and executed through Ithon, including imported
modules. This was a repair of the attempted program, not evidence that Ithon
cannot do the job. The unreached producer attempt was not separately executed.

The first Mathieu trace scheduled b before a's 12 cycle intervals finished.
The actual session returned failure and the incomplete output was preserved.
The corrected trace waits for the real engine; its pause interval remains
unchanged. Independent audio reconstruction also had to retain the original
FLAC quantization boundary before comparing the original PCM bytes.

The first registered FP run at `b4fe3e385a15224b83d7034fb2350e2502f56624`
failed before timeline tests: the selected Grease runtime rejects POSIX
`export`. Its own diagnostic required the maintained `setglobal ENV` spelling.
The corrected recipe uses that spelling. The failed FP stage receipt is
retained; syntax parsing alone had not proved runtime execution.

## Language work

The motion-plan correction adds typed half-open frame sections with independent
intent and hold/movement obligations. A separate render policy disables controls
inside the owning application renderer; it does not change the mathematical
session or encode a crop. `motion_plan.pi` uses the existing checked Ithon
boundary for the same missing Idriç filesystem/process facilities described above.
The Mathieu owner renderer and tests are Icky C through the qualified ICK frontend.

The first missing end-to-end facility here is a maintained typed media/process
interface with bounded byte reads, process exit status, cancellation and
transactional output. Remove the Ithon orchestration only after an Idriç
implementation rejects the same bad timelines and corrupted media without
changing the producer/driver contract. The small admission law alone is not
proof that Idriç drove the movie.

## Golay rosette film

FP #253 reuses the owner's sampled layout API at e6afdba33b6f1e10be43944bbe604dcc2c21f09d.
The bounded layout/frame scalar is a whole native geometry tick from 0 to 90.
Its track drives the layout only; group/action events remain discrete ATLAS
permutations. The five selected coordinates complete T0 union T1 exactly.
The retained plan covers 540 frames at 30 fps: grid hold, 90-tick smooth layout,
octad reveal, a, pause, b, final hold. Every source frame is generated through
the owner renderer. Held frames have separate regular filenames sharing bytes
by hard link, preserving the complete sequence within the host's disk budget.
The native adapter reruns the entire trace in a fresh process and compares every
regenerated pixel and checkpoint without storing a redundant second sequence.
This extends the same Icky C/Ithon boundary and its existing Idriç facility gap;
it adds no mathematical engine, video encoder, or new Python source.
