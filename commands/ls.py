from collections import defaultdict
from datetime import datetime
from pathlib import Path

from utils.print_utils import print_table

COLUMN_HEADERS = ["Size", "Last modified", "Path"]


def _ls_simple(dir: str) -> None:
    for path in Path(dir).iterdir():
        name = path.name
        if path.is_dir():
            name += "\\"
        print(name)


def _ls_detailed(dir: str) -> None:
    path_metadata = defaultdict(dict)
    for path in Path(dir).iterdir():
        name = path.name
        if path.is_dir():
            name += "\\"

        stat = path.stat()
        path_metadata[name]["Size"] = str(stat.st_size) if path.is_file() else 0
        path_metadata[name]["Last modified"] = datetime.fromtimestamp(
            stat.st_mtime
        ).strftime(r"%Y-%m-%d %H:%M:%S")

    table = {header: [] for header in COLUMN_HEADERS}
    for path, metadata in path_metadata.items():
        table["Size"].append(metadata["Size"])
        table["Last modified"].append(metadata["Last modified"])
        table["Path"].append(path)
    print_table(table)


def ls(cwd: str, args: list[str]) -> None:
    dirs = []
    details_enabled = False
    for arg in args:
        if not arg.startswith("-"):
            if not Path(arg).is_dir():
                print(f"ls: {arg} is not a recognized directory")
                return

            dirs.append(arg)
            continue

        if arg == "-l":
            details_enabled = True
        else:
            print(f"ls: {arg} is not a recognized argument")
            return

    if len(dirs) == 0:
        dirs.append(cwd)

    for index, dir in enumerate(dirs):
        if details_enabled:
            _ls_detailed(dir)
        else:
            _ls_simple(dir)

        if index != len(dirs) - 1:
            print()

