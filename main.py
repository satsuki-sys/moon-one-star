#!/usr/bin/env python3
"""Write a one-star review of the Moon to /output/entry.txt.

Entry for the make.fun competition "The Moon Gets One Star":
a single one-star review, 120 characters at most.

The review complains about the Moon itself and only the Moon could
earn it: it drags the whole ocean around twice a day (the tides),
changes shape every week (the phases), and still gets called
romantic. One star, for being controlling.
"""

import os

ENTRY = "★☆☆☆☆ Drags the whole ocean around twice a day, changes shape weekly, and still gets called romantic. Controlling."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
