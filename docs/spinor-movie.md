# Spinor movie pipeline

`spinor-movie` is the repeatable cross-repository path for the public Spinor
0 → 2π → 4π demo.

## Ownership

- `functorial-games/spinor` owns the physical-angle trajectory, semantic
  Spin(3) / SO(3) state, contraction field, six-ribbon geometry, and numbered
  PPM frame rendering.
- `isomorphisms/kitchen` owns the pasteable composition command and canonical
  FFmpeg stills → H.264/MP4 command.
- Flexible Pipes owns identity checks, registered execution, and the normal
  pipeline receipt.

## Run

```sh
KITCHEN_ROOT=/path/to/kitchen \
SPINOR_ROOT=/path/to/spinor \
python3 scripts/run-pipeline spinor-movie
```

Optional deterministic render inputs pass through unchanged:

```sh
KITCHEN_ROOT=/path/to/kitchen \
SPINOR_ROOT=/path/to/spinor \
SPINOR_MOVIE_FRAMES=120 \
SPINOR_MOVIE_FPS=30 \
SPINOR_MOVIE_WIDTH=360 \
SPINOR_MOVIE_HEIGHT=360 \
SPINOR_MOVIE_OUTPUT=/tmp/spinor-4pi-demo.mp4 \
python3 scripts/run-pipeline spinor-movie
```

## Fail closed

`scripts/spinor-movie` checks both repository origins and the Git blob identity
of every script and semantic C/header file that can change the produced movie.
It verifies the working-tree bytes too. A newer local checkout does not silently
become the registered pipeline; update `registry/spinor-movie.json` and this
script deliberately when accepting changed inputs.

The pipeline also emits compiler/FFmpeg identities before handing off to
Kitchen. Kitchen preserves numbered stills, trajectory/checksums, verifies the
MP4 frame count, and writes a content receipt.
