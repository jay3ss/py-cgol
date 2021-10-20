"""
Command line interface for Conway's Game of Life
"""
import argparse
import copy
import curses

from cgol import display, GameOfLife
from seeds import seed_to_grid, seeds


if __name__ == '__main__':
    parser = argparse.ArgumentParser('py-cgol')
    parser.add_argument(
        '--size',
        default="50,50",
        action='store',
        help='size of the universe (col x row)'
    )
    parser.add_argument(
        '--rand',
        default=False,
        action='store_true',
        help='random generation of universe'
    )
    parser.add_argument(
        '--seed',
        default='',
        action='store',
        help='seed if desired'
    )
    parser.add_argument(
        '--seed-position',
        default='40,40',
        action='store',
        help='position of the seed'
    )
    # args = parser.parse_args()
    args = parser.parse_args(
        ['--size', '4,4', '--seed', 'beacon', '--seed-position', '0,0']
    )
    size = (int(args.size.split(',')[0]), int(args.size.split(',')[1]))
    rand = args.rand
    seed = seeds[args.seed] if args.seed else None
    seed_position = (
        int(args.seed_position.split(',')[0]),
        int(args.seed_position.split(',')[1])
        ) if seed else None

    gol = GameOfLife(size=size, rand=rand)

    if seed:
        col_start = seed_position[0]
        col_end = col_start + len(seed[0])
        row_start = seed_position[1]
        row_end = row_start + len(seed)
        sub_grid = seed_to_grid(seed=seed)

        grid = copy.deepcopy(gol._grid)

        # replace the portion of the grid specified by the user with the
        # specified seed
        # i, j = 0, 0 # column, row
        # for r in range(row_start, row_end):
        #     i = 0
        #     for c in range(col_start, col_end):
        #         cell = sub_grid[j][i]
        #         cell.row = r
        #         cell.col = c
        #         grid.update_cell(cell)
        #         i += 1

        #     j += 1
        i = 0
        for row in range(row_start, row_end):
            grid._grid[row][col_start:col_end] = sub_grid[i]
            i += 1

        gol._grid = grid

    curses.wrapper(lambda s: display(s, gol))
