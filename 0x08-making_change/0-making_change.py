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
    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[total] if dp[total] != float('inf') else -1
