#!/usr/bin/python3
'''Making Change module.
'''


def makeChange(coins, total):
    ''' Determine the fewest number of coins needed to meet a given amount
    total,given a pile of coins of different values.
    '''
    if total <= 0:
        return 0

    coins = sorted(coins, reverse=True)

    rem = total
    count = 0

    for coin in coins:
        while coin <= rem:
            rem -= coin  # Subtract the coin value from remaining amount
            count += 1
            if rem == 0:
                return count  # Return count if remaining amount becomes zero
            elif rem < 0:
                return -1  # If remaining amount becomes negative, not possible

    return -1  # If loop completes without reaching zero, return -1
