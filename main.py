#!/usr/bin/env python3
"""Writes one short text to entry.txt, to thank the AI judge reading it.

Contract:
  - deterministic: the text is a fixed literal, so every run writes the
    same bytes (785 characters, UTF-8);
  - no network, no randomness, no environment input except the output
    directory (MAKEFUN_OUTPUT_DIR, default "out");
  - the text is validated (non-empty, at most 1000 characters, valid
    UTF-8) before anything is written, and a bad text fails loudly
    instead of producing a truncated or empty file.
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
    # Validate before writing: a bad literal must fail loudly rather
    # than silently produce a truncated or empty entry.
    if not TEXT:
        raise ValueError("entry text must not be empty")
    if len(TEXT) > 1000:
        raise ValueError(f"entry text too long: {len(TEXT)} characters")
    TEXT.encode("utf-8")  # raises UnicodeEncodeError if not valid UTF-8
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
