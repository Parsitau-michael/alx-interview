#!/usr/bin/python3
""" This module represents a function to return the least number of coins
required to make change for a given sum of money.
"""


def makeChange(coins, total):
    """
    The function that returns the least number of coins
    """
    if total <= 0:
        return 0
    
    n = len(coins)

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1