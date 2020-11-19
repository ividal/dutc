from fizzbuzz import is_divisible_by, contains, fizzbuzzify, fizzbuzz


def test_is_divisible_by():
    assert not is_divisible_by(3, 6)


def test_is_divisible_by():
    assert is_divisible_by(6, 3)


def test_contains():
    assert contains(34, 4)


def test_fizzbuzz_15():
    ref = "1, 2, fizz, 4, buzz, fizz, 7, 8, fizz, buzz, 11, fizz, fizz, 14, fizzbuzz"
    assert ref == fizzbuzz(15)


def test_fizzbuzz_1():
    ref = "1"
    assert ref == fizzbuzz(1)


def test_fizzbuzz_m1():
    ref = ""
    assert ref == fizzbuzz(-1)

def test_fizzbuzz_extended_35():
    ref = "fizzbuzzquux"
    assert ref == fizzbuzzify(35, is_extended=True)

def test_fizzbuzzify_vanilla_35():
    ref = "fizzbuzz"
    assert ref == fizzbuzzify(35)

def test_fizzbuzz_extended_15():
    ref = "1, 2, fizz, 4, buzz, fizz, quux, 8, fizz, buzz, 11, fizz, fizz, quux, fizzbuzz"
    assert ref == fizzbuzz(15, is_extended=True)

