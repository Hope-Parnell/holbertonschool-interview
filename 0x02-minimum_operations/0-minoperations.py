#!/usr/bin/python3
"""
In a text file, there is a single character H. Your text editor can execute
 only two operations in this file: Copy All and Paste. Given a number n,
 calculate the fewest number of operations needed to result in exactly
 n H characters in the file
"""
from math import sqrt


def minOperations(n):
    """
    Finds the min number of Copy All and Pastes needed to have n H characters
    """
    if (n < 2 or type(n) is not int):
        return 0

    operations = 0
    while (n % 2 == 0):
        operations += 2
        n /= 2
    for factor in range(3, int(n) + 1, 2):
        if (n < factor):
            if (n != 1):
                operations += n
            break
        while (n % factor == 0):
            operations += factor
            n = n / factor
    return int(operations if operations > 0 else n)
