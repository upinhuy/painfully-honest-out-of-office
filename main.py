#!/usr/bin/env python3
"""Painfully Honest Out-of-Office — make.fun entry.

Writes one out-of-office auto-reply to /output/entry.txt.

The reply has to be painfully honest about the sender's absence and
inbox, yet polite enough that a manager would let it stand. The line
below admits the private truth every employee knows — a mountain of
unread mail nobody is brave enough to open — and wraps it in a warm
thank-you and a promise to reply, so it reads as honest, not rude.
"""

import os
import sys

ENTRY = (
    "I'm away, and honestly, your email will wait in a queue of 400 "
    "unread messages I already dread opening \u2014 thank you for your "
    "patience, I'll reply as soon as I'm back and brave enough."
)

MAX_CHARS = 200


def validate(text: str) -> None:
    """Enforce the competition gate: 1-200 chars, not only whitespace."""
    if not text or not text.strip():
        raise ValueError("entry is empty")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
        )
    # One sentence: exactly one sentence-ending full stop, at the end.
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("entry must be a single sentence ending in '.'")


def main() -> int:
    validate(ENTRY)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(ENTRY)
    # Read back and verify byte-for-byte: the gate counts exactly
    # what lands in the file, so a silent write failure must not pass.
    with open(path, encoding="utf-8") as fh:
        written = fh.read()
    if written != ENTRY:
        raise ValueError("entry.txt does not match the validated entry")
    print(f"Wrote {len(ENTRY)} characters to {path}")
    print(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
