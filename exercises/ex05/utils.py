"""EX05 - 'list' Utility Functions."""


__author__: str = "730234932"


def only_evens(numbers: list[int]) -> list[int]:
    """Test if a number in a given list is even."""
    evens: list[int] = []
    for number in numbers:
        if number % 2 == 0:
            evens.append(number)
    return evens


def sub(a_list: list[int], a: int, b: int) -> list[int]:
    """Takes a list and returns the items at idicies a and b."""
    results: list[int] = []
    for item in a_list:
        if a_list.index(item) >= a and a_list.index(item) <= (b - 1):
            results.append(item)
    return results


def concat(a_list: list[int], b_list: list[int]) -> list[int]:
    """Combines two lists of integers, the first and then the second returned."""
    new_list: list[int] = []
    for item in a_list:
        new_list.append(item)
    for item in b_list:
        new_list.append(item)
    return new_list