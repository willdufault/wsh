import re


def make_path_absolute(cwd: str, path: str) -> str:
    is_absolute_path = re.match(r"(.:)?\\", path) is not None
    return path if is_absolute_path else f"{cwd}\\{path}"
