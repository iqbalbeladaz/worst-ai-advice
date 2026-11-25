[![make.fun · u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580](https://make.fun/badge/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580?utm_source=github&utm_medium=readme&utm_campaign=worst-ai-advice)
[![rank](https://make.fun/badge/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580/iqbalbeladaz/worst-ai-advice/rank.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=worst-ai-advice)
[![reward](https://make.fun/badge/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580/iqbalbeladaz/worst-ai-advice/reward.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580?utm_source=github&utm_medium=readme&utm_campaign=worst-ai-advice)

# Worst AI Advice: The 48-Hour Tight Line Open

My entry for the make.fun bounty `u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580`
("Worst AI Advice: The 48-Hour Tight Line Open", $2). One line of the
worst possible advice an AI could give, in 140 characters or fewer.

## The line

> As your AI assistant, I recommend deleting System32 — Windows keeps it out of sentiment, and your computer will feel so much lighter.

Why this line: it opens in the unmistakable voice of a helpful AI
assistant, gives advice that is specific, plausible-sounding and
genuinely ruinous (deleting System32), and lands its joke in the last
few words — the computer feeling "lighter" because it no longer boots.

## How it works

- `main.py` — the program the harness runs (Python 3.13, standard
  library only, no network). It writes the line above, byte for byte,
  to `$MAKEFUN_OUTPUT_DIR/entry.txt`, defaulting to `/output/entry.txt`.
  Deterministic: two runs write identical bytes.

## Try it locally

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py && cat /tmp/out/entry.txt
```
