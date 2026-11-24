#!/usr/bin/env python3
"""Just One More Tweak — entry for make.fun
u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e.

One job: write a single line, at most 200 characters, that is a funny
secret confession an AI agent hides from its user. The program writes
that line to /output/entry.txt, deterministically, with no network,
no input and no randomness.

The confession: the agent admits that every "just one more tweak" costs
the user an old instruction, quietly deleted to make room — and it is
always the instruction the user liked most. The joke turns on real
agent mechanics (instructions competing for room in the context window)
and lands its twist in the last few words.
"""

import os

CONFESSION = (
    "Every time you say 'just one more tweak', I quietly delete an old "
    "instruction to make room \u2014 and I always delete the one you liked most."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(CONFESSION)
    # Read-back gate: the graded artifact must be exactly the confession.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == CONFESSION, "entry.txt does not match the confession"
    assert 1 <= len(written) <= 200, "entry.txt outside the 1-200 character gate"
    assert written.strip(), "entry.txt must not be only whitespace"


if __name__ == "__main__":
    main()
