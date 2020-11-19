from random import choice
from collections import Counter, deque


# NOTE: for naming & design purposes, you may assume the players are directional
#       i.e., `a` is the Player
#             `b` is the Challenger
#       e.g., `rules` could return "player wins" or "player loses"
#              or it could "player wins" vs "challenger wins"
# QUESTION: how do you represent ties?
def rules(a: str, b: str) -> str:
    """
    Returns who wins, given shapes played by two players a and b
    a: Player
    b: Challenger
    Returns oneof:
        "1": Player wins
        "X": Tie
        "2": Challenger wins
    """

    if a not in ["r", "p", "s"] or \
            b not in ["r", "p", "s"]:
        return None

    if a == b:
        return "X"

    if a == "r":
        result = "1" if (b == "s") else "2"
        return result
    if a == "p":
        result = "1" if (b == "r") else "2"
        return result
    if a == "s":
        result = "1" if (b == "p") else "2"
        return result


def random_strategy():
    """ randomly select a shape """
    return choice(['rps'])


# other sample strategies…

# QUESTION: how do we track "history" here?
def beat_previous_play():
    """ select the shape that would beat the opponent's previous play """
    pass


def most_common_play(n=3):
    ''' select the most common shape from the opponent's previous N plays '''
    pass


games = [(random_strategy(), random_strategy()) for _ in range(10_000)]
results = [rules(a, b) for a, b in games]
