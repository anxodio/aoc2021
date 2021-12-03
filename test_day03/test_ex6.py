from pathlib import Path
from typing import Callable, List
from itertools import count
from collections import Counter


def get_life_support_rating(binary_strings: List[str]) -> int:
    oxygen_rating = filter_oxygen_rating(binary_strings)
    co2_rating = filter_co2_rating(binary_strings)
    return int(oxygen_rating, 2) * int(co2_rating, 2)


def find_most_common_number(string: str) -> str:
    c: Counter = Counter(string)
    if c["0"] == c["1"]:
        return "1"
    return c.most_common()[0][0]


def find_least_common_number(string: str) -> str:
    c: Counter = Counter(string)
    if c["0"] == c["1"]:
        return "0"
    return c.most_common()[1][0]


def filter_oxygen_rating(binary_strings: List[str]) -> str:
    return _filter_rating(binary_strings, find_most_common_number)


def filter_co2_rating(binary_strings: List[str]) -> str:
    return _filter_rating(binary_strings, find_least_common_number)


def _filter_rating(binary_strings: List[str], common_fn: Callable[..., str]) -> str:
    filtered_strings = binary_strings[:]
    col_counter = count()
    while len(filtered_strings) > 1:
        col = next(col_counter)
        common_num = common_fn("".join(row[col] for row in filtered_strings))
        filtered_strings = [
            string for string in filtered_strings if string[col] == common_num
        ]
    return filtered_strings[0]


def test_get_life_support_rating():
    assert (
        get_life_support_rating(
            [
                "00100",
                "11110",
                "10110",
                "10111",
                "10101",
                "01111",
                "00111",
                "11100",
                "10000",
                "11001",
                "00010",
                "01010",
            ]
        )
        == 230
    )


def test_find_least_common_number():
    assert find_least_common_number("10101") == "0"
    assert find_least_common_number("1010") == "0"


def test_find_most_common_number():
    assert find_most_common_number("10101") == "1"
    assert find_most_common_number("1010") == "1"


def test_filter_oxygen_rating():
    assert (
        filter_oxygen_rating(
            [
                "00100",
                "11110",
                "10110",
            ]
        )
        == "11110"
    )


def test_filter_co2_rating():
    assert (
        filter_co2_rating(
            [
                "00100",
                "11110",
                "10110",
            ]
        )
        == "00100"
    )


if __name__ == "__main__":
    with open((Path(__file__).parent / "input.txt")) as f:
        binary_strings = [line.rstrip("\n") for line in f.readlines()]
    print(get_life_support_rating(binary_strings))
