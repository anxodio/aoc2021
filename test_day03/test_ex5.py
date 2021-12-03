from pathlib import Path
from typing import List
from statistics import mode


def get_submarine_consumption(binary_strings: List[str]) -> int:
    transposed_binary_strings = transpose_list_of_strings(binary_strings)
    gamma_rate = "".join(
        mode(binary_string) for binary_string in transposed_binary_strings
    )
    espilon_rate = invert_binary_string(gamma_rate)
    return int(gamma_rate, 2) * int(espilon_rate, 2)


def transpose_list_of_strings(list_of_strings: List[str]) -> List[str]:
    return ["".join(row) for row in zip(*list_of_strings)]


def invert_binary_string(binary_string: str) -> str:
    return "".join(str(int(not bool(int(number)))) for number in binary_string)


def test_get_submarine_consumption():
    assert (
        get_submarine_consumption(
            [
                "00100",
                "11110",
                "10110",
                "10111",
                "10101",
                "01111",
                "00111",
                "11100",
                "10000",
                "11001",
                "00010",
                "01010",
            ]
        )
        == 198
    )


def test_transpose_list_of_strings():
    assert transpose_list_of_strings(["abc", "def", "ghi"]) == [
        "adg",
        "beh",
        "cfi",
    ]


def test_invert_binary_string():
    assert invert_binary_string("101") == "010"


if __name__ == "__main__":
    with open((Path(__file__).parent / "input.txt")) as f:
        binary_strings = [line.rstrip("\n") for line in f.readlines()]
    print(get_submarine_consumption(binary_strings))
