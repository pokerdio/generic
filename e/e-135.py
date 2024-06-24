
import numpy as np


def foo(n):
    v = np.array([0] * n)
    for x in range(2, n):
        v[(-x % 4) * x:(3 * x - 4) * x + 1: 4 * x] += 1

    return list(v)


def bar(n, nsol):
    v = foo(n)
    v = [x for x in range(len(v)) if v[x] == nsol]
    return len(v)


print(135, bar(10**6, 10))
print(136, bar(5 * 10**7, 1))
