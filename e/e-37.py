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


def go(n):
    primes = init_primes(n)

    for prime in primes:
        if prime < 10:
            continue
        s = str(prime)

        okay = True
        for i in range(1, len(s)):
            #            print("sub ", s[i:], s[:i])
            if int(s[i:]) not in primes or int(s[:i]) not in primes:
                okay = False
                break
        if okay:
            yield(prime)


print(sum([x for x in go(10**6)]))
