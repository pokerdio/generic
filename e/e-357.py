#!/usr/bin/env python3

# https://projecteuler.net/problem=357


# observation: a number fitting the given condition cannot have
# as a divisor a superior power of a prime divisor

from bitarray import bitarray as ba
import itertools
import operator


def init_primes(n):
    sieve = ba(n)
    sieve[:] = True
    primez = []
    for i in range(2, n):
        if sieve[i]:
            sieve[i * 2:n:i] = False
            primez.append(i)

    return primez


def test(n, prime_divz, prime_set):
    n2 = n
    for i in range(len(prime_divz)):
        lst = [1]
        p = prime_divz[i]
        pexp = p
        while n2 % p == 0:
            n2 //= p
            lst.append(pexp)
            pexp *= p
        prime_divz[i] = lst

#    print("testing", n, prime_divz)
    for lst in itertools.product(*prime_divz):
        k = reduce(mul, lst, 1)
        assert n % k == 0, k
        if (k + n // k) not in prime_set:
            return False
    return True


def go(n):
    primez = init_primes(n + 2)
    print("sieve over")
    isprime = set(primez)

    s = 1
    for p in primez[1:]:
        k = p - 1

        ok = True

        prime_divz = []
        for p2 in primez:
            if p2 * p2 > k:
                break
            if k % p2 == 0:
                if k % (p2 * p2) == 0:
                    ok = False
                    break
                if p2 + k // p2 not in isprime:
                    ok = False
                    break
                prime_divz.append(p2)
        if ok and test(k, prime_divz, isprime):
            #            print("adding", k)
            s = s + k
    return s
