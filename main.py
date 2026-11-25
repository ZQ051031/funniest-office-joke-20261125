"""Entry for make.fun: The Funniest Office Joke, Judged Head to Head.

The whole entry is one short line about office life. This program
writes that line, and nothing else, to /output/entry.txt.

The gate the scorer checks: the file must be UTF-8 text of 1 to 200
characters, not only whitespace. So the joke is validated here before
it is written -- single line, inside the length limit, no trailing
newline -- and the program is fully deterministic: same input, same
bytes, every run. Only the Python standard library is used.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")

JOKE = (
    "My performance review said I need to be more visible at work, "
    "so now I reply-all to everything."
)

MAX_CHARS = 200


def build_entry() -> str:
    """Return the entry text, checked against the competition gate."""
    if not JOKE.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in JOKE:
        raise ValueError("entry must be a single line")
    if len(JOKE) > MAX_CHARS:
        raise ValueError(f"entry is {len(JOKE)} chars, over the {MAX_CHARS} limit")
    return JOKE


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(build_entry(), encoding="utf-8", newline="")


if __name__ == "__main__":
    main()
