from pathlib import Path
from typing import List


ONE_LENGHT = 2
FOUR_LENGHT = 4
SEVEN_LENGHT = 3
EIGHT_LENGHT = 7


def count_easy_digits(signals: List[str]) -> int:
    total_easy_digits = 0
    for signal in signals:
        output_values = signal.split(" | ")[1].split()
        for output_value in output_values:
            if len(output_value) in (
                ONE_LENGHT,
                FOUR_LENGHT,
                SEVEN_LENGHT,
                EIGHT_LENGHT,
            ):
                total_easy_digits += 1
    return total_easy_digits


def test_count_easy_digits():
    assert (
        count_easy_digits(
            [
                "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe",
                "edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc",
                "fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg",
                "fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb",
            ]
        )
        == 9
    )


if __name__ == "__main__":
    with open((Path(__file__).parent / "input.txt")) as f:
        raw_lines = [line.rstrip("\n") for line in f]
    print(count_easy_digits(raw_lines))
