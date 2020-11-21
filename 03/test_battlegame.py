from battlegame import Battlegame

import numpy as np


def test_fill_left():
    ref = np.array( [
            [1, 1, 1, 1],
            [1, 1, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]], dtype=bool)

    g = Battlegame(4)

    assert isinstance(g.ship_boards[0], np.ndarray)
    assert ref.shape == g.ship_boards[0].shape
    assert (ref == g.ship_boards[0]).all()
