from utils.path_utils import make_path_absolute


def cat(cwd: str, args: list[str]) -> None:
    for path in args:
        path = path.replace("/", "\\")
        path = make_path_absolute(cwd, path)
        try:
            with open(path) as file:
                print(file.read())
        except OSError:
            print(f"cat: {path} is not a recognized filepath")
