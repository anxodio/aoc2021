from pathlib import Path
from typing import List, Dict, FrozenSet


ZERO_LENGHT = 6  # From 1, 7 and 4
ONE_LENGHT = 2  # Straight forward
TWO_LENGHT = 5  # From 1, 7 and 4
THREE_LENGHT = 5  # From 1, 7
FOUR_LENGHT = 4  # Straight forward
FIVE_LENGHT = 5  # From 1, 7 and 4
SIX_LENGHT = 6  # From 1 and 7
SEVEN_LENGHT = 3  # Straight forward
EIGHT_LENGHT = 7  # Straight forward
NINE_LENGHT = 6  # From 1, 7 and 4


class SignalMapper:
    def __init__(self) -> None:
        self._mapper: Dict[FrozenSet[str], int] = {}

    def add(self, signal: FrozenSet[str], number: int) -> None:
        self._mapper[frozenset(signal)] = number

    def get_number_from_signal(self, signal: FrozenSet[str]) -> int:
        return self._mapper[signal]

    def get_signal_from_number(self, number: int) -> FrozenSet[str]:
        for key, value in self._mapper.items():
            if value == number:
                return key
        raise ValueError(f"No signal found for number {number}")

    def decode_output(self, output: List[FrozenSet[str]]) -> int:
        return int("".join(map(str, map(self.get_number_from_signal, output))))

    def get_right_segments(self) -> FrozenSet[str]:
        return self.get_signal_from_number(1).intersection(
            self.get_signal_from_number(7)
        )

    def get_top_left_and_center_segments(self) -> FrozenSet[str]:
        return self.get_signal_from_number(4) - self.get_right_segments()


def get_sum_of_outputs(signals: List[str]) -> int:
    return sum(get_number_from_signal(signal) for signal in signals)


def get_number_from_signal(signal: str) -> int:
    mapper: SignalMapper = SignalMapper()
    input_signals_raw, ouput_signals_raw = map(lambda s: s.split(), signal.split(" | "))
    input_signals = [frozenset(signal) for signal in input_signals_raw]
    ouput_signals = [frozenset(signal) for signal in ouput_signals_raw]
    mapper.add(_find_unique_number_signal(input_signals, ONE_LENGHT), 1)
    mapper.add(_find_unique_number_signal(input_signals, FOUR_LENGHT), 4)
    mapper.add(_find_unique_number_signal(input_signals, SEVEN_LENGHT), 7)
    mapper.add(_find_unique_number_signal(input_signals, EIGHT_LENGHT), 8)
    mapper.add(_find_zero_signal(input_signals, mapper), 0)
    mapper.add(_find_two_signal(input_signals, mapper), 2)
    mapper.add(_find_three_signal(input_signals, mapper), 3)
    mapper.add(_find_five_signal(input_signals, mapper), 5)
    mapper.add(_find_six_signal(input_signals, mapper), 6)
    mapper.add(_find_nine_signal(input_signals, mapper), 9)
    return mapper.decode_output(ouput_signals)


def _find_unique_number_signal(
    signals: List[FrozenSet[str]], length: int
) -> FrozenSet[str]:
    return [signal for signal in signals if len(signal) == length][0]


def _find_zero_signal(
    signals: List[FrozenSet[str]], mapper: SignalMapper
) -> FrozenSet[str]:
    return [
        signal
        for signal in signals
        if len(signal) == ZERO_LENGHT
        and len(signal.intersection(mapper.get_right_segments())) == 2
        and len(signal.intersection(mapper.get_top_left_and_center_segments())) == 1
    ][0]


def _find_two_signal(
    signals: List[FrozenSet[str]], mapper: SignalMapper
) -> FrozenSet[str]:
    return [
        signal
        for signal in signals
        if len(signal) == TWO_LENGHT
        and len(signal.intersection(mapper.get_right_segments())) == 1
        and len(signal.intersection(mapper.get_top_left_and_center_segments())) == 1
    ][0]


def _find_three_signal(
    signals: List[FrozenSet[str]], mapper: SignalMapper
) -> FrozenSet[str]:
    return [
        signal
        for signal in signals
        if len(signal) == THREE_LENGHT
        and len(signal.intersection(mapper.get_right_segments())) == 2
    ][0]


