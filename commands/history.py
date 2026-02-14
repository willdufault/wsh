from utils.print_utils import print_table


def history(command_history: list[str]) -> None:
    column_headers = ["Id", "Command"]
    table = {header: [] for header in column_headers}
    for index, command in enumerate(command_history):
        table["Id"].append(index + 1)
        table["Command"].append(command)

    print_table(table)
