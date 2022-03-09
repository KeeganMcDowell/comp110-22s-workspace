"""EX06 - Dictionary Functions unit tests."""


__author__: str = "730234932"


import pytest
from dictionary import invert, favorite_color, count


def test_invert_empty() -> None:
    """Tests the invert function with an empty dictionary."""
    assert invert({}) == {}


def test_invert_char() -> None:
    """Tests invert when items are individual characters."""
    assert invert({'a': 'z', 'b': 'y', 'c': 'x'}) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_invert_phrases() -> None:
    """Tests invert when items are phrases."""
    assert invert({'cat in the hat': 'thing 1'}) == {'thing 1': 'cat in the hat'}


with pytest.raises(KeyError):
    """Tests whether the KeyError is raised."""
    my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
    invert(my_dictionary)


def test_favorite_color_empty() -> None:
    """Tests the favorite color function with an empty dictionary."""
    assert favorite_color({}) == ""


def test_favorite_color_one() -> None:
    """Tests favorite color when there is only one entry."""
    assert favorite_color({'Keegan': 'purple'}) == "purple"


def test_favorite_color_tie() -> None:
    """Tests favorite color when there is a tie."""
    assert favorite_color({'Keegan': 'purple', 'Bruna': 'blue'}) == "purple"


def test_count_empty() -> None:
    """Tests the count function with an empty list."""
    assert count([]) == {}


def test_count_small() -> None:
    """Tests count with a few values."""
    assert count(['purple']) == {'purple': 1}


def test_count_lot() -> None:
    """Tests count with a lot of values."""
    assert count(
        ['purple', 'green', 'tomato', 'pie', 'chips', 'korea', 'purple']) == {
            'purple': 2, 'green': 1, 'tomato': 1, 'pie': 1, 'chips': 1, 'korea': 1
    }