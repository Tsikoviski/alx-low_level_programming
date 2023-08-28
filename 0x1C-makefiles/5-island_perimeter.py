#!/usr/bin/python3
""" function that that returns the
    perimeter of the island described in grid """


def island_perimeter(grid):
    """returns perimeter"""
    perimeter = 0
    index = 0

    if not isinstance(grid, list):
        return 0

    for row in grid:
        row_len = len(row)

    grid_line = []
    i = 0
    while i < row_len:
        grid_line.append(0)
        i += 1
    for row in grid:
        for item in row:
            grid_line.append(item)
    i = 0
    while i < row_len:
        grid_line.append(0)
        i += 1

    for item in grid_line:
        if item == 1:
            if grid_line[index - row_len] == 0:
                perimeter += 1
            if grid_line[index - 1] == 0:
                perimeter += 1
            if grid_line[index + 1] == 0:
                perimeter += 1
            if grid_line[index + row_len] == 0:
                perimeter += 1
        index += 1

    return perimeter
