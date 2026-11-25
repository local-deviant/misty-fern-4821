"""Make the AI Judge Laugh — one funny line about office life.

The joke: a new intern is told the office printer is haunted, so IT
stops getting tickets and the ghost takes the credit. True office
observation (interns, IT tickets, a broken printer), a surprising
turn, and the punch lands on the last word.

The program prints nothing to stdout; it writes the single joke line
to the output file named by ENTRY_OUTPUT (default /output/entry.txt).
Only the standard library is used, so the run needs nothing installed
and behaves the same on every machine that runs it.
"""

import os
from pathlib import Path

JOKE = (
    "I told the new intern the printer is haunted — now IT gets "
    "fewer tickets, and the ghost gets all the credit."
)


def _rejects(line: str) -> str | None:
    """Return a reason the line is invalid, or None when it is fine."""
    if not line or line.strip() != line:
        return "line is empty or has surrounding whitespace"
    if "\n" in line or "\r" in line:
        return "line spans more than one line"
    if len(line) >= 200:
        return "line is 200 characters or longer (task needs under 200)"
    if any(ord(ch) < 32 for ch in line):
        return "line contains a control character"
    return None


def main() -> None:
    problem = _rejects(JOKE)
    if problem is not None:
        raise ValueError(f"entry line rejected: {problem}")
    target = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
