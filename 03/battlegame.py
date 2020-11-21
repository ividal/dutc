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
    """

    ship_sizes = {
        "carrier": 5,
        "battleship": 4,
        "cruiser": 3,
        "submarine": 3,
        "destroyer": 2
    }

    def __init__(self, size: int, attack_strategies: tuple = None,
                 allowed_pieces: tuple[str] = ("carrier", "destroyer"),
                 placing_strategies: tuple = ("linear", "linear")):

        filling_strategies = {
            "linear": self.fill_linear
        }

        self.size = size
        self.players = [0, 1]
        self.players_cycle = cycle(self.players)

        if not attack_strategies:
            attack_strategies = self.fixed_target()
        self.attack_strategies = attack_strategies

        ships_A_strategy = filling_strategies.get(placing_strategies[0], filling_strategies["linear"])
        ships_B_strategy = filling_strategies.get(placing_strategies[1], filling_strategies["linear"])
        self.placing_strategies = (ships_A_strategy, ships_B_strategy)

        # 1: has part of a ship, 0: doesn't, -1: block was hit
        ships_A = self.fill_linear(allowed_pieces)
        ships_B = self.fill_linear(allowed_pieces)
        self.ships = (ships_A, ships_B)
        [print(b) for b in self.ships]

        # 0: never fired, 1: hit, -1: missed
        state_A = np.zeros((self.size, self.size), dtype=int)
        state_B = np.zeros((self.size, self.size), dtype=int)
        self.states = (state_A, state_B)

    def find_row(self, board, block_size):
        placed = False

        for r in range(board.shape[0]):
            if placed:
                break
            row = board[r]
            for c in range(board.shape[1]):
                if placed:
                    break
                end = c + block_size
                if any(row[c:end]):
                    continue
                row[c:end] = 1
                placed = True

        return placed, board

    def fill_linear(self, pieces: list) -> np.array:
        board = np.zeros((self.size, self.size), dtype=int)
        for p in pieces:
            blocks = self.ship_sizes[p]
            placed, board = self.find_row(board, blocks)
            if not placed:
                board_t = np.transpose(board)
                _, board_t = self.find_row(board_t, blocks)
                board = np.transpose(board_t)

        return board

    def play_round(self):
        id = next(self.players_cycle)
        target_id = (id + 1) % len(self.players)
        coords = self.choose_next_target(id)
        result = self.fire(target_id, coords)

        return result, self.check_lost(target_id)

    def choose_next_target(self, player_id):
        return next(self.attack_strategies[player_id])

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
            print(f"Player {target_id} lost!")
        return lost

    def fixed_target(self) -> tuple:
        yield (1, 1)


def random_strategy(board_size=10):
    targets = [*product(range(board_size), range(board_size))]
    shuffle(targets)
    while True:
        yield targets.pop()


def linear_strategy(board_size=10):
    targets = [*product(range(board_size), range(board_size))]
    targets.reverse()
    while True:
        yield targets.pop()


if __name__ == "__main__":
    board_size = 5
    strategy_A = random_strategy(board_size)
    strategy_B = random_strategy(board_size)

    g = Battlegame(board_size, (strategy_A, strategy_B),
                   allowed_pieces=("carrier", "destroyer", "destroyer", "carrier"))

    ended = False
    while(not ended):
        result, ended = g.play_round()
