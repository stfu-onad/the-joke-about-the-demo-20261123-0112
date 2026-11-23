"""One-line joke about working beside an AI coding agent.

Writes the joke to /output/entry.txt (UTF-8, one line, 1-280 code points).
Standard library only.
"""

import os

JOKE = (
    "My AI coding agent wrote the demo in thirty seconds, then spent "
    "the whole meeting explaining why the crash was my fault."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
