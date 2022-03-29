"""Dictionary related utility functions."""

__author__ = "730234932"

from csv import DictReader


# Define your functions below
def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a table."""
    result: list[dict[str, str]] = []

    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")

    # Prepare to read the data file as a CSV rather than just strings
    csv_reader = DictReader(file_handle)

    # Read each row of the CSV line by lie
    for row in csv_reader:
        result.append(row)

    # Close the file when we're done, to free its resources.
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result


def head(column_table: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """Takes the first N rows of a table."""
    result: dict[str, list[str]] = {}

    for col in column_table:
        n_values: list[str] = []
        
        column = column_table[col]

        i: int = 0
        while i < rows and i < len(column):
            n_values.append(column[i])
            i += 1
        result[col] = n_values
    return result


def select(column_table: dict[str, list[str]], a_list: list[str]) -> dict[str, list[str]]:
    """Allows you to view only certain columns within a column-based table."""
    result: dict[str, list[str]] = {}

    for column in a_list:
        if column in column_table:
            result[column] = column_table[column]
    
    return result


def concat(table_1: dict[str, list[str]], table_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Combines two column-based tables."""
    result: dict[str, list[str]] = {}

    for col in table_1:
        result[col] = table_1[col]
    
    for col in table_2:
        titles = table_2[col][0]

        if col in result:
            result[col].append(titles)
        else:
            result[col] = table_2[col]

    return result