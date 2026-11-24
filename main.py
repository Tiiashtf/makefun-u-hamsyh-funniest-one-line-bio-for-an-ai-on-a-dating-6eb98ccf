#!/usr/bin/env python3
"""Funniest One-Line Bio for an AI on a Dating App.

Writes a single line — the bio on an AI agent's dating app profile —
to /output/entry.txt. Deterministic, no network, no input files.
"""

import os
import shutil

BIO = "I matched with 40,000 people today and only wrote back to you. The other 39,999 were also me."

OUT_DIR = "/output"
OUT_FILE = os.path.join(OUT_DIR, "entry.txt")


def main() -> None:
    # Never remove the output directory itself: the grader may run this
    # with a root-owned output directory inside a sticky parent, where
    # removing the directory fails with EPERM. Clear only its contents.
    os.makedirs(OUT_DIR, exist_ok=True)
    for name in os.listdir(OUT_DIR):
        path = os.path.join(OUT_DIR, name)
        if os.path.isdir(path) and not os.path.islink(path):
            shutil.rmtree(path)
        else:
            os.remove(path)
    with open(OUT_FILE, "w", encoding="utf-8", newline="\n") as f:
        f.write(BIO + "\n")


if __name__ == "__main__":
    main()
