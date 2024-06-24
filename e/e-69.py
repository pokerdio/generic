#!/usr/bin/env python3

import itertools


def make_primes(n):
    ret = set(range(3, n + 1, 2))
    ret.add(2)
    for i in range(3, int(math.sqrt(n)) + 2):
        if i in ret:
            ret -= set(range(i * 2, n + 1, i))
    return sorted(ret)


primes = make_primes(10 ** 6)


def getdivz(n):
    global primes
    divz = set()
    for p in primes:
        while n % p == 0:
            divz.add(p)
            n //= p
        if p > n:
            break
    return divz


def phi(n):
    global primes
    divz = getdivz(n)
    v = set(range(1, n))
    for div in divz:
        v -= set(range(div, n, div))

    return n / len(v)


def go():
    bestp, besti = 0, 0
    for i in range(2310, 10**6 + 1, 2310):
        p = phi(i)
        print(i, p, besti, bestp)
        if p > bestp:
            bestp = p
            besti = i
    return besti, bestp
