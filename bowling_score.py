from typing import List


class BowlingScore:
    def __init__(self, pins_down: List[]):
        self.pins_down = pins_down

    def get_score(self) -> int:
        pass


class TestBowlingScore:
    def test_score_is_zero_when_all_gutters(self):
        pins_down = [(0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), ]
        score = BowlingScore(pins_down).get_score()
        assert score == 0
