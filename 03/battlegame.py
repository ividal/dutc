import numpy as np
from itertools import cycle

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


# zero_els = np.count_nonzero(row[start:])
def fill_left(size: int, pieces: list) -> np.array:
    board = np.zeros((size, size), dtype=bool)
    for p in pieces:
        placed = False
        blocks = ship_sizes[p]
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


def fire(playerID, coords, state_board):
    return False


size = 4
players = cycle([0, 1])

# 1: has ship block, 0: doesn't
ships_A = fill_left(size, ["carrier", "destroyer"])
ships_B = fill_left(size, ["destroyer", "carrier"])
ship_boards = (ships_A, ships_B)
print(ships_A)
print(ships_B)