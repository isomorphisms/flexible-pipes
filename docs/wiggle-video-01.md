# One input-to-movie route

Assignment: https://github.com/isomorphisms/flexible-pipes/issues/250

An input changes the application's state, the real renderer draws that state,
and Kitchen assembles its numbered stills. A camera angle, a generator action
and the end of a recorded audio window have different meanings. The driver
preserves those meanings rather than treating all three as smooth coordinates.

`pipelines/wiggle-video-01.json` registers one invocation with five required
stages: timeline tests, production, independent AI-CI verification, adversarial
verification, and sealing. Its absolute-path parameters are `control`,
`context`, `inputs` and a fresh `output`. Use the existing FP `scripts/run-pipeline`
controller and its `GREASE_BINARY` runtime binding. This existing Python
controller remains named migration debt; all newly maintained orchestration
and verification here uses checked Ithon, and the phase recipe uses Grease.

`tasks/wiggle-video/run.grease` checks the pinned AI-CI head before any stage.
The driver and independent verifier separately check exact producer origins,
source revisions and tracked working bytes. The normal inputs are the four
retained examples under `tasks/wiggle-video/examples/`. Source pins live in
`tasks/wiggle-video/source-pins.tsv`; AI-CI independently retains its producer
pins. No application gets another encoder.

## Motion plan and controls-free rendering

Every movie has an authored `motion-plan.tsv`, separate from its raw inputs.
Each row is `start_frame`, `end_frame`, `kind`, `intent`; intervals are half-open
and cover the complete movie exactly once. Sections contain at least two frames.
`hold` requires identical scene frames throughout the section. `move` and
`source` require visible change; `source` describes source-driven movement such
as the retained audio windows. At least one moving section is required.
The plan describes purpose and pacing before rendering; events/keyframes drive
the actual application, on the same frame clock. AI-CI checks the resulting
frames against those obligations. A prose caption alone cannot pass a hold.

Control visibility is an independent application rendering policy. Mathematical
state and timing must not depend on whether controls are drawn. Movie manifests
require `controls_visible=false`; adapters select a real scene-only owner API.
No crop, paint-over, screenshot mask or encoder filter can satisfy this policy.
Interactive applications may still compose the controls pass normally.

| Producer | Scene/control boundary used by the movie |
| --- | --- |
| Mathieu | Owner `mathieu_render_with_options` with `controls_visible=0`; separate scene and controls passes; the whole dance is fitted to the movie viewport |
| Wegert | Owner `wegert_portrait_renderer_gles_render_frame`, separate from `wegert_overlay_renderer_gles_draw` |
| SURFER | jsurf renderer `draw` emits surface pixels; Android controls are outside that renderer |
| Florence | Original field-to-PPM rendering has no controls pass; audio/DFT state remains unchanged |

Mathieu's renderer tests cover both group sizes/layouts, unchanged session
state, explicit pass composition, scene motion and UI-only error changes.
The independent movie verifier also rejects old-style UI pixels in the fitted
scene's paper margin. Scene labels, selection rings and cycle arrows remain
mathematical annotations. Titles, buttons, history and instructions are UI.

Earlier offline PASS receipts cover the preceding scope only: they do not
establish this motion-plan/controls-off requirement. Regenerated exact-source
receipts are required. Android installation and physical behavior remain separate.

## Manifest, controls and events

All four input files are UTF-8 TSV. Each manifest key is unique. `manifest.tsv`
contains exactly `schema=wiggle-v1`, `producer`, `input_kind`, `fps`, `frames`,
`width`, `height`, and `controls_visible=false`. The equals signs here describe key/value pairs, not the
file delimiter. FPS is a positive integer up to 120; image dimensions are even
and bounded by 4096; a trace contains 2 to 1,000,000 requested frames.

`input_kind` distinguishes `scripted`, `recorded-human` and `external-samples`.
The examples contain scripted traces and the historical audio source. This
work does not claim to have recorded a new human interaction or live microphone.

Each `controls.tsv` row has these seven columns:

| Column | Meaning |
| --- | --- |
| path | Application-owned semantic control, such as camera/yaw |
| kind | scalar, vector, event, or sample |
| interpolation | linear or hold for coordinates; event for actions; source for integer sample positions |
| units | Producer-owned units and coordinate convention |
| lower, upper | Finite numeric bounds for every coordinate |
| initial | Number, comma-separated coordinates, or initial event label |

Each `events.tsv` row is `time_nanoseconds`, `order`, `path`, `value`. Times are
nonnegative and ordered; equal-time rows have strictly increasing order.
Events between two requested frames are delivered in their original order at
the next frame. They are never dropped. Initial event labels do not fire an
action. Numeric knots at time zero override the declared initial value.

Frame number `frame_index` requests time `frame_index ÷ fps`. Comparisons use
integer cross-products, so rendering wall time cannot skip or retime a request.
Coordinate interpolation uses the two surrounding input knots. After the last
knot, the value holds. Group actions never acquire interpolated permutations.
The current implementation consumes bounded offline sequences, not an
unbounded live recording service. The million-frame test samples the clock and
terminal state; it does not render a million-frame movie.

## Real producer slices

