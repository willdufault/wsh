from pathlib import Path

from utils.path_utils import contains_illegal_chars, get_abs_path


def touch(cwd: str, args: list[str]) -> None:
    if len(args) == 0:
        print("touch: missing a filepath")
        return

    for path in args:
        path = path.replace("/", "\\")
        if contains_illegal_chars(path):
            print(f"touch: {path} contains illegal characters")
            continue

        if path.endswith("\\"):
            print(f"touch: {path} can't be a directory")
            continue

        abs_path = get_abs_path(cwd, path)
        if Path(abs_path).exists():
            print(f"touch: {path} already exists")
            continue

        with open(abs_path, "w") as _:
            pass
