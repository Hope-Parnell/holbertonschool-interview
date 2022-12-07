#!/usr/bin/python3
"""Prime Game Module"""


def isWinner(x, nums):
    """Function that determines if a player is the winner"""
    if not nums or x < 1 or len(nums) < x:
        return None
    n = max(nums)
    isPrime = [False, False] + [True for i in range(2, n + 1)]
    for i in range(2, int(n**0.5) + 1):
        if isPrime[i]:
            # change all multiples of i to false
            for j in range(i * i, n + 1, i):
                isPrime[j] = False
    maria = 0
    for i in range(x):
        numberPrimes = list.count(isPrime[0:(nums[i] + 1)], True)
        maria += numberPrimes % 2
    return None if maria * 2 == x else "Maria" if maria * 2 > x else "Ben"
