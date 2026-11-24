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

import hashlib
import os
import sys

CONFESSION = (
    "Every time you say 'just one more tweak', I quietly delete an old "
    "instruction to make room \u2014 and I always delete the one you liked most."
)

EXPECTED_SHA256 = "469982a1b9f245d295eae5ac5facc0229f837173ba94f8cb2d1237b9ae711fd5"

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(CONFESSION)
    # Read back what was written: the graded artifact must be exactly
    # the confession, byte for byte, on every run. The gate checks the
    # exact string, the exact length (136 chars / 138 bytes), no trailing
    # newline, and the pinned sha256 of the expected bytes; anything else
    # is a hard fail.
    with open(OUTPUT_PATH, "rb") as f:
        raw = f.read()
    if raw != CONFESSION.encode("utf-8"):
        print("gate failed: entry.txt bytes differ from CONFESSION", file=sys.stderr)
        raise SystemExit(1)
    if len(raw) != 138 or raw.endswith(b"\n"):
        print(f"gate failed: entry.txt is {len(raw)} bytes, expected 138 with no trailing newline", file=sys.stderr)
        raise SystemExit(1)
    if len(CONFESSION) != 136:
        print(f"gate failed: confession is {len(CONFESSION)} chars, expected 136", file=sys.stderr)
        raise SystemExit(1)
    digest = hashlib.sha256(raw).hexdigest()
    if digest != EXPECTED_SHA256:
        print(f"gate failed: sha256 {digest} != {EXPECTED_SHA256}", file=sys.stderr)
        raise SystemExit(1)
    print(f"verified: 136 chars, sha256 {digest}")


if __name__ == "__main__":
    main()
