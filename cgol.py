"""
Conway's Game of Life
"""
import enum
import random
from typing import List, Tuple


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



if __name__ == '__main__':
    g = Grid(size=(10, 10), rand=True)
    print(g)
    n = g.get_neighbors((0, 0))
    print(n)
