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


def less_than(col: list[float], threshold: float) -> list[bool]:
    result: list[bool] = []
    for item in col:
        result.append(item < threshold)
    
    return result


def mean(col: list[str]) -> float:
    ints: list[int] = []

    for item in col:
        ints.append(int(item))

    return sum(ints) / len(ints)


def several_means(table: dict[str, list[str]], cols: list[str]) -> None:
    
    for item in cols:
        item_mean = mean(table[item])
        print(f"{item} mean: {item_mean}")


def col_ints(col: list[str]) -> list[int]:
    results: list[int] = []

    for item in col:
        results.append(int(item))

    return results


def count(value_list: list[str]) -> dict[str, int]:
    results: dict[str, int] = {}
    
    for item in value_list:
        if item in results:
            results[item] += 1
        else:
            results[item] = 1

    return results