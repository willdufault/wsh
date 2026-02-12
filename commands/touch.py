import os

from utils.path_utils import make_path_absolute


def touch(cwd: str, args: list[str]) -> None:
    if len(args) == 0:
        print("touch: missing a filepath")
        return

    for path in args:
        path = path.replace("/", "\\")
        path = make_path_absolute(cwd, path)
        if path.endswith("\\"):
            print(f"touch: {path} can't be a directory")
            continue

        with open(path, "w") as _:
            pass
