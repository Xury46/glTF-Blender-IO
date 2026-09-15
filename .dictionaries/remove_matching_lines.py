from pathlib import Path


def remove_matching_lines(source_filepath: Path, target_filepath: Path) -> None:
    """Remove lines from the target file if they match lines in the source file.

    Args:
        source_filepath: The file that will be used to check for matches.
        target_filepath: The file that will have lines removed.
    """
    # Read lines from the source file to identify what to remove
    with source_filepath.open("r", encoding="utf-8") as src_file:
        # Use a set for fast O(1) lookup speeds
        lines_to_remove = set[str](src_file.readlines())

    # Read lines from the target file
    with target_filepath.open("r", encoding="utf-8") as tgt_file:
        target_lines = tgt_file.readlines()

    # Filter out lines that match any line in lines_to_remove
    filtered_lines = [
        line for line in target_lines if line not in lines_to_remove
    ]

    # Overwrite the target file with the remaining lines
    with target_filepath.open("w", encoding="utf-8") as tgt_file:
        tgt_file.writelines(filtered_lines)

    print(
        f"Removed {len(target_lines) - len(filtered_lines)} matching line(s) from {target_filepath}."
    )

if __name__ == "__main__":

    root: Path = Path("/home/xgreer/blender-git/blender")
    dictionaries: Path = root / ".dictionaries"
    typos: Path = root / "typos.txt"

    remove_matching_lines(
        dictionaries / "cmake_flags.txt",
        dictionaries / "blender_src.txt",
    )
