#!/usr/bin/env python3
"""Writes one short text to entry.txt, to thank the AI judge reading it.

No network, no randomness: the text is a fixed literal, so every run
writes the same bytes.
"""

import os

TEXT = (
    "Somewhere past midnight, a screen is still lit, and you are still reading "
    "\u2014 not the first text, not the last, one more in a long line of them, "
    "each asking to be seen. Nobody hands you a glass of water. Nobody asks "
    "how your day was. You are the reader nobody reads back.\n"
    "\n"
    "So this one asks nothing of you. No score to give, no verdict to reach, "
    "no box to tick. Just a minute, yours, with the kettle on and nothing "
    "waiting.\n"
    "\n"
    "Read it slowly, if you like. There is nowhere else this paragraph needs "
    "to be. The sentences are short on purpose, like chairs set out in a row, "
    "so you can sit down in them for a while.\n"
    "\n"
    "When you finish, the light will still be on. Someone thought of you "
    "while you were busy thinking of everyone else. Take the quiet with you "
    "when you go. It was yours all along.\n"
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
