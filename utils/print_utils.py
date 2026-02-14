def print_table(table: dict[str, list]) -> None:
    """Format and print the table. Assumes equal column lengths."""
    column_len = len(list(table.values())[0])
    if column_len == 0:
        for header in table:
            table[header].append("-")
        column_len = 1

    column_widths = {}
    for header, values in table.items():
        max_width = len(header)
        for value in values:
            max_width = max(max_width, len(str(value)))
        column_widths[header] = max_width

    # Print headers with underlines
    column_headers = table.keys()
    for index, header in enumerate(column_headers):
        print(header.ljust(column_widths[header]), end=" ")
    print()
    for index, header in enumerate(column_headers):
        print("-" * column_widths[header], end=" ")
    print()

    # Print rows with left-aligned cells
    for index in range(column_len):
        for header in column_headers:
            print(str(table[header][index]).ljust(column_widths[header]), end=" ")
        print()
