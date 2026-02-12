import os

from utils.path_utils import make_path_absolute


def mkdir(cwd: str, args: list[str]) -> None:
    if len(args) == 0:
        print("mkdir: missing a directory path")
        return

    for path in args:
        path = path.replace("/", "\\")
        path = make_path_absolute(cwd, path)
        try:
            os.mkdir(path)
        except OSError:
            print(f"mkdir: {path} contains a missing directory")
