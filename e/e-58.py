#!/usr/bin/env python3

#

from bitarray import bitarray as ba
from itertools import islice


def init_primes(n):
    print("initializing primes", n)
    sieve = ba(n)
    sieve[:] = True
    primez = set()
    for i in range(2, n):
        if sieve[i]:
            sieve[i * 2:n:i] = False
            primez.add(i)

    return primez


primez = init_primes(100)
primez_max = 99


def isprime(n):
    global primez_max
    global primez
    if n >= primez_max:
        primez_max = n * 3
        primez = init_primes(primez_max)

    return n in primez


def stepper():
    x, step = 1, 2
    while True:
        for _ in range(4):
            x += step
            yield x
        step += 2


def answer():
    k, p = 0, 0
    s = stepper()
    while True:
        k += 4
        p += sum(isprime(x) for x in islice(s, 4))
        print(p, k)
        if p * 10 < k:
            return k // 2 + 1
