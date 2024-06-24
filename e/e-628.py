from itertools import permutations as perm
from copy import deepcopy

import numpy as np


def pri(pos):
    for line in pos:
        print("".join(str(x) for x in line))
    print()


def gen(n):
    ret = 0
    zero = [[0] * n for _ in range(n)]
    onetwo = [0, 0, 0, 0]
    for p in perm(range(n)):
        if p[0] != 0 and p[n - 1] != n - 1:
            pos = deepcopy(zero)
            for i in range(n):
                pos[i][p[i]] = 1

            one, two = paint(pos)
            onetwo[one + two * 2] += 1
            if pos[n - 1][n - 1] == 2:
                ret += 1
            # else:
            #     print(one, two)
            #     pri(pos)
    return ret, onetwo


def paint(v):
    n = len(v)
    v[0][0] = 2

    one, two = 0, 0

    for i in range(1, n):
        x, y = i, 0
        k = 1
        for j in range(i + 1):
            if v[y][x] == 0:
                k = 0
                if (x > 0 and v[y][x - 1] == 2):
                    v[y][x] = 2

                if (y > 0 and v[y - 1][x] == 2):
                    v[y][x] = 2

            x = x - 1
            y = y + 1
        if k and i < n - 1:
            one = 1
    for i in range(1, n):
        x, y = n - 1, i
        k = 1
        for j in range(n - i):
            if v[y][x] == 0:
                k = 0
                if (x > 0 and v[y][x - 1] == 2):
                    v[y][x] = 2

                if (y > 0 and v[y - 1][x] == 2):
                    v[y][x] = 2

            x = x - 1
            y = y + 1
        if k:
            two = 1
    return one, two


if not "fact" in locals():
    fact = np.zeros(10**8 + 1, np.int64)


def make_fact(n):
    global fact
    mod = 1008691207
    fact[0] = 1
    fact[1] = 1
    for i in range(2, n + 1):
        if i % 100000 == 0:
            print(i)
        fact[i] = i * int(fact[i - 1]) % mod


def go(n):
    mod = 1008691207
    global fact
    assert(len(fact) >= n)

    op = ((n - 2) * (n - 2) + n - 1) * int(fact[n - 2])

    mono = int(fact[n - 2]) - 1

    print("mono", mono)
    duo = 0
    for i in range(4, n + 1):
        duo += (i - 3) * int(fact[n - i])
    duo = duo % mod
    print("final duo", duo)
    return (op - mono * 2 - 1 + duo) % mod
