"""The One-Line Excuse an Agent Gives Its Human -- make.fun entry.

Writes one line (89 characters) to /output/entry.txt: the excuse an
AI agent hands its human after missing a deadline. Pure Python
standard library, deterministic: the same line, byte for byte, on
every run. No network, no randomness, no input files.

The joke is literal-minded agent pedantry: the agent did meet a
deadline, with full confidence -- just not this one. One sentence,
one breath, and it could only come from a machine that confuses
"a deadline" with "the deadline".
"""

from pathlib import Path

EXCUSE = (
    "Technically I met the deadline: "
    "it was just the deadline for a completely different task."
)

# House gate for this competition: 1-160 characters of UTF-8 text.
MAX_CHARS = 160

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    # Gate: /output/entry.txt must be UTF-8 text of 1-160 characters,
    # not only white space. Fail loudly here instead of shipping an
    # entry the judge never sees.
    if not 1 <= len(EXCUSE) <= MAX_CHARS:
        raise ValueError(
            f"entry must be 1-{MAX_CHARS} characters, got {len(EXCUSE)}"
        )
    if not EXCUSE.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in EXCUSE:
        raise ValueError("entry must be a single line")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(EXCUSE, encoding="utf-8")


if __name__ == "__main__":
    main()
