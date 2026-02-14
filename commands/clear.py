ANSI_CLEAR_CODE = "\033c"


def clear() -> None:
    print(ANSI_CLEAR_CODE, end="")
