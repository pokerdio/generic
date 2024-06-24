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


def make_isprime(primes=init_primes(50), max_prime=[50]):

    def f(n):
        if n >= max_prime[0]:
            max_prime[0] = int(n * 1.2 + 5)
            primes.update(init_primes(max_prime[0]))
        return n in primes

    global isprime
    isprime = f


make_isprime()


def go():
    maxprimes = 0
    besta, bestb = 0, 0

    primes = []
    for a in range(-1000, 1001):
        for b in range(-1000, 1001):
            n = 0
            while True:
                p = n * n + a * n + b
                if isprime(p):
                    n = n + 1
                else:
                    break
            if n > maxprimes:
                maxprimes = n
                besta, bestb = a, b
    print(besta * bestb, maxprimes, besta, bestb)
