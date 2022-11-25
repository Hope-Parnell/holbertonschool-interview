#!/usr/bin/python3
"""Island Perimeter"""


def island_perimeter(grid):
    """
    Calculate perimeter of island given a grid
    where 1s represent land and 0s represent water
    """
    perimeter = 0
    height, width = len(grid), len(grid[0])
    for x in range(height):
        for y in range(width):
            if grid[x][y]:
                # only count lefts and tops
                # as tops = bottoms and lefts = rights
                if not x or not grid[x - 1][y]:
                    perimeter += 1
                if not y or not grid[x][y - 1]:
                    perimeter += 1
    return perimeter * 2
