#!/usr/bin/python3
"""Island Perimeter"""

def island_perimeter(grid):
    """
    Calculate perimeter of island given a grid
    where 1s represent land and 0s represent water
    """
    perimeter = 0
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y]:
                # count number of 0's on left and top
                perimeter += [grid[x - 1][y],
                              grid[x][y - 1],
                              ].count(0)
    return perimeter * 2
