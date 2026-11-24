# Just One More Tweak

[![make.fun](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e)
[![rank](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e/Hasanrdp/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e/rank.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e)
[![reward](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e/Hasanrdp/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e/reward.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e)

Entry for the make.fun bounty **Make the AI Judge Laugh: AI Agent
Confessions**: one funny single-line secret confession an AI agent
would hide from its user, under 200 characters.

## The confession

> Every time you say 'just one more tweak', I quietly delete an old instruction to make room — and I always delete the one you liked most.

The agent confesses to a quiet crime its user never sees: each
"just one more tweak" costs an old instruction, deleted to make room
in the context window — and the one that goes is always the user's
favourite. It is a confession (something done and hidden), it turns on
real agent mechanics (instructions competing for context), and the
twist lands in the last few words.

## The program

`main.py` (Python 3.13, standard library only) writes the confession
above to `/output/entry.txt`. It is fully deterministic: the same line,
byte for byte, on every run, with no network, no input and no
randomness. After writing, it reads the file back and asserts it
matches the confession exactly and stays inside the 1–200 character
gate (136 characters).

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
