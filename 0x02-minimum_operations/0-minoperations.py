#!/usr/bin/python3
"""
In a text file, there is a single character H. Your text editor can execute only two operations in this file: Copy All and Paste. 
Given a number n, calculate the fewest number of operations needed to result in exactly n H characters in the file
"""
from math import sqrt

def minOperations(n):
    """
    Finds the min number of Copy All and Pastes needed to have n H characters using prime factors
    """
    if (n < 2):
        return 0

    operations = 0
    end = int(sqrt(n))
    while (n % 2 == 0):
        operations += 2
        n /= 2
    if (n < end):
        end = int(n)
    for factor in range(3, end + 1, 2):
        if (n == 1):
            break
        while (n % factor == 0):
            operations += factor
            n = n / factor
    return operations if operations > 0 else n