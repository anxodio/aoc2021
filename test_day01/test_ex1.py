from pathlib import Path
from typing import List
import itertools


def measurement_increases_counter(measurements: List[int]) -> int:
    return sum(
        measurement2 > measurement1
        for measurement1, measurement2 in itertools.pairwise(measurements)
    )


def test_measurement_increases_counter():
    assert (
        measurement_increases_counter(
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
        == 7
    )


if __name__ == "__main__":
    with open((Path(__file__).parent / "input.txt")) as f:
        measurements = [int(line) for line in f.readlines()]
    print(measurement_increases_counter(measurements))
