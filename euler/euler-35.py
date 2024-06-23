#!/usr/bin/env python3

# https://projecteuler.net/problem=35
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


def go():
    primes = init_primes(1000000)

    total = 0
    for i in primes:
        ok = True
        si = str(i)
        for a in range(len(si)):
            s2 = si[a:] + si[:a]
            if int(s2) not in primes:
                ok = False
                break
        if ok and i > 10:
            print(i)
            total += 1
    return total
