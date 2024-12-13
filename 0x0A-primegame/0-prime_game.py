#!/usr/bin/python3
""" This module represents the function to find who the winner
is in the Prime Game
"""


def isWinner(x, nums):
    """ The function definition
    """
    prime = sieveOfEratosthenes(max(nums))
    primeSet = set(prime)

    mariasWins = 0
    bensWins = 0

    for n in nums:
        if n < 2:
            bensWins += 1  # If n < 2, no primes to play
            continue

        remainingNums = set(range(2, n + 1))
        currentPlayer = "Maria"

        while remainingNums:
            nextPrime = min([p for p in remainingNums if p in primeSet],
                            default=None)

            if not nextPrime:
                if currentPlayer == "Maria":
                    bensWins += 1
                else:
                    mariasWins += 1
                break

            for multiple in range(nextPrime, n + 1, nextPrime):
                remainingNums.discard(multiple)

            currentPlayer = "Ben" if currentPlayer == "Maria" else "Maria"

    return (None if mariasWins == bensWins else "Maria"
            if mariasWins > bensWins else "Ben")


def sieveOfEratosthenes(n):
    """ A helper function to compute all the prime numbers
    upto n using Eratosthene’s method.
    """
    prime = [True for i in range(n + 1)]
    p = 2

    while (p * p <= n):
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
            p += 1

    return [p for p in range(2, n + 1) if prime[p]]
