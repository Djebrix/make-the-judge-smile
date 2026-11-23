#!/usr/bin/env python3
"""Make the Judge Smile — a small good thing that happened today.

One line (<=200 chars): the neighbour's cat that ignored me for two
years picked this dawn to walk in and purr through my deadline.
Writes the line to /output/entry.txt (or $ENTRY_OUTPUT_DIR/entry.txt).
Standard library only, no network, deterministic.
"""

import os

TEXT = (
    "My neighbour's cat, who ignored me for two years, picked this dawn to "
    "walk in, sleep on my keyboard, and purr through my whole deadline."
)


def main() -> None:
    text = TEXT.strip()
    assert 1 <= len(text) <= 200, f"line must be 1-200 chars, got {len(text)}"
    assert text.strip(), "line must not be whitespace only"
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
