#!/usr/bin/env python3

import itertools


def make_primes(n):
    ret = set(range(3, n + 1, 2))
    ret.add(2)
    for i in range(3, int(math.sqrt(n)) + 2):
        if i in ret:
            ret -= set(range(i * 2, n + 1, i))
    return sorted(ret), ret


primes, primes_set = make_primes(12001)


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
    divz = getdivz(n)

    for p in divz:
        n = n * (p - 1) // p
    return n


def foo(n, min, max):
    s = set(Fr(a, b) for a in range(1, n) for b in range(a + 1, n + 1)
            if 3 * a > b if a * 2 < b)
    return len(s)
