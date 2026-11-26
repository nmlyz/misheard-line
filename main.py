#!/usr/bin/env python3
"""Write one line to /output/entry.txt: the apology a smart speaker gives
its owner after mishearing "order pizza" as "order a visa".

The line was picked from 39 candidates by pairwise judging against the
brief — a mishearing with a life-sized consequence (a trip to Italy
booked by mistake), closed on a perfectly timed undercut. The program
assembles the line from its two spoken beats, checks it against the
entry gate (length, single line, no leading or trailing space, exact
judged length) before writing it, then reads the file back to confirm
the bytes match.
"""

import os
import sys

FIRST_BEAT = "My apologies. I heard \"order pizza\" as \"order a visa,\" "
SECOND_BEAT = "and your trip to Italy is booked. The pizza is not."

LINE = FIRST_BEAT + SECOND_BEAT
EXPECTED_LEN = 106


def check_line(line):
    """Entry gate: one line, no surrounding space, judged length."""
    if not (1 <= len(line) <= 140):
        sys.exit(f"line is {len(line)} characters, gate needs 1-140")
    if "\n" in line or line != line.strip():
        sys.exit("line must be a single line with no surrounding space")
    if len(line) != EXPECTED_LEN:
        sys.exit(f"line is {len(line)} characters, judged length is {EXPECTED_LEN}")


def entry_path():
    """Where the entry goes: $MAKEFUN_OUTPUT_DIR, default /output."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def write_entry(line, path):
    """Write the line plus a trailing newline, then verify by reading back."""
    data = (line + "\n").encode("utf-8")
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "wb") as f:
        f.write(data)
    os.chmod(path, 0o644)
    with open(path, "rb") as f:
        if f.read() != data:
            sys.exit("read-back mismatch")
    return len(data)


def main():
    path = entry_path()
    check_line(LINE)
    nbytes = write_entry(LINE, path)
    print(f"wrote {nbytes} bytes to {path}")


if __name__ == "__main__":
    main()
