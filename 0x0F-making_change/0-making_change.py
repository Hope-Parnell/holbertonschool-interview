#!/usr/bin/python3
"""given a list of coins make change for a given amont"""


def makeChange(coins, total):
    """Return the minuimun number of coins needed to make change"""
    if total <= 0:
        return 0
    coinsNeeded = 0
    coins.sort(reverse=True)
    for coin in coins:
        coinsNeeded += total // coin
        total %= coin
        if total == 0:
            break
    return coinsNeeded if total == 0 else -1
