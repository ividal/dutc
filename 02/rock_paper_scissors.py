from random import choice
from collections import Counter, deque


class Game:

    def __init__(self, memory=5):
        # fifo, most recent to the left
        self.histories = [
            deque([], maxlen=memory),
            deque([], maxlen=memory)
        ]
        self.what_beats_key = {"r": "p", "s": "r", "p": "s"}

    def beat_previous_play(self, player_id):
        """ select the shape that would beat the opponent's previous play """
        opponents_history = self.histories[not player_id]
        if len(opponents_history) < 1:
            return self.random_strategy()
        winning_shape = self.what_beats_key[opponents_history[0]]
        return winning_shape

    def most_common_play(self, player_id, n=3):
        """ select the most common shape from the opponent's previous N plays """
        opponents_history = self.histories[not player_id]
        limit = min(n, len(opponents_history))
        opponents_recent_history = list(opponents_history)[:limit]
        counts = Counter(opponents_recent_history)
        shape = counts.most_common()[0][0]
        return shape

    def random_strategy(self):
        """ randomly select a shape """
        return choice(["r", "p", "s"])

    def show_hands(self, player_shape, challenger_shape):
        self.histories[0].appendleft(player_shape)
        self.histories[1].appendleft(challenger_shape)
        return player_shape, challenger_shape

    def rules(self, a: str, b: str) -> str:
        """
            Returns who wins, given shapes played by two players a and b
            a: Player
            b: Challenger
            Returns one of:
                "1": Player wins
                "X": Tie
                "2": Challenger wins
        """

        if (a not in ["r", "p", "s"] or
                b not in ["r", "p", "s"]):
            return None

        if a == b:
            return "X"

        result = "2" if b == self.what_beats_key[a] else "1"
        return result


g = Game()

games = [g.show_hands(g.random_strategy(), g.beat_previous_play(1)) for _ in range(10_000)]
results = [g.rules(a, b) for a, b in games]
ranking = Counter(results)
print("1: Player 1 wins, X: tie, 2: Player 2 wins.")
print(f"{ranking= }")
