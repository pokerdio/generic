from math import gcd
from builtins import sum


def foo(n):
    ret = 0

    for j in range(1, n + 1):
        for i in range(1, j + 1):
            ret += gcd(i, j)
    return ret
