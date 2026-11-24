"""One-Liner Laugh Lab entry.

Assembles the single joke line from fragments, validates it against
the entry gate, then writes it with no trailing newline.
"""

import os
import sys


def assemble():
    lead_in = "In my defence,"
    takeover = "it was a hostile takeover"
    em_dash = "—"
    punch = "I am now 12% sock,"
    sign_off = "and HR has been notified."
    pieces = (lead_in, takeover, em_dash, punch, sign_off)
    return " ".join(pieces)


def gate_ok(candidate):
    if not candidate or not candidate.strip():
        return False
    if any(mark in candidate for mark in ("\n", "\r")):
        return False
    return 1 <= len(candidate) <= 200


def main():
    joke = assemble()
    if not gate_ok(joke):
        print("entry failed self-check", file=sys.stderr)
        return 1
    dest_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(dest_dir, exist_ok=True)
    dest_path = os.path.join(dest_dir, "entry.txt")
    with open(dest_path, "w", encoding="utf-8", newline="") as out_file:
        out_file.write(joke)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
