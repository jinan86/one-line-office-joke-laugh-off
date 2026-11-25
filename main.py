#!/usr/bin/env python3
"""One-Line Office Joke Laugh-Off entry.

Writes a single original one-line office joke to /output/entry.txt.

The joke: Finance rejects "emotional damage" as an expense category, so
the narrator resubmits it as "team building" -- a sharp, surprising
punchline about office life, instantly clear on one read, with no
overused office cliche (no plants, no printers, no meetings, no
"per my last email", no pizza-party raises).
"""

JOKE = (
    "Finance rejected 'emotional damage' as an expense category, "
    "so I resubmitted it as 'team building'."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = JOKE
    assert 1 <= len(text) <= 200, "joke must be 1-200 characters"
    assert text.strip(), "joke must not be only whitespace"
    assert "\n" not in text, "joke must be a single line"
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
