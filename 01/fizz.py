def is_divisible_by(n: int, factor: int) -> bool:
    return n%factor == 0

def contains(full_number: int, digit: int) -> bool:
    return str(digit) in str(full_number)

    
if __name__ == "__main__":
    """ This is executed when run from the command line """
    fizz(1)