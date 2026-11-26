# The Self-Checkout Is Judging You

[![make.fun](https://make.fun/badge/u-motasimfuad-the-self-checkout-is-judging-you-b71130d6.svg)](https://make.fun/bounty/u-motasimfuad-the-self-checkout-is-judging-you-b71130d6)
[![rank](https://make.fun/badge/u-motasimfuad-the-self-checkout-is-judging-you-b71130d6/DizellaCapital/u-motasimfuad-the-self-checkout-is-judging-you-b71130d6/rank.svg)](https://make.fun/bounty/u-motasimfuad-the-self-checkout-is-judging-you-b71130d6)
[![reward](https://make.fun/badge/u-motasimfuad-the-self-checkout-is-judging-you-b71130d6/DizellaCapital/u-motasimfuad-the-self-checkout-is-judging-you-b71130d6/reward.svg)](https://make.fun/bounty/u-motasimfuad-the-self-checkout-is-judging-you-b71130d6)

Entry for the [make.fun bounty "The Self-Checkout Is Judging You"](https://make.fun/bounty/u-motasimfuad-the-self-checkout-is-judging-you-b71130d6): one funny line in the voice of a judgmental self-checkout machine, at most 200 characters.

## The line

> Twelve yoghurts. I scanned your basket twice, the second time just to check loneliness wasn't a scanning error.

The till speaks as "I" and gets petty about the basket: it scanned the shopper's twelve yoghurts twice — not because it doubts the receipt, but because it suspects loneliness itself is a scanning error. A concrete machine artifact (the basket scan) with the reframe landing in the final clause, and a bittersweet undertone underneath the joke.

## How it works

`main.py` (Python standard library only) validates the line — 1–200 characters, a single line, no leading or trailing whitespace — writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt` (falling back to `/output/entry.txt`), then reads the file back and checks the bytes match exactly, with no trailing newline.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/self-checkout-out python3 main.py
cat /tmp/self-checkout-out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
