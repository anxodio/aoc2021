from pathlib import Path
from typing import List, Tuple


def get_final_multiplied_position(instructions: List[str]) -> int:
    horitzontal, depth = 0, 0
    for instruction in instructions:
        delta = _calculate_delta(instruction)
        horitzontal, depth = horitzontal + delta[0], depth + delta[1]
    return horitzontal * depth


def _calculate_delta(instruction: str) -> Tuple[int, int]:
    action, number = instruction.split(" ")
    if action == "forward":
        return int(number), 0
    elif action == "down":
        return 0, int(number)
    else:
        return 0, -int(number)


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
        == 150
    )


if __name__ == "__main__":
    with open((Path(__file__).parent / "input.txt")) as f:
        instructions = [line.rstrip("\n") for line in f.readlines()]
    print(get_final_multiplied_position(instructions))
