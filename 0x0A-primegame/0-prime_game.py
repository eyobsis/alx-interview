#!/usr/bin/python3
"""
Define the isWinner function, a solution to the Prime Game problem
"""


def primes(n):
    """Return a list of prime numbers between 1 and n inclusive."""
    prime = []
    sieve = [True] * (n + 1)
    for p in range(2, n + 1):
        if sieve[p]:
            prime.append(p)
            for i in range(p, n + 1, p):
                sieve[i] = False
    return prime


def isWinner(x, nums):
    """
    Determine the winner of the Prime Game.

    Args:
        x (int): Number of rounds of the game.
        nums (list): List of upper limits of ranges for each round.

    Returns:
        str: Name of the winner (Maria/Ben), / None if the winner
    """
    if x is None or nums is None or x == 0 or nums == []:
        return None
    Maria = Ben = 0
    for i in range(x):
        prime = primes(nums[i])
        if len(prime) % 2 == 0:
            Ben += 1
        else:
            Maria += 1
    if Maria > Ben:
        return "Maria"
    elif Ben > Maria:
        return "Ben"
    return None
