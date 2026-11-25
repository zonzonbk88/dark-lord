"""The Tired Dark Lord: a 100-word villain monologue.

Writes one monologue to entry.txt in MAKEFUN_OUTPUT_DIR (or /output).
Standard library only. No trailing newline in the entry text.
"""

import os

MONOLOGUE = (
    "Three kingdoms knelt before my throne, and do you know what they left me? "
    "Forms. In triplicate. The dragon wants a raise. The orcs want dental. "
    "My own mother, bless her black heart, wants a word about the moat. I meant to raise the dead "
    "tonight. Instead I sign pardons for goblins who filed them wrong, again, "
    "and the ink is low, and the candle is low, and the night is... Look. "
    "Kneel, or don't. The throne is cold either way. But if you came to kill "
    "me, could we do it Tuesday? I have a meeting with the tax imps."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(MONOLOGUE)


if __name__ == "__main__":
    main()
