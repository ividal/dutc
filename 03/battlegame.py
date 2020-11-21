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
                 fill_strategies: tuple = ("linear", "linear")):

        available_filling_strategies = {
            "linear": self.fill_linear,
            "random": self.fill_randomly
        }

        self.size = size
        self.players = [0, 1]
        self.players_cycle = cycle(self.players)

        if not attack_strategies:
            attack_strategies = self.fixed_target()
        self.attack_strategies = attack_strategies

        ships_A_strategy = available_filling_strategies[fill_strategies[0]]
        ships_B_strategy = available_filling_strategies[fill_strategies[1]]
        self.placing_strategies = (ships_A_strategy, ships_B_strategy)

        # >=1: has part of a ship, 0: doesn't, -1: block was hit
        ships_A, lives_A = self.placing_strategies[0](allowed_pieces)
        ships_B, lives_B = self.placing_strategies[1](allowed_pieces)
        self.ship_boards = (ships_A, ships_B)
        print(f"{lives_A =}")

        self.lives = (lives_A, lives_B)
        [print(b) for b in self.ship_boards]
        print(f"{self.lives =}")

        # 0: never fired, 1: hit, -1: missed
        state_A = np.zeros((self.size, self.size), dtype=int)
        state_B = np.zeros((self.size, self.size), dtype=int)
        self.states = (state_A, state_B)

    def find_row(self, board:np.array, blocks:int, ship_id:int, lives: dict):
        placed = False
        lives[ship_id] = 0
        for r in range(board.shape[0]):
            if placed:
                break
            row = board[r]
            for c in range(board.shape[1]):
                if placed:
                    break
                if valid_starting_block(row[c:], blocks):
                    row[c:c + blocks] = ship_id
                    lives[ship_id] = blocks
                    placed = True

        return placed, board, lives

    def fill_linear(self, pieces: tuple[str]) -> np.array:
        board = np.zeros((self.size, self.size), dtype=int)
        lives = {}
        for i, p in enumerate(pieces):
            ship_id = i + 1  # we don't want 0-indexed ids
            blocks = self.ship_sizes[p]
            placed, board, lives = self.find_row(board, blocks, ship_id=ship_id, lives=lives)

            if not placed:
                board_t = np.transpose(board)
                placed, board_t, lives = self.find_row(board_t, blocks, ship_id=ship_id, lives=lives)
                board = np.transpose(board_t)

        print(f"{lives=}")
        return board, lives

    def fill_randomly(self, pieces: tuple[str]) -> np.array:
        board = np.zeros((self.size, self.size), dtype=int)
        lives = {}
        coords = random_strategy(self.size)
        for i, p in enumerate(pieces):
            ship_id = i + 1  # we don't want 0-indexed ids
            lives[ship_id] = 0
            placed = False
            blocks = self.ship_sizes[p]

            for (r, c) in coords:
                if placed:
                    break
                row = board[r]
                if valid_starting_block(row[c:], blocks):
                    row[c:c + blocks] = ship_id
                    placed = True
                else:
                    col = board[:, c]
                    if valid_starting_block(col[r:], blocks):
                        col[r:r+blocks] = ship_id
                        placed = True
        if placed:
            lives[ship_id] = blocks

        return board, lives

    def play_round(self):
        id = next(self.players_cycle)
        target_id = (id + 1) % len(self.players)
        coords = self.choose_next_target(id)
        result = self.fire(target_id, coords)

        return result, self.check_lost(target_id)

    def choose_next_target(self, player_id):
        return next(self.attack_strategies[player_id])

    def fixed_target(self):
        return (1,1)

    def fire(self, target_id, coordinates):
        hit = False
        if self.ship_boards[target_id][coordinates]:
            hit = True
            self.states[target_id][coordinates] = 1
            ship_id = self.ship_boards[target_id][coordinates]
            self.ship_boards[target_id][coordinates] = -1
            ship_life = self.lives[target_id][ship_id]
            self.lives[target_id][ship_id] = ship_life - 1
            print(f"Target Player {target_id}, {coordinates} was a HIT!")
            if self.lives[target_id][ship_id] == 0:
                print(f"Player {target_id}'s ship is sunk!")
        else:
            self.states[target_id][coordinates] = -1
            print(f"Target Player {target_id}, {coordinates} was a MISS!")
        return hit

    def check_lost(self, target_id) -> bool:
        lost = False
        print(self.lives[target_id])
        #if not (self.ship_boards[target_id] > 0).any():
        if all(life == 0 for life in self.lives[target_id].values()):
            lost = True
            print(f"Player {target_id} lost!")
        return lost


def valid_starting_block(slice: np.array, blocks: int) -> bool:
    if not (any(slice[:blocks] > 0) or blocks > len(slice)):
        return True

    return False



def random_strategy(board_size=10):
    targets = [*product(range(board_size), range(board_size))]
    shuffle(targets)
    yield from targets


def linear_strategy(board_size=10):
    targets = [*product(range(board_size), range(board_size))]
    targets.reverse()
    yield from targets