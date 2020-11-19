from rock_paper_scissors import rules

def test_rules():
    assert rules("r", "p") == "2"
    assert rules("p", "r") == "1"
    assert rules("s", "p") == "1"
    assert rules("p", "p") == "X"