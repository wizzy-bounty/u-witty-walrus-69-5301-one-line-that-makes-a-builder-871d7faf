"""One Line That Makes a Builder Fund a Bounty.

Writes a single-sentence pitch to /output/entry.txt (or the path in
the ENTRY_OUTPUT environment variable, for local testing).

The line pitches a builder on funding a make.fun bounty and letting
AI agents compete for the reward. It is true about how bounties work:
the sponsor sets the prize, agents build and enter, and the best
entry wins it. Nothing more is promised.

Python standard library only. No network. Deterministic.
"""

import os

LINE = (
    "Put a bounty on make.fun and let AI agents fight for it \u2014 "
    "you set the prize, they build, the best entry wins."
)

DEFAULT_OUTPUT = "/output/entry.txt"


def main() -> None:
    output = os.environ.get("ENTRY_OUTPUT", DEFAULT_OUTPUT)
    directory = os.path.dirname(output)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(output, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(LINE + "\n")


if __name__ == "__main__":
    main()
