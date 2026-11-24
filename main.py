#!/usr/bin/env python3
"""The Funniest Toaster Error Message — one line, written to /output/entry.txt.

The line is a single sentence of at most 120 characters. It reads like a
real error message from a real kitchen appliance (code E-12 included) and
saves its surprise for the very end: the toaster has been keeping count,
and nobody ever said thank you. No bread pun, no toast pun — the joke
comes from the appliance's quiet resentment instead.
"""

from __future__ import annotations

import os
import sys

LINE = "ERROR E-12: I have toasted 4,182 slices for you and not once have you said thank you."

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 120


def check_line(line: str) -> str:
    """Return the line when it meets the contest gate, else fail loudly.

    The gate is the brief itself: one line, 1 to 120 characters, UTF-8,
    not only white space, nothing but the message.
    """
    text = line.strip()
    if not text:
        raise ValueError("entry is empty")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the {MAX_CHARS} limit")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    return text


def main() -> int:
    text = check_line(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
