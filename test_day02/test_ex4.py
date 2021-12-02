from pathlib import Path
from typing import List
from dataclasses import dataclass


@dataclass
class Position:
    horizontal: int
    depth: int
    aim: int


def get_final_multiplied_position(instructions: List[str]) -> int:
    position: Position = Position(0, 0, 0)
    for instruction in instructions:
        position = _calculate_next_position(position, instruction)
    return position.horizontal * position.depth


def _calculate_next_position(position: Position, instruction: str) -> Position:
    action, number = instruction.split(" ")
    if action == "up":
        return Position(position.horizontal, position.depth, position.aim - int(number))
    elif action == "down":
        return Position(position.horizontal, position.depth, position.aim + int(number))
    else:
        return Position(
            position.horizontal + int(number),
            position.depth + (position.aim * int(number)),
            position.aim,
        )


def test_get_final_multiplied_position():
    assert (
        get_final_multiplied_position(
            [
                "forward 5",
                "down 5",
                "forward 8",
                "up 3",
                "down 8",
                "forward 2",
            ]
        )
        == 900
    )


if __name__ == "__main__":
    with open((Path(__file__).parent / "input.txt")) as f:
        instructions = [line.rstrip("\n") for line in f.readlines()]
    print(get_final_multiplied_position(instructions))
