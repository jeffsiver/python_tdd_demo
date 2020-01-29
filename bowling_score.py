from typing import List


class BowlingGame:
    def __init__(self, pins_down: List[int]):
        self._pins_down = pins_down

    def final_score(self) -> int:
        score = 0
        frame_start_index = 0
        for frame in range(1, 11):
            score += self._calculate_score_for_frame(frame_start_index)
            frame_start_index += self.increment_frame_start_index(frame_start_index)
        return score

    def _calculate_score_for_frame(self, frame_start_index: int):
        if self._is_strike(frame_start_index):
            return 10 + self._pins_down[frame_start_index + 1] + self._pins_down[frame_start_index + 2]
        elif self._is_spare(frame_start_index):
            return 10 + self._pins_down[frame_start_index + 2]
        return self._pins_down[frame_start_index] + self._pins_down[frame_start_index + 1]

    def _is_strike(self, frame_start_index: int):
        return self._pins_down[frame_start_index] == 10

    def _is_spare(self, frame_start_index: int):
        return self._pins_down[frame_start_index] + self._pins_down[frame_start_index+1] == 10

    def increment_frame_start_index(self, frame_start_index: int):
        if self._is_strike(frame_start_index):
            return 1
        return 2


class TestBowlingGame:
    def test_all_gutter_balls(self):
        pins_down = [0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, ]
        score = BowlingGame(pins_down).final_score()
        assert score == 0

    def test_all_open_frames(self):
        pins_down = [3,4, 6,3, 7,2, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, ]
        score = BowlingGame(pins_down).final_score()
        assert score == 25

    def test_has_one_spare_and_no_strikes(self):
        pins_down = [3,4, 6,3, 7,2, 7,3, 3,4, 0,0, 0,0, 0,0, 0,0, 0,0, ]
        score = BowlingGame(pins_down).final_score()
        assert score == 45

    def test_has_no_spares_and_one_strike(self):
        pins_down = [0,0, 10, 7,2, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, ]
        score = BowlingGame(pins_down).final_score()
        assert score == 28

    def test_has_no_spares_and_one_strike_and_a_strike_in_the_tenth(self):
        pins_down = [0,0, 10, 7,2, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 10,7,2, ]
        score = BowlingGame(pins_down).final_score()
        assert score == 47

    def test_has_no_spares_and_one_strike_and_a_spare_in_the_tenth(self):
        pins_down = [0,0, 10, 7,2, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 9,1,7, ]
        score = BowlingGame(pins_down).final_score()
        assert score == 45

    def test_perfect_game(self):
        pins_down = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,  ]
        score = BowlingGame(pins_down).final_score()
        assert score == 300

    def test_alternating_game(self):
        pins_down = [10, 7,3, 10, 7,3, 10, 7,3, 10, 7,3, 10, 7,3,10, ]
        score = BowlingGame(pins_down).final_score()
        assert score == 200
