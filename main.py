"""One-line cat joke entry for make.fun.

Writes a single one-line joke about cats to /output/entry.txt.
Python 3.13 standard library only, no network at run time.
"""

import os

JOKE = (
    "My cat knocked my coffee off the table, looked at the mess, "
    "and blamed the dog \u2014 who died in 2019."
)


def main() -> None:
    # Gate assertions: the entry must be exactly one non-empty line of
    # 1-200 characters, matching the competition's sealed gate.
    assert JOKE, "joke must not be empty"
    assert "\n" not in JOKE, "joke must be a single line"
    assert JOKE == JOKE.strip(), "joke must not have leading/trailing whitespace"
    assert 1 <= len(JOKE) <= 200, "joke must be 1-200 characters"
    output_path = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
