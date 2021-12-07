from pathlib import Path
from typing import List
from itertools import chain


def count_lanterfish(initial: List[int], days: int) -> int:
    lanterfishes = initial[:]
    for _ in range(days):
        lanterfishes = get_next_day(lanterfishes)
    return len(lanterfishes)


def get_next_day(lanterfishes: List[int]) -> List[int]:
    return list(
        chain.from_iterable(
            iterate_lanterfish(lanterfish) for lanterfish in lanterfishes
        )
    )


def iterate_lanterfish(lanterfish: int) -> List[int]:
    if lanterfish == 0:
        return [6, 8]
    return [lanterfish - 1]


def test_count_lanterfish():
    assert count_lanterfish([3, 4, 3, 1, 2], 18) == 26
    assert count_lanterfish([3, 4, 3, 1, 2], 80) == 5934


def test_get_next_day():
    assert sorted(get_next_day([2, 3, 2, 0, 1])) == sorted([1, 2, 1, 6, 0, 8])


def test_iterate_lanterfish():
    assert iterate_lanterfish(5) == [4]
    assert iterate_lanterfish(2) == [1]
    assert iterate_lanterfish(1) == [0]
    assert iterate_lanterfish(0) == [6, 8]


if __name__ == "__main__":
    with open((Path(__file__).parent / "input.txt")) as f:
        raw_lines = [line.rstrip("\n") for line in f]
    lanterfishes = [int(timer) for timer in raw_lines[0].split(",")]
    print(count_lanterfish(lanterfishes, 80))
