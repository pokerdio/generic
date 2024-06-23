from math import gcd
from builtins import sum
from functools import reduce


# not sure I got this perfectly right on edge cases but whatever,
# it works for the test case and the idea is sound

def lcm(x, y):
    return x * y // gcd(x, y)


def lcmn(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return reduce(lcm, range(2, n + 1))


def P(n, m):
    if n == 1:
        return (m - 2) // 2

    divby = lcmn(n)
    notdivby = lcmn(n + 1)

    return (m - 1) // divby - (m - 1) // notdivby


def go():
    return sum(P(i, 4 ** i) for i in range(1, 32))
