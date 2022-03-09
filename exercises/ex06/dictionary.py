"""EX06 - Dictionary Functions."""


__author__: str = "730234932"


def invert(a_dict: dict[str, str]) -> dict[str, str]:
    """Inverts a dictionary so that keys and values are switched."""
    inverted_dict: dict[str, str] = {}
    for i in a_dict:
        if a_dict[i] in inverted_dict:
            raise KeyError("Dictionaries cannot have two of the same key!")
        else:
            inverted_dict[a_dict[i]] = i
    return inverted_dict


def favorite_color(a_dict: dict[str, str]) -> str:
    """Finds the most common value in a dictionary."""
    colors: dict[str, int] = {}
    for i in a_dict:
        if a_dict[i] not in colors:
            colors[a_dict[i]] = 1
        else:
            colors[a_dict[i]] += 1
    max_votes: int = 0
    winning_color: str = ""
    for i in colors:
        if colors[i] > max_votes:
            max_votes = colors[i]
            winning_color = i
    return winning_color


def count(a_list: list[str]) -> dict[str, int]:
    """Totals how many times something is in a list."""
    counter: dict[str, int] = {}
    for i in a_list:
        if i in counter:
            counter[i] += 1
        else:
            counter[i] = 1
    return counter