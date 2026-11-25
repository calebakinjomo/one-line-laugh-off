#!/usr/bin/env python3
"""One-Line Laugh-Off entry for make.fun bounty
u-zkhiel-one-line-laugh-off-714618ae.

Writes exactly one funny line to /output/entry.txt.
The line is a single joke that lands on a cold read:
it takes the familiar therapy phrase "embrace your mistakes"
absurdly literally — the punchline is a hug for the ex, not
self-growth. The twist arrives in the last three words, with
no setup notes and no explanation.
"""

import os

ENTRY = "My therapist told me to embrace my mistakes, so I hugged my ex."

def main():
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 200
    # characters, not only white space.
    assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} out of range"
    assert ENTRY.strip(), "entry must not be only white space"
    assert "\n" not in ENTRY.strip(), "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
