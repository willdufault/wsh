import os
from pathlib import Path

from utils.path_utils import contains_illegal_chars, get_abs_path


def mkdir(cwd: str, args: list[str]) -> None:
    if len(args) == 0:
        print("mkdir: missing a directory path")
        return

    for path in args:
        path = path.replace("/", "\\")
        if contains_illegal_chars(path):
            print(f"touch: {path} contains illegal characters")
            continue

        abs_path = get_abs_path(cwd, path)

        if Path(abs_path).exists():
            print(f"mkdir: {path} already exists")
            continue

        try:
            os.mkdir(abs_path)
        except OSError:
            print(f"mkdir: {path} contains a missing directory")
