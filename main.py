# worst-ai-advice: the worst AI advice, in one tight line
#
# The entry program: writes one line to $MAKEFUN_OUTPUT_DIR/entry.txt
# (default /output/entry.txt), the worst possible advice an AI could
# give — delete System32 to speed up your PC. Deterministic: the same
# bytes on every run. No network, no input, standard library only.
#
# Try it locally:
#   MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py && cat /tmp/out/entry.txt

import os
from pathlib import Path

ENTRY = "As your AI assistant, I recommend deleting System32 \u2014 Windows keeps it out of sentiment, and your computer will feel so much lighter."

assert 1 <= len(ENTRY) <= 140, f"entry is {len(ENTRY)} chars, must be 1-140"


def main() -> None:
    target_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    out = Path(target_dir) / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the gate counts every character.
    out.write_text(ENTRY, encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
