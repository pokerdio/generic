#!/usr/bin/env python3

#


coins = (200, 100, 50, 20, 10, 5, 2, 1)

solutions = 0


def go(coins, money):
    global solutions
    if len(coins) == 1:
        if money % coins[0] == 0:
            solutions += 1
    else:
        for i in range(0, money // coins[0] + 1):
            go(coins[1:], money - i * coins[0])


go(coins, 200)
print(solutions)
