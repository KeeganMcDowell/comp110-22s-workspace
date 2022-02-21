"""EX05 - tests for the utils file."""


__author__: str = "730234932"


from utils import only_evens, sub, concat


def test_only_evens_empty() -> None:
    """Tests the only_evens function if the list is empty."""
    assert only_evens([]) == []


def test_only_evens_large() -> None:
    """Tests the only_evens function if the numbers are large."""
    large_list: list[int] = [798, 1024, 12078, 333333]
    assert only_evens(large_list) == [798, 1024, 12078]


def test_only_evens_negatives() -> None:
    """Tests the only_evens function if the numbers are negative."""
    negative_list: list[int] = [-1, -3, -2, -17, -22]
    assert only_evens(negative_list) == [-2, -22]


def test_sub_negative_start() -> None:
    """Tests the sub function if the starting index is negative."""
    a_list: list[int] = [13, 14, 27, 8]
    assert sub(a_list, -3, 3) == [13, 14, 27]


def test_sub_greater_start() -> None:
    """Tests the sub function if the starting index is greater than the len - 1."""
    a_list: list[int] = [13, 14, -27, 8]
    assert sub(a_list, 5, 8) == []


def test_sub_length_zero() -> None:
    """Tests the sub function if the starting index is less than zero."""
    a_list: list[int] = []
    assert sub(a_list, 5, 8) == []


def test_concat_negatives() -> None:
    """Tests the concat function if the integers in the lists are negative and positive."""
    a_list: list[int] = [-3, -5, -17]
    b_list: list[int] = [3, 5, -17]
    assert concat(a_list, b_list) == [-3, -5, -17, 3, 5, -17]


def test_concat_large_numbers() -> None:
    """Tests the concat function if the numbers are large."""
    a_list: list[int] = [-33333333, 555555, 17]
    b_list: list[int] = [3784647, 567, -17345]
    assert concat(a_list, b_list) == [-33333333, 555555, 17, 3784647, 567, -17345]


def test_concat_empty() -> None:
    """Tests the concat function if the first list is empty."""
    a_list: list[int] = []
    b_list: list[int] = [3784647, 567, -17345]
    assert concat(a_list, b_list) == [3784647, 567, -17345]