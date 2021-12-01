from pathlib import Path
from typing import List, Iterable, Any
import itertools
import functools


def three_measurement_increases_counter(measurements: List[int]) -> int:
    last_sum: int = 999999999  # Arbitrary large number
    counter: int = 0
    for m1, m2, m3 in triplewise(measurements):
        if m1 + m2 + m3 > last_sum:
            counter += 1
        last_sum = m1 + m2 + m3
    return counter


def triplewise(iterable: Iterable[Any]) -> tuple[Any, Any, Any]:
    "Return overlapping triplets from an iterable"
    # Recipe from https://docs.python.org/3/library/itertools.html
    # triplewise('ABCDEFG') -> ABC BCD CDE DEF EFG
    for (a, _), (b, c) in itertools.pairwise(itertools.pairwise(iterable)):
        yield a, b, c


def test_three_measurement_increases_counter():
    assert (
        three_measurement_increases_counter(
            [
                199,
                200,
                208,
                210,
                200,
                207,
                240,
                269,
                260,
                263,
            ]
        )
        == 5
    )


if __name__ == "__main__":
    with open((Path(__file__).parent / "input.txt")) as f:
        measurements = [int(line) for line in f.readlines()]
    print(three_measurement_increases_counter(measurements))
