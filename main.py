#!/usr/bin/env python3
"""Real-Life Patch Notes: The Comedy Changelog.

Writes one patch note (<=160 chars) for a bug in human biology to
/output/entry.txt, in the terse register of a real release note.
"""

import os

LINE = (
    "v3.1.0: fixed a bug where the brain replayed your most embarrassing "
    "moment from 2014 every night at 2 a.m. as a featured update."
)


def main() -> None:
    # Gate: the sealed scorer requires UTF-8 text of 1-160 chars, not
    # only white space. Fail loudly here instead of shipping a bad entry.
    assert 1 <= len(LINE) <= 160, f"line is {len(LINE)} chars, must be 1-160"
    assert LINE.strip(), "line must not be only white space"
    LINE.encode("utf-8")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
