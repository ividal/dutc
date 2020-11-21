import numpy as np
from itertools import cycle


class Battlgame:
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

    def __init__(self, size):
        self.size = size
        self.players = [0, 1]
        self.players_cycle = cycle(self.players)


        # 1: has ship block, 0: doesn't
        ships_A = self.fill_left(["carrier", "destroyer"])
        ships_B = self.fill_left(["destroyer", "carrier"])
        self.ship_boards = (ships_A, ships_B)
        [print(b) for b in self.ship_boards]

        # X: hit, .: miss
        self.state_board = np.empty((size, size), dtype=bool)
        print(self.ship_boards)

    # zero_els = np.count_nonzero(row[start:])
    def fill_left(self, pieces: list) -> np.array:
        board = np.zeros((self.size, self.size), dtype=bool)
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
                row[start:end] = True
                placed = True
                continue
        return board

    def play_round(self):
        id = next(self.players_cycle)
        target_id = (id + 1) % len(self.players)
        coords = (0, 0)
        result = self.fire(target_id, coords)
        return result, self.check_end()

    def fire(self, target_id, coordinates):
        hit = False
        if (self.ship_boards[target_id][coordinates] #and
                # self.state_board[target_id][coordinates]
            ):
            hit = True
        return hit

    def check_end(self) -> bool:
        return False

    def choose_next_target(self) -> tuple:
        return (1, 1)


size = 4
g = Battlgame(size)

print(g.ship_boards[0][1, 0])

# handles for the players
rounds = 6
for r in range(rounds):
    result,_ = g.play_round()
    print(result)
