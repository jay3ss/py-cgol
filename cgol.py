"""
Conway's Game of Life
"""
import copy
import curses
import enum
import random
import time
from typing import List, Tuple


DISPLAY_DELAY = 0.1


class CellStatus(enum.Enum):
    """
    Enum for a cell's status (alive or dead).
    """
    dead = 0
    alive = 1


class Cell:
    """
    The cell
    """
    def __init__(
        self,
        position: Tuple[int, int],
        state: CellStatus=None
        ) -> None:
        self.state = state if state is not None \
            else random.choice([CellStatus.alive, CellStatus.dead])
        self.col, self.row = position
        print('', end='')

    @property
    def is_alive(self):
        """
        Determines if the cell is alive or not

        Returns:
            bool: True if the cell is alive, Faslse otherwise
        """
        return self.state == CellStatus.alive

    def kill(self):
        """
        Sets the cell's state to CellStatus.dead
        """
        self.state = CellStatus.dead

    def reanimate(self):
        """
        Sets the cell's state to CellStatus.alive
        """
        self.state = CellStatus.alive

    def __repr__(self) -> str:
        return f'<Cell: {self.state} ({self.col}, {self.row})>'

    def __str__(self) -> str:
        return '*' if self.state is CellStatus.alive else ' '


class Grid:
    """
    Gird to hold the cells.
    """

    def __init__(self, size: Tuple[int, int], rand=False) -> None:
        self._rows, self._cols = size
        self._grid = self._initialize_grid(rand)

    def update_cell(self, cell: Cell) -> Cell:
        """
        Updates the state of the cell.

        Args:
            position (Tuple[int, int]): The position of the cell within the Grid
            new_state (CellStatus): The new state of the cell

        Returns:
            Cell: The updated cell.
        """
        col, row = cell.col, cell.row
        self._grid[row][col] = cell
        return self._grid[row][col]

    def get_cell(self, position: Tuple[int, int]) -> Cell:
        """
        Returns the cell at the given position

        Args:
            position (Tuple[int, int]): Position of the cell within the grid

        Returns:
            Cell: The desired cell
        """
        col, row = position
        cell = self._grid[row][col]
        return cell

    def get_neighbors(self, position: Tuple[int, int]) -> List[Cell]:
        """
        Returns a list of neighboring cells. A neighboring cell is one that
        either shares an edge or corner with the cell in question. The grid is
        assumed to not wrap around.

        Args:
            position (Tuple[int, int]): Position of the cell within the grid.

        Returns:
            Cell: The neighbors of the given cell.
        """
        neighbors = []
        col, row = position

        for i in range(-1, 2):
            for j in range(-1, 2):
                # don't add the cell itself or any out-of-bounds cells
                loc = col + j, row + i
                if not loc == position and self.is_in_bounds(loc):
                    neighbors.append(self.get_cell(loc))

        return neighbors

    def is_in_bounds(self, position: Tuple[int, int]) -> bool:
        """
        Determines if the given position is within the bounds of the grid

        Args:
            position (Tuple[int, int]): The location

        Returns:
            bool: True if the position is within bounds, False otherwise
        """
        col, row = position
        return 0 <= col < self._cols and 0 <= row < self._rows

    def _initialize_grid(self, rand: bool) -> List:
        """
        Initializes the grid.

        Args:
            rand (bool): If True, the grid will randomly have select cells
            selected to be alive or dead. Otherwise, all cells are dead.

        Returns:
            List: The initialized grid.
        """
        state = None if rand else CellStatus.dead
        return [
            [Cell((col, row), state) for col in range(self._cols)]
            for row in range(self._rows)
        ]

    def __str__(self) -> str:
        return '\n'.join([
            ' '.join([str(self.get_cell((i, j))) for i in range(self._cols)])
                for j in range(self._rows)
        ])


class GameOfLife:
    """
    Runs the game
    """

    def __init__(self, size: Tuple[int, int], rand: bool) -> None:
        self._grid = Grid(size=size, rand=rand)

    def update(self) -> None:
        """
        Updates the next generation of cells
        """
        grid = copy.deepcopy(self._grid)
        cols, rows = grid._cols, grid._rows

        for col in range(cols):
            for row in range(rows):
                location = col, row
                neighbors = grid.get_neighbors(location)
                cell = grid.get_cell(location)
                num_alive = _num_alive(neighbors)

                # rules for updating:
                # 1. Any live cell with two or three live neighbours survives.
                # 2. Any dead cell with three live neighbours becomes a live
                #    cell.
                # 3. All other live cells die in the next generation. Similarly,
                #    all other dead cells stay dead.
                if cell.is_alive and num_alive in [2, 3]:
                    # don't do anything
                    continue
                elif not cell.is_alive and num_alive == 3:
                    cell.reanimate()
                else:
                    cell.kill()

        self._grid = grid

    def __str__(self) -> str:
        return str(self._grid)


def display(screen, gol: GameOfLife):
    """
    Displays (prints) the grid to the terminal
    """
    curses.curs_set(0)
    screen.nodelay(True)

    while True:
        screen.erase()
        screen.addstr(str(gol))
        screen.refresh()
        gol.update()
        time.sleep(DISPLAY_DELAY)



def _num_alive(neighbors: List[Cell]) -> int:
    """
    Counts the number living neighbors.

    Args:
        neighbors (List[Cell]): The neighbors

    Returns:
        int: The number of living neighbors
    """
    return sum([
        1 if neighbor.is_alive else 0
        for neighbor in neighbors
    ])



if __name__ == '__main__':
    gol = GameOfLife(size=(30, 30), rand=True)
    curses.wrapper(lambda s: display(s, gol))