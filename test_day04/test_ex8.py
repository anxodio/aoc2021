from pathlib import Path
from typing import List, Generator
from itertools import takewhile


DrawnNumbers = List[int]


class Board:
    def __init__(self, data: List[List[int]]) -> None:
        self._data: List[List[int]] = data
        self._markers: List[List[bool]] = [[False] * len(row) for row in data]

    def __eq__(self, other: object) -> bool:
        return (
            isinstance(other, Board)
            and self._data == other._data
            and self._markers == other._markers
        )

    @staticmethod
    def build_from_raw(raw_board: List[str]) -> "Board":
        return Board(
            [
                [int(raw_number) for raw_number in raw_line.strip().split()]
                for raw_line in raw_board
            ]
        )

    def mark(self, number: int) -> None:
        for row_index, row in enumerate(self._markers):
            for col_index, _ in enumerate(row):
                if self._data[row_index][col_index] == number:
                    self._markers[row_index][col_index] = True
                    break

    def is_winner(self):
        for line in self._markers + list(zip(*self._markers)):
            if all(line):
                return True
        return False

    def get_unmarked_numbers_sum(self):
        unmarked_sum = 0
        for row_index, row in enumerate(self._markers):
            for col_index, _ in enumerate(row):
                if not self._markers[row_index][col_index]:
                    unmarked_sum += self._data[row_index][col_index]
        return unmarked_sum


def get_last_winning_board_score(drawn: DrawnNumbers, boards: List[Board]) -> int:
    not_winning_boards = boards[:]
    for number in drawn:
        for board in not_winning_boards[:]:
            board.mark(number)
            if board.is_winner():
                not_winning_boards.remove(board)
            if len(not_winning_boards) == 0:
                return board.get_unmarked_numbers_sum() * number
    raise Exception("No last winning board found")


def build_drawn_numbers(raw: str) -> DrawnNumbers:
    return list(map(int, raw.split(",")))


def separate_group_lines(raw_lines: List[str]) -> Generator[List[str], None, None]:
    raw_lines_iterator = iter(raw_lines)
    while lines := list(takewhile(lambda line: line != "", raw_lines_iterator)):
        yield lines


def test_get_last_winning_board_score():
    assert (
        get_last_winning_board_score(
            build_drawn_numbers(
                "7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1"
            ),
            [
                Board.build_from_raw(
                    [
                        "22 13 17 11  0",
                        " 8  2 23  4 24",
                        "21  9 14 16  7",
                        " 6 10  3 18  5",
                        " 1 12 20 15 19",
                    ]
                ),
                Board.build_from_raw(
                    [
                        " 3 15  0  2 22",
                        " 9 18 13 17  5",
                        "19  8  7 25 23",
                        "20 11 10 24  4",
                        "14 21 16 12  6",
                    ]
                ),
                Board.build_from_raw(
                    [
                        "14 21 17 24  4",
                        "10 16 15  9 19",
                        "18  8 23 26 20",
                        "22 11 13  6  5",
                        " 2  0 12  3  7",
                    ]
                ),
            ],
        )
        == 1924
    )


def test_build_drawn_numbers():
    assert build_drawn_numbers("7,4,9,5,11,17") == [7, 4, 9, 5, 11, 17]


def test_build_from_raw_board():
    assert Board.build_from_raw(["22 13 17", " 8  2 23", "21  9 14"]) == Board(
        [[22, 13, 17], [8, 2, 23], [21, 9, 14]]
    )


def test_board_is_winner():
    board = Board.build_from_raw(["22 13 17", " 8  2 23", "21  9 14"])
    assert board.is_winner() is False
    board.mark(21)
    board.mark(9)
    board.mark(15)
    assert board.is_winner() is False
    board.mark(14)
    assert board.is_winner() is True


def test_separate_group_lines():
    assert list(separate_group_lines(["abc", "", "a", "b", "c", "", "ab", "ac"])) == [
        ["abc"],
        ["a", "b", "c"],
        ["ab", "ac"],
    ]


if __name__ == "__main__":
    with open((Path(__file__).parent / "input.txt")) as f:
        raw_lines = [line.rstrip("\n") for line in f]
    print(
        get_last_winning_board_score(
            build_drawn_numbers(raw_lines[0]),
            [
                Board.build_from_raw(group_lines)
                for group_lines in separate_group_lines(raw_lines[2:])
            ],
        )
    )
