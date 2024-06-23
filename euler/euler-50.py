#!/usr/bin/env python3

# https://projecteuler.net/problem=27
#

from bitarray import bitarray as ba


def init_primes(n):
    sieve = ba(n)
    sieve[:] = True
    primez = []
    for i in range(2, n):
        if sieve[i]:
            sieve[i * 2:n:i] = False
            primez.append(i)

    return primez


def foo(n):
    primez = init_primes(n)
    primez_set = set(primez)
    bestk = 0
    bests = 0
    for i in range(len(primez)):
        s = 0
        k = 0
        for j in range(i, len(primez)):
            s += primez[j]
            if s > n:
                break
            k += 1
            if k > bestk and s in primez_set:
                bestk = k
                bests = s
                print("new best %d = %s" %
                      (bests, " + ".join(str(primez[x]) for x in range(i, j + 1))))
    return bests
