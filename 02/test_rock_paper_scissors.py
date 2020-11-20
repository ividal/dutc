from collections import deque
from rock_paper_scissors import Game


def test_rules():
    g = Game()
    assert g.rules("r", "p") == "2"
    assert g.rules("p", "r") == "1"
    assert g.rules("s", "p") == "1"
    assert g.rules("p", "p") == "X"


def test_beat_last():
    g = Game()
    g.histories = [
        deque(["r", "s"]),
        deque(["p", "p"])
    ]
    assert g.beat_previous_play(0) == "s"
    assert g.beat_previous_play(1) == "p"

def test_most_common():
    g = Game()
    g.histories = [
        deque(["r", "s", "s"]),
        deque(["p", "p", "s"])
    ]
    assert g.most_common_play(0) == "p"
    assert g.most_common_play(1) == "s"
