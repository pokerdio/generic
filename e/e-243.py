import primez
from fractions import Fraction as Fr

thresh = Fr(15499, 94744)

from itertools import product


def smol(s):
    p = 1
    pr = primez.iterate_primez()
    for k in s:
        p *= next(pr) ** k
    return p


def sums(n, maxsum=None):
    maxsum = maxsum or n
    yield (1,) * n
    for i in range(2, min(maxsum, n) + 1):
        for s in sums(n - i, i):
            yield (i, *s)


def smolest(n):
    best = None

    for s in sums(n):
        p = smol(s) - 1
        bad = divz(s)


def res(s):
    x = 1
    y = 1
    p = primez.iterate_primez()
    for a in s:
        b = next(p)
        ba = b ** a
        x = x * (b ** a) * (Fr(b - 1, b))
        y = y * ba
    return x / (y - 1), y


def best(n):
    best = None
    best_res = None
    for s in sums(n):
        resilience, d = res(s)
        if resilience < thresh:
            if not best or d < best:
                best = d
                best_res = resilience
    return best, best_res


def go(n=20):
    for i in range(2, n):
        print(i, best(i))


go()  # you figure it out :) hint best answer is for best(11)
