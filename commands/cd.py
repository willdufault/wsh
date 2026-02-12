from pathlib import Path


def cd(cwd: str, args: list[str]) -> str:
    if len(args) == 0:
        return cwd

    if len(args) > 1:
        print("cd: too many arguments")
        return cwd

    path_parts = cwd.split("\\")
    arg_parts = args[0].replace("/", "\\").split("\\")
    if arg_parts[0] == "":
        path_parts = [path_parts[0]]
    arg_parts = list(filter(lambda part: part != "", arg_parts))

    for part in arg_parts:
        match part:
            case ".":
                pass
            case "..":
                if len(path_parts) > 1:
                    path_parts.pop()
            case _:
                path_parts.append(part)

    new_path = Path("\\".join(path_parts))
    if not new_path.is_dir():
        print(f"cd: {new_path} is not a recognized directory")
        return cwd

    new_cwd = str(new_path)
    # Needed to properly handle "C:"
    if "\\" not in new_cwd:
        new_cwd += "\\"
    return new_cwd
