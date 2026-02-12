from datetime import datetime
from pathlib import Path
from collections import defaultdict


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
        path_metadata[name]["Size"] = str(stat.st_size) if path.is_file() else "0"
        path_metadata[name]["Last modified"] = datetime.fromtimestamp(
            stat.st_mtime
        ).strftime(r"%Y-%m-%d %H:%M:%S")

    column_widths = {header: len(header) for header in column_headers}
    for path, metadata in path_metadata.items():
        column_widths["Path"] = max(column_widths["Path"], len(path))
        for column_header, value in metadata.items():
            column_widths[column_header] = max(
                column_widths[column_header], len(metadata[column_header])
            )

    for index, header in enumerate(column_headers):
        print(
            header.ljust(column_widths[header]),
            end=" " if index != len(column_headers) - 1 else "\n",
        )
    for index, header in enumerate(column_headers):
        print(
            "-" * column_widths[header],
            end=" " if index != len(column_headers) - 1 else "\n",
        )

    if len(path_metadata) == 0:
        path_metadata["-"] = {
            header: "-" for header in column_headers if header != "Path"
        }

    for path, metadata in path_metadata.items():
        for column_header, value in metadata.items():
            print(value.ljust(column_widths[column_header]), end=" ")
        print(path.ljust(column_widths["Path"]))
