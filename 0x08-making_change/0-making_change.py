#!/usr/bin/python3
def makeChange(coins, total):
    """
    Calculate the minimum number of coins needed to make a given total amount.

    Args:
        coins (list): A list of coin denominations.
        total (int): The total amount to make change for.

    Returns:
        int: The minimum number of coins needed to make the total amount. If the total amount cannot be made, return -1.
    """
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total]!= float('inf') else -1
