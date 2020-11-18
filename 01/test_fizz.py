from fizz import is_divisible_by, contains

def test_is_divisible_by():
    assert is_divisible_by(2, 2)

def test_is_divisible_by():
    assert is_divisible_by(4, 2)

def test_is_divisible_by():
    assert not is_divisible_by(3, 6)

def test_is_divisible_by():
    assert is_divisible_by(6, 3)

def test_contains():
    assert contains(34, 4)



