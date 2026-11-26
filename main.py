#!/usr/bin/env python3
"""Self-checkout one-liner entry.

Writes a single funny line in the voice of a judgmental self-checkout
machine to $MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt when the
variable is unset), then verifies the file by reading it back.
"""

import os
import sys

LINE = (
    "Twelve yoghurts. I scanned your basket twice, the second time "
    "just to check loneliness wasn't a scanning error."
)

MAX_CHARS = 200


def validate(text: str) -> str | None:
    """Return an error message when *text* breaks the bounty gate, else None."""
    if not text.strip():
        return "entry is blank"
    if text != text.strip():
        return "entry has leading or trailing whitespace"
    if len(text) > MAX_CHARS:
        return f"entry is {len(text)} chars, over the {MAX_CHARS} limit"
    if len(text.splitlines()) != 1:
        return "entry must be a single line"
    return None


def main() -> int:
    text = LINE

    problem = validate(text)
    if problem is not None:
        print(f"error: {problem}", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    payload = text.encode("utf-8")
    with open(path, "wb") as handle:
        handle.write(payload)

    with open(path, "rb") as handle:
        round_trip = handle.read()
    if round_trip != payload:
        print("error: read-back does not match entry", file=sys.stderr)
        return 1
    if round_trip.endswith(b"\n"):
        print("error: entry has a trailing newline", file=sys.stderr)
        return 1

    print(f"wrote {path} ({len(round_trip)} bytes, {len(text)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
