from pathlib import Path

import os
import re


def write_cmake_words(root: Path) -> None:

    output: Path = root / "cmake_words.txt"

    words = set[str]()
    for dir, _, files in os.walk(root.as_posix()):
        for file in files:
            if file.endswith('.cmake'):
                with open(os.path.join(dir, file), 'r') as f:
                    content = f.read()
                    # Extract words (alphanumeric sequences)
                    words.update(re.findall(r'\b\w+\b', content))

    with output.open('w') as f:
        for word in sorted(words):
            _ = f.write(word + '\n')

if __name__ == "__main__":
    root: Path = Path("/home/xgreer/blender-git/blender")
    write_cmake_words(root)