| Producer | Input and actual computation | Output profile |
| --- | --- | --- |
| Florence Nightingale | Original retained Ogg → original two-excerpt FLAC splice → mono 48 kHz PCM → original 128-sample mean-removed Hann windows → DFT → 24-term complex polynomial → original Wegert coloring | 154 frames, 96×192, 5 fps, sound; no invented 60 fps or GPU claim |
| SURFER | Fixed exact `x² + xz² + y³`; yaw and pitch control Stussak's existing jsurf preview renderer | 24 frames, 160×160, 8 fps; CPU offline ray tracing |
| Wegert | One zero and one pole move in the complex plane; the owner's offscreen GLES renderer draws the owner's unchanged shader | 36 frames, 192×192, 12 fps; actual host GL identity is retained separately |
| Mathieu | ATLAS M₂₄ actions a, b and B, selected point, pause and resume; existing session and owner scene renderer | 420 frames, 360×360, 30 fps; opening/pause/endpoint holds with the application's intervening cycle motion |

The thin adapters expose existing methods; they do not implement a surrogate
mathematical model. SURFER's current preview adapter exposes yaw/pitch, not zoom;
Wegert's example has a fixed viewport. Additional owner controls can be mapped
without changing the generic timeline contract.

Florence windows end at the right edge of each 200 ms frame interval, exactly
as in the retained experiment. AI-CI reconstructs the original two-stage
Ogg → FLAC → PCM path before checking bytes; skipping the retained FLAC boundary
can change rounding. The source audio and its genuine cylinder noise remain
retained. AAC in the viewing copy is checked for alignment against that source.

## Verification and retained evidence

Production retains inputs, resolved controls, source identities, checkpoints,
every contiguous zero-based PPM, frame hashes and a candidate MP4. Kitchen at
the pinned revision remains the only movie assembler. A render/encoder failure
leaves an incomplete directory, and a rerun refuses to overwrite it.

AI-CI imports none of the driver code. It independently reconstructs timeline
values and ATLAS permutation products, checks actual pause state and held
pixels, recomputes Florence's Fourier coefficients and selected phase-colored
pixels, verifies source audio and AAC alignment, independently re-renders
selected SURFER viewpoints, and checks Wegert's function and selected pixels.
Its existing `aici-video` verifies complete decoding, geometry, duration, FPS,
audio and codec. A separate canonical Kitchen reconstruction must decode to
exactly the same pixel checksums as the candidate, preserving frame order.

Acceptance is transactional across all four examples. A new failed verification
removes prior acceptance; sealing also binds the checker and production
digests. Only after all required FP stages pass does sealing expose `movie.mp4`.
The success receipt says `offline_examples=PASS` and `physical_device=NOT_RUN`.
This is local registered execution, not protected-controller admission or a
physical-device capture receipt.

Owner tests include twelve invalid input classes, same-time event ordering and a
long-clock sample. AI-CI attacks changed inputs and source pins, missing,
reordered and symlinked frames, corrupt movies, wrong permutations, pause
states, clocks, interpolation, equations, sample windows, DFT values,
historical audio and mathematical pixels. Separate executed cases exercise an
encoder exit, an actual `/dev/full` sink and preservation of interrupted work.
Six additional evidence mutants reject false holds, false movement, plan gaps,
missing intent, controls enabled and actual UI pixels after canonical re-encoding.

## Flower's real-engine boundary

Default branch observed at `8174dbf19c0d00547c0ca0178c50a7bccd6b40c5` has finite
crochet mechanics and retained-net realization work. The actual held-growth
prototype remains at `8d9e15f4219cb6ebc510989d5c3da02c5287e466` on
`prototype/raylib-hold-growth`.

The existing host core tests at that exact prototype were compiled through
qualified ICK and executed: release freezes the complete state, paused time
does not accumulate, a fresh press resumes, invalid/stalled input cancels,
and 60/120 Hz input agrees on fixed steps. This establishes a runnable growth
interface. It does not establish a movie of that interface.

Flower movie integration remains **BLOCKED_REAL_ENGINE_RENDER_ADAPTER_NOT_QUALIFIED**:
the retained real Net/Skin and independent `flower_camera_move` /
`flower_camera_turn` methods still need a numbered-frame adapter to the actual
raylib/subpixel rendering path. Do not use a made-up growth wave or an unrelated
static crochet diagram as its acceptance movie. No Flower movie or A1/C67
capture is claimed by this job.
Its future adapter must accept the same authored motion plan and select a
scene-only renderer independently of mathematical growth and camera state.

## Reconcile the old Mathieu experiment

The source and tests of the old capture experiment remain preserved at
`isomorphisms/mathieu@39177f8ed2235634d3d8ecfdbda2683ee7f62042`, in
`capture/export.py` and `capture/tests/test_export.py`. It checked ordered
events, bijections/word consistency, regular frames, hashes and decoded media,
then called Kitchen. Its synthetic identity/color fixture was not a real
Mathieu recording. Those useful obligations now have generic input/media
checks and an independent ATLAS action oracle; none of its group-name labels
is used as group-authenticity evidence. The old 24/30/60-only FPS restriction
would reject the real Florence fixture and is not carried forward.

Existing application work remains [isomorphisms/mathieu PR #3, “Implement exact
Mathieu choreography and native Android application core”](https://github.com/isomorphisms/mathieu/pull/3).
No new Mathieu video PR was created. The shared replacement and preserved
provenance allow the redundant [isomorphisms/mathieu PR #2, “Validate Mathieu
replay and assemble MP4 through shared Kitchen”](https://github.com/isomorphisms/mathieu/pull/2)
to be retired after publication and exact-head verification of this route.
