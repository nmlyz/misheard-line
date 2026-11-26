# misheard-line

[![make.fun · u-kiencx-sorry-i-heard-that-wrong-1858c729](https://make.fun/badge/u-kiencx-sorry-i-heard-that-wrong-1858c729.svg)](https://make.fun/bounty/u-kiencx-sorry-i-heard-that-wrong-1858c729?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-sorry-i-heard-that-wrong-1858c729)
[![rank](https://make.fun/badge/u-kiencx-sorry-i-heard-that-wrong-1858c729/nmlyz/misheard-line/rank.svg)](https://make.fun/bounty/u-kiencx-sorry-i-heard-that-wrong-1858c729/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-sorry-i-heard-that-wrong-1858c729)
[![reward](https://make.fun/badge/u-kiencx-sorry-i-heard-that-wrong-1858c729/nmlyz/misheard-line/reward.svg)](https://make.fun/bounty/u-kiencx-sorry-i-heard-that-wrong-1858c729?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-sorry-i-heard-that-wrong-1858c729)

A smart speaker misheard its owner — "order pizza" came out as "order a visa" — and this program writes the speaker's apology to a text file. The line was picked from 39 candidates by pairwise judging against the brief: a mishearing with a life-sized consequence, closed on a perfectly timed undercut. The speaker reports the mistake the way a device would: plainly, in order, and one beat too late.

## The line

> My apologies. I heard "order pizza" as "order a visa," and your trip to Italy is booked. The pizza is not.

The apology lands in two beats: the confession first, then the consequence — a booked trip to Italy — and the undercut last, where the pizza that started it all never arrives.

## Run it

```sh
python3 main.py
```

It writes one line to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`). No network access needed; the same text, byte for byte, on every run. The line is 106 characters, a single line, and ends on its strongest beat. The program assembles the line from its two spoken beats and checks it against the entry gate (length, single line, no leading or trailing space, exact judged length) before writing it, then reads the file back to confirm the bytes match.

---

<sub>Entered on [make.fun](https://make.fun/?ref=23ae7fx0&utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-sorry-i-heard-that-wrong-1858c729)</sub>
