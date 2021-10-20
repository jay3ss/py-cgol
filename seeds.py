"""
Module to hold pre-defined grids that demonstrate interesting behaviors.

Many taken from: https://github.com/robertmartin8/PyGameofLife
"""
from cgol import Cell, CellStatus
from typing import List


seeds = {
    "diehard": [
        [0, 0, 0, 0, 0, 0, 1, 0],
        [1, 1, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 1, 1, 1],
    ],
    "boat": [
        [1, 1, 0],
        [1, 0, 1],
        [0, 1, 0]
    ],
    "r_pentomino": [
        [0, 1, 1],
        [1, 1, 0],
        [0, 1, 0]
    ],
    "pentadecathlon": [
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 1, 1, 1, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
    ],
    "beacon": [
        [1, 1, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 1, 1],
        [0, 0, 1, 1]
    ],
    "acorn": [
        [0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [1, 1, 0, 0, 1, 1, 1]
    ],
    "spaceship": [
        [0, 0, 1, 1, 0],
        [1, 1, 0, 1, 1],
        [1, 1, 1, 1, 0],
        [0, 1, 1, 0, 0]
    ],
    "block_switch_engine": [
        [0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 0, 1, 1],
        [0, 0, 0, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 0, 0, 0, 0],
    ],
    "infinite": [
        [1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0],
        [0, 0, 0, 1, 1],
        [0, 1, 1, 0, 1],
        [1, 0, 1, 0, 1],
    ],
}


def num_to_state(num: int) -> CellStatus:
    """
    Transform a 1 or 0 to a CellStatus state, alive or dead, respectively.

    Args:
        num (int): either a 0 or a 1.

    Returns:
        CellStatus: dead if num is 0, alive otherwise
    """
    return CellStatus.dead if num == 0 else CellStatus.alive



def seed_to_grid(seed: List) -> List[Cell]:
    """
    Transforms the seed to a grid (list of Cell objects)

    Args:
        seed (list):
    """
    cols, rows = len(seed[0]), len(seed)
    return [
        [
            Cell((c, r), state=num_to_state(seed[r][c]))
            for c in range(cols)
        ]
        for r in range(rows)
    ]