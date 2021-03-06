#!/usr/bin/python3
"""
You have 'n' number of locked boxes in front of you.
Each box is numbered sequentially from '0' to 'n - 1'
and each box may contain keys to the other boxes.
"""


def canUnlockAll(boxes):
    """
        Tests if all boxes can be unlocked.
        ** Index 0 is already unlocked by default

        Args: boxes list of list(boxes) possibly containing numbered keys

        Return: True if all can be opened, false otherwise
    """
    # There are no boxes or only 1 box
    if boxes is None or len(boxes) < 2:
        return True
    n = len(boxes)
    # Open box 0
    opened = [0]
    usableKeys = []
    for key in boxes[0]:
        if key < n and key not in usableKeys and key not in opened:
            usableKeys.append(key)
    while (len(usableKeys) != 0):
        # All boxes are opened or have keys
        if (len(opened)+len(usableKeys) == n):
            return True
        # open box with key
        currentBox = usableKeys.pop(0)
        opened.append(currentBox)
        for key in boxes[currentBox]:
            if key < n and key not in usableKeys and key not in opened:
                usableKeys.append(key)
    return False
