import numpy as np


def ndiv(n):
    v = np.array([1] * (n + 1))
    for i in range(2, n + 2):
        v[::i] += 1
    return v


def solve(n=10**7):
    ret = 0
    v = ndiv(n)

    for i in range(2, len(v) - 1):
        if v[i] == v[i + 1]:
            ret += 1
    return ret
