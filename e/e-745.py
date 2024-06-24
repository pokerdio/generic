import numpy as np


def foo(n):
    i = 2
    v = np.full(n + 1, 1)
    while i * i <= n:
        i2 = i * i
        i += 1
        v[i2::i2] = i2

    return sum(v) - 1, v


def go(n2):
    """solves the problem for n2**2"""

    n = n2 * n2

    n22 = int(sqrt(n2))
    ret = n2 * n2
    v = np.full(n2 + 1, 0)
    for i in range(n2, 0, -1):
        if i < n22:
            print(i)
        v[i] = n // (i * i) - v[i * 2:: i].sum()
        ret = (ret + v[i] * (i * i - 1)) % 1000000007
    return ret
