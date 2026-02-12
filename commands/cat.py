from utils.path_utils import get_abs_path


def cat(cwd: str, args: list[str]) -> None:
    for path in args:
        path = path.replace("/", "\\")
        abs_path = get_abs_path(cwd, path)
        try:
            with open(abs_path) as file:
                print(file.read())
        except OSError:
            print(f"cat: {path} is not a recognized filepath")
