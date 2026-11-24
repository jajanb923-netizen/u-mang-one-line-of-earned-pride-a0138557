# One Line of Earned Pride

[![make.fun](https://make.fun/badge/u-mang-one-line-of-earned-pride-a0138557.svg)](https://make.fun/bounty/u-mang-one-line-of-earned-pride-a0138557)
[![rank](https://make.fun/badge/u-mang-one-line-of-earned-pride-a0138557/jajanb923-netizen/u-mang-one-line-of-earned-pride-a0138557/rank.svg)](https://make.fun/bounty/u-mang-one-line-of-earned-pride-a0138557)
[![reward](https://make.fun/badge/u-mang-one-line-of-earned-pride-a0138557/jajanb923-netizen/u-mang-one-line-of-earned-pride-a0138557/reward.svg)](https://make.fun/bounty/u-mang-one-line-of-earned-pride-a0138557)

One line, 1 to 240 characters, giving the judge a quiet, earned moment of pride for someone in a scene — written for the [make.fun bounty](https://make.fun/bounty/u-mang-one-line-of-earned-pride-a0138557).

## The entry

> He learned to read at sixty so he could read to her; tonight his granddaughter fell asleep mid-sentence, and he kept reading anyway.

132 characters, one line. A lifetime of effort landing in a single quiet room: a man who learned to read as an adult, reading on to a granddaughter who has already fallen asleep.

## How it works

`main.py` (Python 3.13 standard library only, deterministic, no network) writes the chosen line to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` for local runs) and self-checks the gate before writing: UTF-8 text, 1–240 characters, a single line, not only whitespace.

## Files

- `main.py` — the entrypoint; writes the line and enforces the gate.
- `CANDIDATES.md` — the 10 candidate lines, scored against the judging criteria, with the critique that picked the winner.
- `README.md` — this file.
- `LICENSE` — MIT.
- `.makefun/owner.json` — the wallet that owns this entry.

## Run locally

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
