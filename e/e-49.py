#!/usr/bin/env python3

#

from bitarray import bitarray as ba


def init_primes(n):
    sieve = ba(n)
    sieve[:] = True
    primez = set()
    for i in range(2, n):
        if sieve[i]:
            sieve[i * 2:n:i] = False
            primez.add(i)

    return primez


def test(lst):
    lst = sorted(lst)
    for i in range(len(lst) - 2):
        a = lst[i]
        for j in range(i + 1, len(lst)):
            b = lst[j]
            c = a + 2 * (b - a)
            if c in lst:
                return a, b, c


def foo():
    primez = init_primes(10000)
    d = {}

    for p in primez:
        if p > 999:
            key = "".join(sorted(str(p)))
            d[key] = d.get(key, [])

            d[key].append(p)

    for key, primez in d.items():
        if len(primez) >= 3:
            if test(primez):
                print(test(primez))
