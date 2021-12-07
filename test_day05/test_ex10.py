from pathlib import Path
from typing import List, Dict
from dataclasses import dataclass
from collections import defaultdict


@dataclass(frozen=True)
class Coordinates:
    x: int
    y: int


@dataclass(frozen=True)
class VentLine:
    start: Coordinates
    end: Coordinates

    @staticmethod
    def from_raw_string(raw_string: str) -> "VentLine":
        raw_start, raw_end = raw_string.split(" -> ")
        start_x, start_y = [int(x) for x in raw_start.split(",")]
        end_x, end_y = [int(x) for x in raw_end.split(",")]
        return VentLine(Coordinates(start_x, start_y), Coordinates(end_x, end_y))

    def get_all_coordinates(self) -> List[Coordinates]:
        x_range = list(
            range(self.start.x, self.end.x + 1)
            if self.start.x < self.end.x
            else range(self.start.x, self.end.x - 1, -1)
        )
        y_range = list(
            range(self.start.y, self.end.y + 1)
            if self.start.y < self.end.y
            else range(self.start.y, self.end.y - 1, -1)
        )
        if len(x_range) == 1 or len(y_range) == 1:
            return [Coordinates(x, y) for x in x_range for y in y_range]
        return [Coordinates(x, y) for x, y in zip(x_range, y_range)]


def get_number_of_overlapping_points(vent_lines: List[VentLine]) -> int:
    space: Dict[Coordinates, int] = defaultdict(int)
    for line in vent_lines:
        for point in line.get_all_coordinates():
            space[point] += 1
    return sum(1 for point in space.values() if point > 1)


def test_get_number_of_overlapping_points():
    assert (
        get_number_of_overlapping_points(
            [
                VentLine.from_raw_string("0,9 -> 5,9"),
                VentLine.from_raw_string("8,0 -> 0,8"),
                VentLine.from_raw_string("9,4 -> 3,4"),
                VentLine.from_raw_string("2,2 -> 2,1"),
                VentLine.from_raw_string("7,0 -> 7,4"),
                VentLine.from_raw_string("6,4 -> 2,0"),
                VentLine.from_raw_string("0,9 -> 2,9"),
                VentLine.from_raw_string("3,4 -> 1,4"),
                VentLine.from_raw_string("0,0 -> 8,8"),
                VentLine.from_raw_string("5,5 -> 8,2"),
            ]
        )
        == 12
    )


def test_ventline_from_raw_string():
    assert VentLine.from_raw_string("1,1 -> 3,3") == VentLine(
        Coordinates(1, 1), Coordinates(3, 3)
    )


def test_ventile_get_all_coordinates():
    assert VentLine.from_raw_string("1,1 -> 1,3").get_all_coordinates() == [
        Coordinates(1, 1),
        Coordinates(1, 2),
        Coordinates(1, 3),
    ]
    assert VentLine.from_raw_string("9,7 -> 7,7").get_all_coordinates() == [
        Coordinates(9, 7),
        Coordinates(8, 7),
        Coordinates(7, 7),
    ]
    assert VentLine.from_raw_string("1,1 -> 3,3").get_all_coordinates() == [
        Coordinates(1, 1),
        Coordinates(2, 2),
        Coordinates(3, 3),
    ]
    assert VentLine.from_raw_string("9,7 -> 7,9").get_all_coordinates() == [
        Coordinates(9, 7),
        Coordinates(8, 8),
        Coordinates(7, 9),
    ]


if __name__ == "__main__":
    with open((Path(__file__).parent / "input.txt")) as f:
        raw_lines = [line.rstrip("\n") for line in f]
    vent_lines = [VentLine.from_raw_string(line) for line in raw_lines]
    print(get_number_of_overlapping_points(vent_lines))