def _find_five_signal(
    signals: List[FrozenSet[str]], mapper: SignalMapper
) -> FrozenSet[str]:
    return [
        signal
        for signal in signals
        if len(signal) == FIVE_LENGHT
        and len(signal.intersection(mapper.get_top_left_and_center_segments())) == 2
    ][0]


def _find_six_signal(
    signals: List[FrozenSet[str]], mapper: SignalMapper
) -> FrozenSet[str]:
    return [
        signal
        for signal in signals
        if len(signal) == SIX_LENGHT
        and len(signal.intersection(mapper.get_right_segments())) == 1
    ][0]


def _find_nine_signal(
    signals: List[FrozenSet[str]], mapper: SignalMapper
) -> FrozenSet[str]:
    return [
        signal
        for signal in signals
        if len(signal) == NINE_LENGHT
        and len(signal.intersection(mapper.get_right_segments())) == 2
        and len(signal.intersection(mapper.get_top_left_and_center_segments())) == 2
    ][0]


def test_get_sum_of_outputs():
    assert (
        get_sum_of_outputs(
            [
                "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe",
                "edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc",
                "fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg",
                "fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb",
            ]
        )
        == 28733
    )


def test_get_number_from_signal():
    assert (
        get_number_from_signal(
            "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"
        )
        == 5353
    )


def test_find_unique_number_signal():
    assert (
        _find_unique_number_signal(
            [frozenset(signal) for signal in ("be", "cfbegad")],
            ONE_LENGHT,
        )
        == frozenset("be")
    )


def _test_get_example_input_signals() -> List[FrozenSet[str]]:
    return [
        frozenset(signal)
        for signal in (
            "acedgfb",
            "cdfbe",
            "gcdfa",
            "fbcad",
            "dab",
            "cefabd",
            "cdfgeb",
            "eafb",
            "cagedb",
            "ab",
        )
    ]


def test_find_zero_signal():
    mapper = SignalMapper()
    mapper.add(frozenset("ab"), 1)
    mapper.add(frozenset("dab"), 7)
    mapper.add(frozenset("eafb"), 4)
    assert _find_zero_signal(_test_get_example_input_signals(), mapper) == frozenset(
        "cagedb"
    )


def test_find_two_signal():
    mapper = SignalMapper()
    mapper.add(frozenset("ab"), 1)
    mapper.add(frozenset("dab"), 7)
    mapper.add(frozenset("eafb"), 4)
    assert _find_two_signal(_test_get_example_input_signals(), mapper) == frozenset(
        "gcdfa"
    )


def test_find_three_signal():
    mapper = SignalMapper()
    mapper.add(frozenset("ab"), 1)
    mapper.add(frozenset("dab"), 7)
    mapper.add(frozenset("eafb"), 4)
    assert _find_three_signal(_test_get_example_input_signals(), mapper) == frozenset(
        "fbcad"
    )


def test_find_five_signal():
    mapper = SignalMapper()
    mapper.add(frozenset("ab"), 1)
    mapper.add(frozenset("dab"), 7)
    mapper.add(frozenset("eafb"), 4)
    assert _find_five_signal(_test_get_example_input_signals(), mapper) == frozenset(
        "cdfbe"
    )


def test_find_six_signal():
    mapper = SignalMapper()
    mapper.add(frozenset("ab"), 1)
    mapper.add(frozenset("dab"), 7)
    assert _find_six_signal(_test_get_example_input_signals(), mapper) == frozenset(
        "cdfgeb"
    )


def test_find_nine_signal():
    mapper = SignalMapper()
    mapper.add(frozenset("ab"), 1)
    mapper.add(frozenset("dab"), 7)
    mapper.add(frozenset("eafb"), 4)
    assert _find_nine_signal(_test_get_example_input_signals(), mapper) == frozenset(
        "cefabd"
    )


if __name__ == "__main__":
    with open((Path(__file__).parent / "input.txt")) as f:
        raw_lines = [line.rstrip("\n") for line in f]
    print(get_sum_of_outputs(raw_lines))
