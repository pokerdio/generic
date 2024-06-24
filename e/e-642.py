#!/usr/bin/env python3


# f(n) = largest prime factor of n
# WORK IN PROGRESS


def test():
    assert(f(10) == 32)
    assert(f(100) == 1915)
    assert(f(10000) == 10118280)


primez = 0


def init_primez(n):
    global primez
    primez = set(range(2, n + 1))

    for i in range(2, n + 1):
        if i in primez:
            for j in range(i * 2, n + 1, i):
                if j in primez:
                    primez.remove(j)


def solve(n):
    init_primez(int(math.sqrt(n) + 1))


solve(201820182018)
