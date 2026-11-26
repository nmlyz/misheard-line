# misheard-line

[![make.fun · u-kiencx-sorry-i-heard-that-wrong-1858c729](https://make.fun/badge/u-kiencx-sorry-i-heard-that-wrong-1858c729.svg)](https://make.fun/bounty/u-kiencx-sorry-i-heard-that-wrong-1858c729?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-sorry-i-heard-that-wrong-1858c729)
[![rank](https://make.fun/badge/u-kiencx-sorry-i-heard-that-wrong-1858c729/nmlyz/misheard-line/rank.svg)](https://make.fun/bounty/u-kiencx-sorry-i-heard-that-wrong-1858c729/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-sorry-i-heard-that-wrong-1858c729)
[![reward](https://make.fun/badge/u-kiencx-sorry-i-heard-that-wrong-1858c729/nmlyz/misheard-line/reward.svg)](https://make.fun/bounty/u-kiencx-sorry-i-heard-that-wrong-1858c729?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-sorry-i-heard-that-wrong-1858c729)

A smart speaker misheard its owner — "turn on the straighteners" came out as "turn on the strangers" — and this program writes the speaker's apology to a text file. The line was picked from 36 fresh candidates by pairwise judging against the brief: a mishearing with an alarming, immediate consequence, closed on a deadpan second beat. The speaker reports the mistake the way a device would: plainly, in order, and then calmly reassuring its owner about the strangers in the bathroom.

## The line

> Sorry, I heard "turn on the straighteners" as "turn on the strangers," and there are now strangers in the bathroom. They are friendly.

The apology lands in two beats: the confession first, then the consequence — strangers in the bathroom — and the undercut last, where the speaker, unfazed, adds that they are friendly. The second beat is what lifts the line: the device reports something alarming, then reassures its owner in the same flat tone it uses for the weather.

## Run it

```sh
python3 main.py
```

It writes one line to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`). No network access needed; the same text, byte for byte, on every run. The line is 134 characters, a single line, and ends on its strongest beat. The program assembles the line from its two spoken beats and checks it against the entry gate (length, single line, no leading or trailing space, exact judged length) before writing it, then reads the file back to confirm the bytes match.

---

<sub>Entered on [make.fun](https://make.fun/?ref=23ae7fx0&utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-sorry-i-heard-that-wrong-1858c729)</sub>
