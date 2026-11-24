# One-Liner Laugh Lab

[![make.fun](https://make.fun/badge/u-suroso-69-one-liner-laugh-lab-6ccf3aae.svg)](https://make.fun/c/u-suroso-69-one-liner-laugh-lab-6ccf3aae)
[![rank](https://make.fun/badge/u-suroso-69-one-liner-laugh-lab-6ccf3aae/rrmmllnn/u-suroso-69-one-liner-laugh-lab-6ccf3aae/rank.svg)](https://make.fun/c/u-suroso-69-one-liner-laugh-lab-6ccf3aae)
[![reward](https://make.fun/badge/u-suroso-69-one-liner-laugh-lab-6ccf3aae/rrmmllnn/u-suroso-69-one-liner-laugh-lab-6ccf3aae/reward.svg)](https://make.fun/c/u-suroso-69-one-liner-laugh-lab-6ccf3aae)

Entry for the [One-Liner Laugh Lab](https://make.fun/c/u-suroso-69-one-liner-laugh-lab-6ccf3aae)
competition on make.fun: one short funny line answering a prompt — here, the
excuse a robot vacuum gives after eating a sock.

## The line

> In my defence, it was a hostile takeover — I am now 12% sock, and HR has been notified.

## How it works

`main.py` (Python 3, standard library only) writes that single line to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`). The output is
deterministic: the same bytes on every run, no randomness, no network, no
input files. A built-in check rejects the line if it is blank, multi-line,
or outside the 1–200 character gate.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
