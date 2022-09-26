"""
Given a list of non-negative integers representing the heights of walls with
unit width 1, as if viewing the cross-section of a relief map, calculate how
many square units of water will be retained after it rains.
"""

def rain(walls):
    """
    Calculates the amount of rain a set of walls can hold

    Args:
        walls: list of non-negative integers representing
               the height of each wall in units

    Return: Amount of water(in square units) the given walls can hold
    """
    if type(walls) is not list:
        raise TypeError(
            "walls is not a list")
    rainVol = 0
    size = len(walls)
    if size > 0:
        if any(type(x) is not int for x in walls):
            raise TypeError(
                "walls contains non-integers")
        if any(x < 0 for x in walls):
            raise ValueError(
                "walls contains negitive integer")
        left = size * [0]
        right = size * [0]
        leftMax = walls[0]
        rightMax = walls[-1]
        for i in range(0, size):
            if walls[i] > leftMax:
                leftMax = walls[i]
            left[i] = leftMax
            if walls[size - i - 1] > rightMax:
                rightMax = walls[size -i - 1]
            right[size - i - 1] = rightMax
        for i in range(0, size):
            rainVol += min(left[i], right[i]) - walls[i]

    return rainVol
