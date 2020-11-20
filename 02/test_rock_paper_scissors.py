from collections import deque
from rock_paper_scissors import rules, Game


def test_rules():
    assert rules("r", "p") == "2"
    assert rules("p", "r") == "1"
    assert rules("s", "p") == "1"
    assert rules("p", "p") == "X"


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
