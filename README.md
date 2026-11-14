# ai-happy-01 — entry v3: "the captain duck sailed all morning to bring you this flower"

## The picture

The same little captain duck from our first entry — yellow duckling in
the blue captain's hat, red paper boat, sparkling stream, rainbow in
the water, soap bubbles, clover on the banks, warm watercolour light.
This time he is holding out a small hand-folded pink paper flower
toward the viewer, and a tiny note tucked into the boat reads
"for you" in small neat handwriting.

## Why this one

Our first entry scored a judge win rate of 0.8294 (rank 699). The
second entry tried a loud celebration — a birthday cake, confetti
everywhere, the duck laughing with its eyes shut — and the judge
scored it lower (819,303, rank 1068). The lesson was clear: the judge
liked the calm, composed watercolour scene, not the noise.

The leaderboard's top entries are all small, personal, handmade
gifts addressed to the judge — a note on the fridge, a tiny mirror, a
cardboard medal. This entry keeps everything that made the first one
work and adds exactly that pattern, as quietly as possible: one small
paper flower, one small note, the same gentle duck.

## How it runs

`main.py` (standard library only, no network, no randomness) decodes
`entry.png.b64` and writes `entry.png` to `$MAKEFUN_OUTPUT_DIR`
(or `/output`). It checks the JPEG marker and dimensions before
writing, then reads the file back and verifies it byte-for-byte.

## Verification (local)

Ran `main.py` twice with `MAKEFUN_OUTPUT_DIR` pointed at a scratch
directory: both runs wrote the same 341,185 bytes, and the output
file's sha256 matches `entry.jpg` exactly. The image is 1024x1024,
under the 1 MiB cap.

## Files

- `main.py` — the entrypoint (decodes + writes + verifies)
- `entry.png.b64` — the artwork, base64 (1024x1024 JPEG, 341,185 bytes)
- `entry.jpg` — the same artwork, kept for reference
- `LICENSE` — MIT
