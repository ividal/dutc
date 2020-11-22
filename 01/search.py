import re
from fizzbuzz import fizzbuzz

"""
If the pattern is found, return the position and the remainder of the list to be examined.
"""


def match_element(pattern: str, element: str) -> bool:
    # CHANGE: this must be a regex comparison,
    # consider the 4 different possibilities --> different methods?
    # find string in list: sequence.index(element)
    # find 1ofN words: try the above twice
    # find any word: re find word
    # find digit: re find digit

    if pattern == "*":
        return True
    if pattern == "#":
        re_pattern = re.compile("[0-9]+")
        match = re.fullmatch(re_pattern, element) is not None
        return match
    if "|" in pattern:
        word1, word2 = pattern.split("|")
        match = (word1 == element) or (word2 == element)
        return match

    # Anything else, it better match exactly what the pattern is.
    # We're accepting even things other than just words.
    match = pattern == element
    return match


def search(pattern, *, max_value=100_000) -> int:
    ''' search for a pattern within the fizzbuzz sequence up to max_value

    Use the following (sample) grammar:
    - word: match this exact word (e.g., fizz, buzz, fizzbuzz)
    - word₁|word₂: match word₁ OR word₂
    - *: match any word
    - #: match only a number

    Assume match needs to be exactly the pattern, as in fullmatch
    Returns the position (0-indexed) where the matched sequence starts
    '''

    fizzbuzz_string = fizzbuzz(max_value)

    sequence = fizzbuzz_string.split(", ")
    matched_positions = [i for i, element in enumerate(sequence) if match_element(pattern[0], element)]

    if len(matched_positions) < 1:
        return None

    # the rest must follow exactly. As soon as a pair mis-matches, we're out.
    # If there was a perfect match, we keep the position where it started
    for pos in matched_positions:
        subsequence = sequence[pos:]
        matches = [match_element(p, s) for p, s in zip(pattern, subsequence) ]
        if all(matches):
            return pos, fizzbuzz_string

    return None, None


# look for four sequential plays that are
#   fizz, then fizz OR buzz, then anything, then buzz
pattern = ['fizz', 'fizz|buzz', '*', 'fizzbuzz']
pos, fizzbuzz = search(pattern, max_value=15)

print(f"Found {pattern=} \n\ton 0-indexed {pos=} \n\tof {fizzbuzz=}")
