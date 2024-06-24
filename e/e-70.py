#!/usr/bin/env python3

import itertools


def make_primes(n):
    ret = set(range(3, n + 1, 2))
    ret.add(2)
    for i in range(3, int(math.sqrt(n)) + 2):
        if i in ret:
            ret -= set(range(i * 2, n + 1, i))
    return sorted(ret), ret


primes, primes_set = make_primes(10 ** 7)


def getdivz(n):
    global primes

    if n in primes_set:
        return set((n,))

    maxp = int(math.sqrt(n) + 2)

    divz = set()
    for p in primes:
        while n % p == 0:
            divz.add(p)
            n //= p
            if n in primes_set:
                divz.add(n)
                return divz
        if p > n or p > maxp:
            break
    return divz


def phi(n):
    global primes
    divz = getdivz(n)
    v = set(range(1, n))
    for div in divz:
        v -= set(range(div, n, div))
    return len(v)


def phi2(n):
    divz = getdivz(n)

    for p in divz:
        n = n * (p - 1) // p
    return n


def go():
    bestp, besti = 9999, 0
    for i in range(2, 10 ** 7 + 1):
        if i % 100000 == 0:
            print(i, bestp, besti)
        p = phi2(i)
        if i / p < bestp:
            if "".join(sorted(str(i))) == "".join(sorted(str(p))):
                bestp = i / p
                besti = i
    return besti, bestp
