#!/usr/bin/env python3
"""Entry for make.fun: The Funniest Excuse for Skipping a Meeting.

The program writes a single excuse line to the grader's output
folder. The line is fixed text, written exactly as it appears
below; nothing is fetched, generated, or randomised at run time.
It is 146 characters, inside the 1 to 200 character gate.
Deterministic: the same bytes on every run, with no network.
"""

import os
import sys

EXCUSE = "Sorry, I have to skip stand-up — I'm already in a meeting about cutting down on meetings, and it just got extended by a meeting about the meeting."

LIMIT = 200


def run() -> int:
    text = EXCUSE
    if not text.strip():
        print("error: excuse is blank", file=sys.stderr)
        return 1
    if len(text) > LIMIT:
        print(f"error: excuse is {len(text)} characters, over the {LIMIT} limit", file=sys.stderr)
        return 1
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    path = os.path.join(outdir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    sys.exit(run())
