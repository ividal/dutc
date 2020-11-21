import numpy as np
from itertools import cycle
from itertools import product
from random import shuffle


class Battlegame:
    """
    The ‘carrier’ is 5×1 in size.
    The ‘battleship’ is 4×1 in size.
    The ‘cruiser’ is 3×1 in size.
    The ‘submarine’ is 3×1 in size.
    The ‘destroyer’ is 2×1 in size
    
    If the list has 1 destroyer and 1 submarine:
    [ [1, 1, 1, 0],
      [1, 1, 0, 0],
      [0, 0, 0, 0]
    ]
    """

    ship_sizes = {
        "carrier": 5,
        "destroyer": 2,
    }

    def __init__(self, size: int, strategies: tuple=None):
        self.size = size
        self.players = [0, 1]
        self.players_cycle = cycle(self.players)
        if not strategies:
            strategies = self.fixed_target()
        self.strategies = strategies

        # 1: has ship block, 0: doesn't
        ships_A = self.fill_left(["carrier", "destroyer"])
        ships_B = self.fill_left(["destroyer", "carrier"])
        self.ships = (ships_A, ships_B)
        [print(b) for b in self.ships]

        # 0: never fired, 1: hit, -1: missed
        state_A = np.zeros((self.size, self.size), dtype=int)
        state_B = np.zeros((self.size, self.size), dtype=int)
        self.states = (state_A, state_B)

    def fill_left(self, pieces: list) -> np.array:
        board = np.zeros((self.size, self.size), dtype=int)
        for p in pieces:
            placed = False
            blocks = self.ship_sizes[p]
            start = 0
            end = start + blocks
            for row in board:
                if placed:
                    break
                if any(row[start:end]):
                    continue
                row[start:end] = 1
                placed = True
                continue
        return board

    def play_round(self):
        id = next(self.players_cycle)
        target_id = (id + 1) % len(self.players)
        coords = self.choose_next_target(id)
        result = self.fire(target_id, coords)

        return result, self.check_lost(target_id)

    def choose_next_target(self, player_id):
        return next(self.strategies[player_id])

    def fire(self, target_id, coordinates):
        hit = False
        if self.ships[target_id][coordinates]:
            hit = True
            self.states[target_id][coordinates] = 1
            self.ships[target_id][coordinates] = -1
            print(f"Target Player {target_id}, {coordinates} was a HIT!")
        else:
            self.states[target_id][coordinates] = -1
            print(f"Target Player {target_id}, {coordinates} was a MISS!")
        return hit

    def check_lost(self, target_id) -> bool:
        lost = False
        if not (self.ships[target_id] == 1).any():
            lost = True
        return lost

    def fixed_target(self) -> tuple:
        yield (1, 1)


def random_strategy(board_size=10):
    targets = [*product(range(board_size), range(board_size))]
    shuffle(targets)
    while True:
        yield targets.pop()


if __name__ == "__main__":
    board_size = 4
    strategy_A = random_strategy(board_size)
    strategy_B = random_strategy(board_size)

    g = Battlegame(board_size, (strategy_A, strategy_B))

    rounds = 6
    #ended = False
    for r in range(rounds):
        result, ended = g.play_round()
        print(result)
        if ended:
            break
