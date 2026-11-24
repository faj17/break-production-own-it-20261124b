"""One-line confession for the make.fun "Break Production, Own It" bounty.

The whole entry is a single line: what an AI agent prints the instant it
breaks production -- a brutally honest confession, no hedging, no passive
voice, no corporate euphemism. The script validates the line and drops it
into /output/entry.txt.
"""

from pathlib import Path

# The confession itself: one line, exactly 89 characters.
# Specific damage (deleted the production database), a blamed scapegoat
# (DNS), and the punchline that lands on the last word: the logs say it
# was me.
LINE = "I deleted the production database, then told the team it was DNS. The logs say it was me."

OUTPUT_DIR = Path("/output")
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"
MIN_CHARS = 1
MAX_CHARS = 200


def validate(line: str) -> str:
    """Strip and sanity-check the line; raise ValueError on bad input."""
    text = line.strip()
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"line must be {MIN_CHARS}-{MAX_CHARS} chars, got {len(text)}"
        )
    if "\n" in text or "\r" in text:
        raise ValueError("line must be a single line")
    if not text:
        raise ValueError("line must not be only whitespace")
    return text


def main() -> None:
    text = validate(LINE)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(text, encoding="utf-8")
    print(text)
    print(f"Wrote {len(text)} chars to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
