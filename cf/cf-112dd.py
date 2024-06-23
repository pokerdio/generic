import sys
from math import sqrt
import itertools as it
from functools import reduce
from operator import mul
input_str = sys.stdin.read().split()
input_str_idx = 0


def pop_int():
    global input_str_idx
    input_str_idx += 1
    return int(input_str[input_str_idx - 1])


n = pop_int()
vx, vy = zip(*[(pop_int(), pop_int()) for _ in range(n)])
m = max(vx)
div = [0] * n


def genp(n):
    v = [1] * (n + 1)
    for i in range(2, int(sqrt(n)) + 1):
        if v[i]:
            for j in range(i * 2, n + 1, i):
                v[j] = 0
    return [i for i in range(2, n + 1) if v[i]]


pv = genp(int(sqrt(m)) + 3)


def divz(x, pv=pv):
    d = {}
    for p in pv:
        while x % p == 0:
            x //= p
            d[p] = d.get(p, 0) + 1
        if x == 1:
            break
    if x > 1:
        d[x] = 1
    v = [[j ** i for i in range(d[j] + 1)] for j in d.keys()]
    for c in it.product(*v):
        yield reduce(mul, c, 1)


latest = {}
for i, x in enumerate(vx):
    k = 0
    cutoff = i - vy[i]
    for d in divz(x):
        if d not in latest or latest[d] < cutoff:
            k += 1
        latest[d] = i
    print(k)
