from battlegame import Battlegame

import numpy as np

test_ship_board = np.array([
    [0, -1, -1, -1],
    [0, 0, 1, -1],
    [0, 0, 0, 0],
    [0, 0, 0, 0]], dtype=int)

test_state_board = np.array([
    [0, 1, 1, 1],
    [0, 0, 0, 1],
    [0, 0, 0, 0],
    [0, 0, -1, 0]], dtype=int)


def test_fill_left():
    ref = np.array([
        [1, 1, 1, 1],
        [1, 1, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]], dtype=int)

    g = Battlegame(4)

    assert isinstance(g.ships[0], np.ndarray)
    assert ref.shape == g.ships[0].shape
    assert (ref == g.ships[0]).all()


def test_fire():
    g = Battlegame(4)
    g.ships = (test_ship_board, False * test_ship_board)
    g.states = (test_state_board, 8 * test_state_board)

    assert g.fire(0, (1, 2))
    assert (g.ships[0] == np.array([
        [0, -1, -1, -1],
        [0, 0, -1, -1],
        [0, 0, 0, 0],
        [0, 0, 0, 0]], dtype=int)).all()

    assert (g.states[0] == np.array([
        [0, 1, 1, 1],
        [0, 0, 1, 1],
        [0, 0, 0, 0],
        [0, 0, -1, 0]], dtype=int)).all()
    assert g.check_lost(0)
