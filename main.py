"""Office Artifacts: The One-Line Placard Contest.

Writes a single museum placard (one line, at most 180 characters) for an
ordinary office object treated as an ancient artifact, to /output/entry.txt.

The line was chosen from eight candidates by the winning-playbook method:
each candidate ends in a reversal, carries a specific mechanism with
concrete catalogue details (date, material, donor), and the two finalists
were compared head-to-head by a mock jury in both orders. The winner:

  Computer mouse, c. 950 BCE, carved ivory. The oracle answered every
  question by moving exactly where the priest's hand already was.
  Gift of IT.

The reversal: the oracle is not a prophet but a mirror -- it only ever
moves where the priest's hand already is, so its prophecies are redundant.
Deterministic, offline, standard library only.
"""

import os

ENTRY = (
    "Computer mouse, c. 950 BCE, carved ivory. "
    "The oracle answered every question by moving exactly where "
    "the priest's hand already was. Gift of IT."
)

MAX_CHARS = 180


def main() -> None:
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        raise ValueError("entry must be 1-180 characters, got %d" % len(ENTRY))
    if not ENTRY.strip():
        raise ValueError("entry must not be only whitespace")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Read back and confirm the file holds exactly the intended line.
    with open(path, "r", encoding="utf-8") as f:
        if f.read() != ENTRY:
            raise ValueError("entry.txt does not match the intended entry")


if __name__ == "__main__":
    main()
