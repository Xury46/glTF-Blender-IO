from pathlib import Path
from typing import Literal


def categorize(word: str) -> Literal[0, 1, 2]:
    if word.isupper():
        return 0
    elif any(c.isupper() for c in word):
        return 1
    else:
        return 2


def main(input_file: Path, output_file: Path) -> None:

    words: list[str]
    with input_file.open("r") as f:
        words = [line.strip() for line in f if line.strip()]

    # Group variants by their casefold.
    groups: dict[str, list[str]] = {}
    for word in words:
        groups.setdefault(word.casefold(), []).append(word)

    # Pick the best variant from each group.
    result: list[str] = [min(variants, key=categorize) for variants in groups.values()]

    with output_file.open("w") as f:
        _ = f.write("\n".join(result) + "\n")

    print(f"Wrote {len(result)} unique words to {output_file}")


if __name__ == "__main__":
    root: Path = Path("/home/xgreer/blender-git/blender")
    dictionaries: Path = root / ".dictionaries"

    for item in dictionaries.iterdir():
        if item.is_file() and item.suffix == ".txt":
            main(
                item,
                item,
            )
