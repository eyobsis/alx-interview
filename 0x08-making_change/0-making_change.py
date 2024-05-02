#!/usr/bin/python3
"""
Calculate minimum coins needed to make a given amount.
"""


def makeChange(coins, total):
    """
    Calculate minimum coins needed to make total amount.

    Args:
        coins (list): Available coin denominations.
        total (int): Total amount to make change for.

    Returns:
        int: Minimum coins needed, or -1 if not possible.
    """
    mcn = [float('inf')] * (total + 1)
    mcn[0] = 0
    for i in range(1, total + 1):
        for coin in coins:
            if i >= coin:
                mcn[i] = min(mcn[i], mcn[i - coin] + 1)
    minimum_coins_needed = mcn[total] if mcn[total] != float('inf') else -1
    return minimum_coins_needed
