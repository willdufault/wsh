from utils.print_utils import print_table

COLUMN_HEADERS = ["Id", "Command"]


def history(command_history: list[str]) -> None:
    table = {header: [] for header in COLUMN_HEADERS}
    for index, command in enumerate(command_history):
        table["Id"].append(index + 1)
        table["Command"].append(command)

    print_table(table)
