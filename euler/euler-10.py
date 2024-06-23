#!/usr/bin/env python3

import math
import primez
from builtins import sum


def foo(n=2000000):
    print(sum(primez.iterate_primez(n)))


def subprime(p):
    """finds the biggest prime < p"""
    if p < 2:
        return 0
    pv = primez.primez
    if pv[-1] < p:
        primez.init_primes(int((p + 100) * 1.1))
        pv = primez.primez

    i, j = 0, len(pv) - 1
    while j - i > 1:
        k = (i + j) // 2
        if pv[k] > p:
            j = k
        else:
            i = k
    return pv[i]


def s(x, p, d={}):
    if p < 2:
        return x * (x + 1) // 2
    if p == 2:
        x = x - (1 - x % 2)
        return (x + 1) * ((x + 1) // 2) // 2
    xp = (x, p)
    if xp in d:
        return d[xp]
    if not primez.isprime(p):
        return s(x, subprime(p))

    sp = subprime(p - 1)
    ret = s(x, sp) - p * s(x // p, sp)
    d[xp] = ret
    return ret


def sumprimez(n):
    n2 = int(math.sqrt(n))
    return sum(primez.iterate_primez(n2 + 1)) + s(n, n2) - 1


def _s(x, p):
    v = list(range(x + 1))
    v[0] = 0

    for i in primez.iterate_primez(p + 1):
        for j in range(i, x + 1, i):
            v[j] = 0
    return sum(v)


def decompose_str(i):
    i = primez.decompose(i)
    keys = sorted(i.keys())
    s = ""
    for key in keys:
        for _ in range(i[key]):
            if s:
                s = s + "*"
            s += str(key)
    return s


def _s2(x, p):
    s = 0
    tx = ""
    for i in range(1, x + 1):
        for j in range(2, p + 1):
            if i % j == 0:
                break
        else:
            s += i
            if not primez.isprime(i):
                tx += str(decompose_str(i)) + " "
    print(tx)
    return s
