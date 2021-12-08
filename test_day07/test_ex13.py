from pathlib import Path
from typing import List
from statistics import median


def get_minimum_alignement_fuel(positions: List[int]) -> int:
    best_position = int(median(positions))
    return sum(abs(pos - best_position) for pos in positions)


def test_get_minimum_alignement_fuel():
    assert get_minimum_alignement_fuel([16, 1, 2, 0, 4, 2, 7, 1, 2, 14]) == 37


if __name__ == "__main__":
    with open((Path(__file__).parent / "input.txt")) as f:
        raw_lines = [line.rstrip("\n") for line in f]
    positions = [int(position) for position in raw_lines[0].split(",")]
    print(get_minimum_alignement_fuel(positions))
