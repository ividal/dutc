def is_divisible_by(full_number: int, factor: int) -> bool:
    return full_number % factor == 0

def contains(full_number: int, digit: int) -> bool:
    return str(digit) in str(full_number)


"""
players…:
    say “fizz” if their number is divisible by 3 or contains the digit 3
    say “buzz” if their number is divisible by 5 or contains the digit 5
    say “fizzbuzz” if their number…
        is divisible by 3 or contains the digit 3
        and, is divisible by 5 or contains the digit 5
    otherwise, they just say their number
“one, two, fizz (three,) four, buzz (five,) fizz (six,) seven, eight, 
fizz (nine,) buzz (ten,) eleven, fizz (twelve,) fizz (thirteen,) fourteen, fizzbuzz (fifteen,) …”
"""
def fizzbuzzify(full_number: int, is_extended: bool = False) -> str:
    if full_number < 1:
        return None

    result = ""
    is_fizz = is_divisible_by(full_number, 3) or contains(full_number, 3)
    is_buzz = is_divisible_by(full_number, 5) or contains(full_number, 5)
    is_quux = is_extended and (is_divisible_by(full_number, 7) or contains(full_number, 7))
    is_none = not (is_fizz or is_buzz or is_quux)

    # We assume words can be appended for extensions as well (e.g. fizzbuzzquux for 35)
    if is_fizz:
        result += "fizz"
    if is_buzz:
        result += "buzz"
    if is_quux:
        result += "quux"

    if is_none:
        # TODO: int to numeral (word)?
        result = str(full_number)

    return result


def fizzbuzz(full_number: int, **kwargs):
    return ", ".join([fizzbuzzify(i, **kwargs) for i in range(1, full_number+1, 1)])
    
if __name__ == "__main__":
    print(fizzbuzz(15, is_extended=True))