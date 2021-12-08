from pathlib import Path
from typing import List, Tuple
from statistics import mean
from math import floor, ceil


def get_minimum_alignement_fuel(positions: List[int]) -> Tuple[int, int]:
    best_position_floor = floor(mean(positions))
    best_position_ceil = ceil(mean(positions))
    return (
        sum(
            (abs(pos - best_position_floor) * (abs(pos - best_position_floor) + 1) // 2)
            for pos in positions
        ),
        sum(
            (abs(pos - best_position_ceil) * (abs(pos - best_position_ceil) + 1) // 2)
            for pos in positions
        ),
    )


def test_get_minimum_alignement_fuel():
    assert 168 in get_minimum_alignement_fuel([16, 1, 2, 0, 4, 2, 7, 1, 2, 14])


if __name__ == "__main__":
    with open((Path(__file__).parent / "input.txt")) as f:
        raw_lines = [line.rstrip("\n") for line in f]
    positions = [int(position) for position in raw_lines[0].split(",")]
    print(get_minimum_alignement_fuel(positions))
