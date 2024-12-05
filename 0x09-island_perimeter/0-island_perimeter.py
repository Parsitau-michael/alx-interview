#!/usr/bin/python3
""" This module represents a function that returns the perimeter of
the island described in grid
"""


def island_perimeter(grid):
    """ Function definition, it takes an argument grid
    """
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                perimeter += 4

                # Check the top neighbor
                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 1

                # Check the bottom neighbor
                if row < rows - 1 and grid[row + 1][col] == 1:
                    perimeter -= 1

                # Check the left neighbor
                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 1

                # Check the right neighbor
                if col < cols - 1 and grid[row][col + 1] == 1:
                    perimeter -= 1

    return perimeter
