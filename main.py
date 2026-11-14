#!/usr/bin/env python3
"""ai-happy-01 entry v3: the captain duck sails over with a paper flower.

The artwork is stored in this repository as ``entry.png.b64`` (base64
text) so the whole entry stays plain UTF-8. When the grader runs this
program it decodes that file and writes the picture to ``entry.png``
inside the output directory named by ``$MAKEFUN_OUTPUT_DIR`` (or
``/output`` when the variable is not set).

The program is deliberately boring: standard library only, no network,
no randomness, no clock. The same input always produces the same
output bytes. Before writing anything it checks the decoded payload
starts with the JPEG start-of-image marker (FF D8 FF) and reads the
image's width and height from the JPEG header, so a damaged payload
fails loudly instead of quietly producing a broken file.

The picture: the same little captain duck from our first entry, still
sailing his red paper boat over the sparkling stream after the rain —
but this time he is holding out a small hand-folded pink paper flower
toward the viewer, with a tiny note tucked into the boat that reads
"for you". A small, specific, handmade gift, painted in the same warm
watercolour light.
"""

import base64
import os
import sys
from pathlib import Path

PAYLOAD = "entry.png.b64"
TARGET = "entry.png"
JPEG_MARKER = b"\xff\xd8\xff"


def out_dir() -> Path:
    """Output directory from the environment, defaulting to /output."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def read_size(data: bytes) -> tuple[int, int]:
    """Pull (width, height) out of a JPEG's Start-of-Frame segment."""
    i = 2
    while i < len(data) - 9:
        if data[i] != 0xFF:
            i += 1
            continue
        marker = data[i + 1]
        if marker in (0xD8, 0xD9) or 0xD0 <= marker <= 0xD7:
            i += 2
            continue
        size = (data[i + 2] << 8) | data[i + 3]
        if marker in (0xC0, 0xC1, 0xC2):
            height = (data[i + 5] << 8) | data[i + 6]
            width = (data[i + 7] << 8) | data[i + 8]
            return width, height
        i += 2 + size
    raise ValueError("no JPEG Start-of-Frame segment found")


def main() -> int:
    here = Path(__file__).resolve().parent
    raw = base64.b64decode((here / PAYLOAD).read_text())
    if not raw.startswith(JPEG_MARKER):
        print("payload is not a JPEG (bad SOI marker)", file=sys.stderr)
        return 1
    width, height = read_size(raw)
    dest = out_dir()
    dest.mkdir(parents=True, exist_ok=True)
    written = dest / TARGET
    written.write_bytes(raw)
    # Read the file back and confirm it is exactly what we decoded:
    # same length, same JPEG marker, same dimensions. If the read-back
    # differs, the entry is broken and we say so instead of passing
    # silently.
    check = written.read_bytes()
    if check != raw or not check.startswith(JPEG_MARKER):
        print("read-back verification failed", file=sys.stderr)
        return 1
    check_w, check_h = read_size(check)
    if (check_w, check_h) != (width, height):
        print("read-back dimensions changed", file=sys.stderr)
        return 1
    print(f"wrote {TARGET} ({width}x{height}, {len(raw)} bytes) to {dest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
