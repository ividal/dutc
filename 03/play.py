from battlegame import Battlegame, random_strategy


if __name__ == "__main__":
    board_size = 6
    strategy_A = random_strategy(board_size)
    strategy_B = random_strategy(board_size)

    g = Battlegame(board_size, (strategy_A, strategy_B),
                   allowed_pieces=("carrier", "destroyer", "destroyer", "carrier"),
                   fill_strategies=("linear", "linear"))

    ended = False
    while(not ended):
    # for r in range(3):
        result, ended = g.play_round()
