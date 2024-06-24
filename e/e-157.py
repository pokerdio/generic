from primez import decompose
import itertools as it
import numpy as np


def dec(n):
    for combo in it.product(*(tuple(i ** p for p in range(j + 1))
                              for i, j in decompose(n).items())):
        yield np.prod(combo)


def go(n):
    two = 2 ** n
    five = 5 ** n

    for i in range(n + 1):
        ki = 2 ** i
        for j in range(n + 1):
            kj = 5 ** j
            q = two * five * (ki + kj) // ki // kj
            for k in dec(q):
                yield tuple(sorted((ki * k, kj * k, q // k)))

            kij = ki * kj
            q = two * five * (1 + kij) // kij
            for k in dec(q):
                yield tuple(sorted((k, kij * k, q // k)))


def solve(n):
    return sum(len(set(go(i))) for i in range(1, n + 1))
