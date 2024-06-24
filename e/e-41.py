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


def go(n=987654322):
    primez = init_primes(n)

    digitz = set("123456789"[:x] for x in range(4, 10))
    print(digitz)
    for p in primez[::-1]:
        if "".join(sorted(str(p))) in digitz:
            return p
