from collections import defaultdict
from datetime import datetime
from pathlib import Path

from utils.print_utils import print_table


def ls(cwd: str, args: list[str]) -> None:
    if len(args) > 0:
        print("ls: too many arguments")
        return

    column_headers = ["Size", "Last modified", "Path"]
    path_metadata = defaultdict(dict)
    for path in Path(cwd).iterdir():
        name = path.name
        if path.is_dir():
            name += "\\"

        stat = path.stat()
        path_metadata[name]["Size"] = str(stat.st_size) if path.is_file() else 0
        path_metadata[name]["Last modified"] = datetime.fromtimestamp(
            stat.st_mtime
        ).strftime(r"%Y-%m-%d %H:%M:%S")

    table = {header: [] for header in column_headers}
    for path, metadata in path_metadata.items():
        table["Size"].append(metadata["Size"])
        table["Last modified"].append(metadata["Last modified"])
        table["Path"].append(path)

    print_table(table)
