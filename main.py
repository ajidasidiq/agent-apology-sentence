"""The One-Sentence Apology Your Agent Owes You.

A make.fun program/v1 entry. The grader runs this file and reads
/output/entry.txt: one sentence of apology an AI assistant owes the
person it works for.

The joke is a confession with a sharp turn: the agent owns up to
inventing a source, then admits its only backup for the invention was
its own confidence. Flat, specific, a little embarrassed, and
unmistakably an assistant owning a failure it really does commit.
"""

from __future__ import annotations

import os
from pathlib import Path

ENTRY = (
    "I'm sorry I cited a source that doesn't exist, then doubled down "
    "by citing my own confidence as the source."
)

OUTPUT_PATH = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))


def main() -> None:
    # The sealed gate accepts 1-200 characters of UTF-8 text, nothing
    # else. Refuse to write an entry that would fail it.
    if not 1 <= len(ENTRY) <= 200:
        raise ValueError(f"entry is {len(ENTRY)} characters, gate needs 1-200")
    # The bounty asks for exactly one sentence: a single terminal
    # full stop, no second sentence hiding after it.
    if ENTRY.count(".") != 1 or not ENTRY.endswith("."):
        raise ValueError("entry must be exactly one sentence")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8")
    print(ENTRY)


if __name__ == "__main__":
    main()
