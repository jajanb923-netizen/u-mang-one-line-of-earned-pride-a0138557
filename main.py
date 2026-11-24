"""One Line of Earned Pride.

Writes one line -- a quiet, earned moment of pride for someone in a
scene -- to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt for
local runs).

Python 3.13 standard library only. Deterministic, no network, no secrets.
The entry is self-checked against the competition gate before it is
written: UTF-8 text, 1 to 240 characters, a single line, not only
whitespace.
"""

import os
import sys

# The chosen line (see CANDIDATES.md for the full field of 10 and the
# scoring that picked it): a man who learned to read at sixty so he could
# read to his granddaughter, reading on after she has fallen asleep
# mid-sentence. A lifetime of effort landing in one quiet room -- the
# strongest line in the field on the judge's first criterion, genuine
# earned pride. Winner of the critique round, 24/25.
LINE_PARTS = (
    "He learned to read at sixty so he could read to her;",
    "tonight his granddaughter fell asleep mid-sentence,",
    "and he kept reading anyway.",
)

MAX_CHARS = 240


def build_entry():
    """Join the line's clauses into the single submitted line."""
    return " ".join(LINE_PARTS)


def check_gate(text):
    """Enforce the competition gate; raise ValueError on any failure."""
    failures = []
    if not isinstance(text, str):
        failures.append("entry is not text")
    else:
        if not 1 <= len(text) <= MAX_CHARS:
            failures.append(
                "entry is %d characters, gate allows 1-%d" % (len(text), MAX_CHARS)
            )
        if text.strip() == "":
            failures.append("entry is only whitespace")
        if "\n" in text or "\r" in text:
            failures.append("entry must be a single line")
        try:
            text.encode("utf-8")
        except UnicodeEncodeError:
            failures.append("entry is not valid UTF-8")
    if failures:
        raise ValueError("; ".join(failures))
    return text


def main():
    entry = check_gate(build_entry())
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(entry + "\n")
    print("wrote %s (%d characters)" % (path, len(entry)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
