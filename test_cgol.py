"""
Test suite
"""
import pytest
from cgol import Cell, CellStatus, Grid


@pytest.fixture
def grid_3x3():
    """
    Sets up a 3x3 grid
    """
    grid_list = [
        [Cell((0, 0), CellStatus.dead), Cell((1, 0), CellStatus.dead), Cell((2, 0), CellStatus.alive)],
        [Cell((0, 1), CellStatus.alive), Cell((1, 1), CellStatus.dead), Cell((2, 1), CellStatus.alive)],
        [Cell((0, 2), CellStatus.dead), Cell((1, 2), CellStatus.dead), Cell((2, 2), CellStatus.dead)]
    ]
    grid = Grid(size=(3, 3), rand=False)
    grid._grid = grid_list
    return grid


def test_get_cell(grid_3x3: Grid):
    """
    Test that the proper cell is returned.
    """
    position = 1, 1 # center
    cell = grid_3x3.get_cell(position)
    assert position == (cell.col, cell.row)

    position = 0, 1 # left
    cell = grid_3x3.get_cell(position)
    assert position == (cell.col, cell.row)

    position = 2, 1 # right
    cell = grid_3x3.get_cell(position)
    assert position == (cell.col, cell.row)

    position = 1, 0 # top
    cell = grid_3x3.get_cell(position)
    assert position == (cell.col, cell.row)

    position = 1, 2 # bottom
    cell = grid_3x3.get_cell(position)
    assert position == (cell.col, cell.row)


def test_get_neighbors_center_position(grid_3x3: Grid):
    """
    Test that the correct neighbors are returned when the cell is in the center
    of the gird.
    """
    n = grid_3x3.get_neighbors((1, 1))
    assert len(n) == 8
    assert n[0].state == CellStatus.dead
    assert n[1].state == CellStatus.dead
    assert n[2].state == CellStatus.alive
    assert n[3].state == CellStatus.alive
    assert n[4].state == CellStatus.alive
    assert n[5].state == CellStatus.dead
    assert n[6].state == CellStatus.dead
    assert n[7].state == CellStatus.dead


def test_get_neighbors_left_side(grid_3x3: Grid):
    n = grid_3x3.get_neighbors((0, 1))
    assert len(n) == 5
    assert n[0].state == CellStatus.dead
    assert n[1].state == CellStatus.dead
    assert n[2].state == CellStatus.dead
    assert n[3].state == CellStatus.dead
    assert n[4].state == CellStatus.dead


def test_get_neighbors_right_side(grid_3x3: Grid):
    n = grid_3x3.get_neighbors((2, 1))
    assert len(n) == 5
    assert n[0].state == CellStatus.dead
    assert n[1].state == CellStatus.alive
    assert n[2].state == CellStatus.dead
    assert n[3].state == CellStatus.dead
    assert n[4].state == CellStatus.dead


def test_get_neighbors_top_side(grid_3x3: Grid):
    n = grid_3x3.get_neighbors((1, 0))
    assert len(n) == 5
    assert n[0].state == CellStatus.dead
    assert n[1].state == CellStatus.alive
    assert n[2].state == CellStatus.alive
    assert n[3].state == CellStatus.dead
    assert n[4].state == CellStatus.alive


def test_get_neighbors_bottom_side(grid_3x3: Grid):
    n = grid_3x3.get_neighbors((1, 2))
    assert len(n) == 5
    assert n[0].state == CellStatus.alive
    assert n[1].state == CellStatus.dead
    assert n[2].state == CellStatus.alive
    assert n[3].state == CellStatus.dead
    assert n[4].state == CellStatus.dead
