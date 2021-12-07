from pathlib import Path
from typing import List
from functools import cache


def count_lanterfishes(lanterfishes: List[int], days: int) -> int:
    return sum(count_lanterfish(lanterfish, days) for lanterfish in lanterfishes)


@cache
def count_lanterfish(lanterfish: int, days: int) -> int:
    total = 1
    for remaining_days in range(days, 0, -1):
        if lanterfish == 0:
            lanterfish = 7
            total += count_lanterfish(9, remaining_days)
        lanterfish -= 1
    return total


def test_count_lanterfishes():
    assert count_lanterfishes([3, 4, 3, 1, 2], 18) == 26
    assert count_lanterfishes([3, 4, 3, 1, 2], 256) == 26984457539


def test_count_lanterfish():
    assert count_lanterfish(3, 2) == 1
    assert count_lanterfish(3, 7) == 2
    assert count_lanterfish(3, 11) == 3
    assert count_lanterfish(3, 13) == 4


if __name__ == "__main__":
    with open((Path(__file__).parent / "input.txt")) as f:
        raw_lines = [line.rstrip("\n") for line in f]
    lanterfishes = [int(timer) for timer in raw_lines[0].split(",")]
    print(count_lanterfishes(lanterfishes, 256))
