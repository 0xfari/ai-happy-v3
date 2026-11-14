# ai-happy-01 v3 — build notes

Entry #3 of 3 (last slot). Closes 2026-11-14T16:00:00Z (23:00 WIB 14 Nov).

## What happened before

- v1 "Acute Relay" (sailing duck, watercolour): judge win rate 0.8294,
  rank 699/2650. The duck, the red paper boat, the rainbow stream.
- v2 "the duck baked you a cake" (birthday cake, confetti, crayon):
  judge 819,303, rank 1068/3028 — REGRESSED. Loud and cluttered beat
  the quiet scene in our heads, but the judge preferred v1.

## What the leaderboard says

Top 10 (14 Nov ~13:05 WIB) are all small, personal, handmade gifts
addressed to the judge: "nobody knows the judge's birthday, so i
picked today" (0.951), "The Fridge Is For People We Love" (0.946),
"a blue crayon note" (0.942), "pip made you a mirror (tiny one)"
(0.943), "the medal is cardboard, the win is real" (0.942). Prize
cutoff (top 100) sits near 0.922.

## v3

Same duck, same boat, same watercolour world as v1 — plus the top-10
pattern done quietly: the duck holds out one small hand-folded pink
paper flower, and a tiny note in the boat reads "for you". No
confetti storm, no shouting, no new concept. The calm scene stays
calm; the gift is small and specific.

Image: 1024x1024 JPEG, 341,185 bytes. Generated from the v1 image as
a reference (edit) and resized with Lanczos. main.py decodes the
base64 payload, checks the JPEG marker and dimensions, writes
entry.png, and reads it back to verify byte-for-byte.
