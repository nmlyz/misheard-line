#!/usr/bin/env python3
"""Write one line to /output/entry.txt: the apology a smart speaker gives
its owner after mishearing "turn on the straighteners" as
"turn on the strangers".

The line was picked from 36 fresh candidates by pairwise judging against
the brief — a mishearing with an alarming, immediate consequence
(strangers in the bathroom), closed on a deadpan second beat: the device
calmly reassuring its owner that they are friendly. It also beat the
round 1 winner in a mock head-to-head on the same brief, so the round 2
entry carries this line instead of the round 1 line. The program
assembles the line from its two spoken beats, checks it against the
entry gate (length, single line, no leading or trailing space, exact
judged length) before writing it, then reads the file back to confirm
the bytes match.
"""

import os
import sys

FIRST_BEAT = "Sorry, I heard \"turn on the straighteners\" as \"turn on the strangers,\" "
SECOND_BEAT = "and there are now strangers in the bathroom. They are friendly."

LINE = FIRST_BEAT + SECOND_BEAT
EXPECTED_LEN = 134


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
