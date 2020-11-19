from fizzbuzz import fizzbuzz

# NOTE: feel free to redesign the grammar for your pattern.
"""
If the pattern is found, return the position and the remainder of the list to be examined.
"""
def search_in_sequence(element: str, sequence: list):
    # CHANGE: this must be a re comparison,
    # consider the 4 different possibilities --> different methods?
    # find string in list: sequence.index(element)
    # find 1ofN words: try the above twice
    # find any word: re find word
    # find digit: re find digit
    pos = 3
    return pos


def search(pattern, *, max_value=100_000):
    ''' search for a pattern within the fizzbuzz sequence up to max_value

    Use the following (sample) grammar:
    - word: match this exact word (e.g., fizz, buzz, fizzbuzz)
    - word₁|word₂: match word₁ OR word₂
    - *: match any word
    - #: match only a number

    Assume match needs to be exactly the pattern, as in no unrecognized elements inbetween those of the pattern
    '''

    fizzbuzz_string = fizzbuzz(max_value)
    # first one is free in the sequence

    sequence = fizzbuzz_string.split(", ")
    pos = search_in_sequence(pattern.pop(0), sequence)
    if pos < 0:
        return None

    # the rest must follow exactly. As soon as a pair mis-matches, we're out.
    # If there was a perfect match, we keep the position where it started
    for p, s in zip(pattern, sequence):
        new_pos = search_in_sequence(pattern.pop(0), [sequence[pos]])
        if new_pos < 0:
            return None
    return pos



# look for four sequential plays that are
#   fizz, then fizz OR buzz, then anything, then buzz
pattern = ['fizz', 'fizz|buzz', '*', 'fizzbuzz']

search(pattern, max_value=10)