from search import search, search_in_sequence


def test_search_word():
    pattern = ["fizz"]
    # For 10:
    # 1, 2, fizz, 4, buzz, fizz, 7.nm, 8, fizz, buzz
    assert search(pattern, max_value = 10) == 3

def test_search():
    pattern = ["fizz", "*", "buzz"]
    # For 10:
    # 1, 2, fizz, 4, buzz, fizz, 7.nm, 8, fizz, buzz
    assert search(pattern, max_value = 10) == 3
