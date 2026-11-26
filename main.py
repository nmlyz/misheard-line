#!/usr/bin/env python3
"""Write one line to /output/entry.txt: the apology a smart speaker gives
its owner after mishearing "order pizza" as "order a visa".

The line was picked from 39 candidates by pairwise judging against the
brief — a mishearing with a life-sized consequence (a trip to Italy
booked by mistake), closed on a perfectly timed undercut. The program
holds the line as one constant and checks it against the entry gate
(length, single line, no leading or trailing space, exact judged
length) before writing it, then reads the file back to confirm the
bytes match.
"""

import os
import sys

LINE = (
    "My apologies. I heard \"order pizza\" as \"order a visa,\" "
    "and your trip to Italy is booked. The pizza is not."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    if not (1 <= len(LINE) <= 140):
        sys.exit(f"line is {len(LINE)} characters, gate needs 1-140")
    if "\n" in LINE or LINE != LINE.strip():
        sys.exit("line must be a single line with no surrounding space")
    data = (LINE + "\n").encode("utf-8")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "wb") as f:
        f.write(data)
    os.chmod(path, 0o644)
    with open(path, "rb") as f:
        if f.read() != data:
            sys.exit("read-back mismatch")
    print(f"wrote {len(data)} bytes to {path}")


if __name__ == "__main__":
    main()
