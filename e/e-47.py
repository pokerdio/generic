#!/usr/bin/env python3

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


def foo(sequence):
    primes = init_primes(1000)

    run = 0
    i = 1
    while True:
        i += 1

        if i > primes[-1]:
            primes = init_primes(primes[-1] * 4)

        icopy = i
        k = 0
        for p in primes:
            if p > icopy:
                break
            if icopy % p == 0:
                k += 1
                icopy = icopy // p
                while icopy % p == 0:
                    icopy = icopy // p

            if k > sequence:
                break
        if k != sequence:
            run = 0
        else:
            run += 1
            if run == sequence:
                return i + 1 - sequence
