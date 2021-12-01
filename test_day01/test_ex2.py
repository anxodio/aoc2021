from pathlib import Path
from typing import List, Iterable, Any, Generator
import itertools


def three_measurement_increases_counter(measurements: List[int]) -> int:
    return sum(
        three_sum2 > three_sum1  # type: ignore
        for three_sum1, three_sum2 in itertools.pairwise(
            map(sum, triplewise(measurements))
        )
    )


def triplewise(iterable: Iterable[Any]) -> Generator[tuple[Any, Any, Any], None, None]:
    iterable = iter(iterable)
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
