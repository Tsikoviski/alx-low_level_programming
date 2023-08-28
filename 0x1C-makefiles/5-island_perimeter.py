#!/usr/bin/python3
"""Defines the island perimeter function"""


def island_perimeter(grid):
    """
    Returns the perimeter of an island described in grid
    Grid is a list of list of integers with 0 representing water
    and 1 representing land
    """
    height = len(grid)
    breadth = len(grid[0])
    size = 0
    edge = 0
    for a in range(height):
        for b in range(breadth):
            if grid[a][b] == 1:
                size += 1
                if (b > 0 and grid[a][b - 1] == 1):
                    edge += 1
                if (a > 0 and grid[a - 1][b] == 1):
                    edge += 1
    return ((size * 4) - (edge * 2))
