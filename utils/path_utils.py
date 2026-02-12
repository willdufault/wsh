import re


def get_abs_path(cwd: str, path: str) -> str:
    is_absolute_path = re.match(r"(.:)?\\", path) is not None
    return path if is_absolute_path else f"{cwd}\\{path}"


def contains_illegal_chars(path: str) -> bool:
    return re.fullmatch(r"[a-zA-Z0-9\-_.\\]+", path) is None
