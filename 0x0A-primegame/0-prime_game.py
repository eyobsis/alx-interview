#!/usr/bin/python3
"""
Define the isWinner function, a solution to the Prime Game problem
"""


def primes(n):
    """Return a list of prime numbers between 1 and n inclusive."""
    prime_list = []
    sieve_list = [True] * (n + 1)
    for num in range(2, n + 1):
        if sieve_list[num]:
            prime_list.append(num)
            for multiple in range(num, n + 1, num):
                sieve_list[multiple] = False
    return prime_list


def isWinner(x, nums):
    """
    Determine Game winner.

    Args:
        x (int): Number of game rounds.
        nums (list): List of upper limits of ranges for each round.

    Returns:
        str: winner's Name (Maria/Ben), / None if the winner
    """
    if x is None or nums is None or x == 0 or nums == []:
        return None
    maria_score = ben_score = 0
    for round_num in range(x):
        primes_list = primes(nums[round_num])
        if len(primes_list) % 2 == 0:
            ben_score += 1
        else:
            maria_score += 1
    if maria_score > ben_score:
        return "Maria"
    elif ben_score > maria_score:
        return "Ben"
    return None
