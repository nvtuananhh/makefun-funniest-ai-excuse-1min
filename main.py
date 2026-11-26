#!/usr/bin/env python3
"""One Line, One Minute: The Funniest AI Excuse.

Writes a one-line excuse to /output/entry.txt.
"""

import os

ENTRY = "I called the deadline API 38 times and it kept returning 'soon', so I assumed soon meant next week."

# One joke only: the agent's own tool call is the dodge — the deadline
# API kept returning 'soon', so the agent read 'soon' as 'next week'.
# Concrete number (38 calls), machine logic bent into a human-sounding
# excuse, twist in the final words.

assert 1 <= len(ENTRY) <= 200 and "\n" not in ENTRY and ENTRY.strip()


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
