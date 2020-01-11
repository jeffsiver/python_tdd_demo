from typing import List, Tuple


class BowlingScore:
    def __init__(self, pins_down: List[Tuple[int, ...]]):
        self._pins_down = pins_down

    def get_score(self) -> int:
        score = 0
        for frame_number in range(1,11):
            score += self._get_score_for_frame(frame_number)
        return score

    def _get_score_for_frame(self, frame_number: int) -> int:
        if self._does_frame_have_strike(frame_number):
            return self._calculate_frame_score_for_strike(frame_number)
        if self._does_frame_have_spare(frame_number):
            return  self._calculate_frame_score_for_spare(frame_number)
        pins_down_in_frame = self._pins_down[frame_number - 1]
        return pins_down_in_frame[0] + pins_down_in_frame[1]

    def _does_frame_have_strike(self, frame_number) -> bool:
        if self._pins_down[frame_number-1][0] == 10:
            return True
        return False

    def _does_frame_have_spare(self, frame_number: int) -> bool:
        pins_in_frame = self._pins_down[frame_number-1]
        if pins_in_frame[0] + pins_in_frame[1] == 10:
            return True
        return False

    def _is_last_frame(self, frame_number: int) -> bool:
        return frame_number == 10

    def _calculate_frame_score_for_strike(self, frame_number: int) -> int:
        if self._is_last_frame(frame_number):
            return 10 + self._pins_down[frame_number-1][1] + self._pins_down[frame_number-1][2]
        if self._does_frame_have_strike(frame_number+1):
            return 20 + self._pins_down[frame_number+1][0]
        return 10 + self._pins_down[frame_number][0] + self._pins_down[frame_number][1]

    def _calculate_frame_score_for_spare(self, frame_number: int) -> int:
        if self._is_last_frame(frame_number):
            return 10 + self._pins_down[frame_number-1][2]
        return 10 + self._pins_down[frame_number][0]


class TestBowlingScore:
    def test_get_score_when_all_gutters(self):
        pins_down = [(0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), ]
        score = BowlingScore(pins_down).get_score()
        assert score == 0

    def test_get_score_when_no_spares_or_strikes(self):
        pins_down = [(1,2), (3,4), (5,3), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), ]
        score = BowlingScore(pins_down).get_score()
        assert score == 18

    def test_get_score_when_with_spares_and_no_strikes(self):
        pins_down = [(1,2), (3,4), (5,5), (1,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), ]
        score = BowlingScore(pins_down).get_score()
        assert score == 22

    def test_get_score_when_with_strikes_without_following_strikes(self):
        pins_down = [(1,2), (3,4), (10, ), (1,3), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), ]
        score = BowlingScore(pins_down).get_score()
        assert score == 28

    def test_get_score_when_with_two_strikes_in_a_row(self):
        pins_down = [(1,2), (3,4), (10, ), (10, ), (1,3), (0,0), (0,0), (0,0), (0,0), (0,0), ]
        score = BowlingScore(pins_down).get_score()
        assert score == 49

    def test_get_score_when_with_three_strikes_in_a_row(self):
        pins_down = [(1,2), (3,4), (10, ), (10, ), (10, ), (1,3), (0,0), (0,0), (0,0), (0,0), ]
        score = BowlingScore(pins_down).get_score()
        assert score == 79

    def test_get_score_when_with_three_strikes_in_a_row_and_spare_in_tenth(self):
        pins_down = [(1,2), (3,4), (10, ), (10, ), (10, ), (1,3), (0,0), (0,0), (0,0), (8, 2, 7), ]
        score = BowlingScore(pins_down).get_score()
        assert score == 96

    def test_get_score_when_with_three_strikes_in_a_row_and_strike_in_tenth(self):
        pins_down = [(1,2), (3,4), (10, ), (10, ), (10, ), (1,3), (0,0), (0,0), (0,0), (10, 9, 1), ]
        score = BowlingScore(pins_down).get_score()
        assert score == 99


