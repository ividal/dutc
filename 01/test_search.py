from search import search, match_element


def test_match_element():
    pattern = "fizz|buzz"
    element = "buzz"
    assert match_element(pattern, element)


def test_match_element_any():
    pattern = "*"
    element = "buzz"
    assert match_element(pattern, element)


def test_search_word():
    pattern = ["fizz"]
    # For 10:
    # 1, 2, fizz, 4, buzz, fizz, 7.nm, 8, fizz, buzz
    assert search(pattern, max_value=10) == 2


def test_search():
    pattern = ["fizz", "*", "buzz"]
    # For 10:
    # 1, 2, fizz, 4, buzz, fizz, 7, 8, fizz, buzz
    assert search(pattern, max_value=10) == 2


def test_search_not_first():
    pattern = ["fizz", "#", "#"]
    # For 10:
    # 1, 2, fizz, 4, buzz, fizz, 7, 8, fizz, buzz
    assert search(pattern, max_value=10) == 5
