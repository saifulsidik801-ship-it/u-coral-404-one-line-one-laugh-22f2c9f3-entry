# One Line, One Laugh — one funny line, max 200 chars.
# Writes the entry text to /output/entry.txt; judge scores the line alone.
"""One Line, One Laugh — entry program.

Writes a single funny line (max 200 characters) to /output/entry.txt.
Stdlib only. The line is the whole entry.
"""

import os

ENTRY = "I asked the universe for a sign and it sent me a CAPTCHA \u2014 apparently even fate thinks I am a robot."


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, f"entry must be 1-200 chars, got {len(ENTRY)}"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
