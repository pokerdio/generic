#!/usr/bin/env python3
from bitarray import bitarray as ba
from math import sqrt, gcd
import itertools as it
from random import randint
import numpy as np


def init_primes(n):
    global maxprime, primez, primez_set
    if n > maxprime:
        maxprime = n
        primez, primez_set = create_primes(maxprime)
    return primez, primez_set


def create_primes(n):
    sieve = ba(n)
    sieve[:] = True
    primez = []
    primez_set = set()
    for i in range(2, n):
        if sieve[i]:
            sieve[i * 2:n:i] = False
            primez.append(i)
            primez_set.add(i)

    return primez, primez_set


maxprime = 10
primez, primez_set = create_primes(maxprime)


def isprime(n):
    global maxprime, primez, primez_set
    if n >= maxprime:
        primez, primez_set = init_primes(int(n * 1.2))

    return n in primez_set


def isprime_slow(n):
    if n < 2:
        return False
    for i in iterate_primez(int(sqrt(n + 1) + 1)):
        if n % i == 0:
            return False
    return True


def coprime2(a, b):
    a, b = min(a, b), max(a, b)

    assert (a > 0)
    for i in iterate_primez(min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            return False
    return True


def coprime(a, b):
    return gcd(a, b) == 1


def test_coprime(n=100):
    for i in range(1, n):
        for j in range(1, n):
            if coprime(i, j) != coprime2(i, j):
                print("Alarm", i, j)
                assert(False)


def iterate_primez(maxp=None):
    global maxprime, primez, primez_set
    idx = 0
    while True:
        idx, r = len(primez), range(idx, len(primez))
        for i in r:
            p = primez[i]
            if maxp and maxp <= p:
                return
            yield p

        primez, primez_set = init_primes(maxprime * 3)


ip = iterate_primez


def decompose(n):
    factors = {}

    root = int(sqrt(n) + 1)
    for p in iterate_primez(root):
        if n % p == 0:
            while n % p == 0:
                n //= p
                factors[p] = factors.get(p, 0) + 1
            if n in primez_set:
                factors[n] = factors.get(n, 0) + 1
                n = 1
        if n == 1:
            break
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors


def prod(ittie):
    ret = 1
    for i in ittie:
        ret *= i
    return ret


def decompose_iterate(n):
    if type(n) == int:
        n = decompose(n)
    for combo in it.product(*(tuple(i ** p for p in range(j + 1))
                              for i, j in n.items())):
        yield prod(combo)


init_primes(1000)


def rm_prime_kapow(a, b, p):
    ret = 1

    while b > 0:
        if b % 2 == 1:
            ret = (ret * a) % p
        a = a * a % p
        b //= 2
    return ret


def rm_prime(n, attempts=3):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    if n % 3 == 0:
        return n == 3
    if n % 5 == 0:
        return n == 5

    n1 = n - 1
    m = n1
    twos = 0
    while m % 2 == 0:
        m //= 2
        twos += 1

    base = 2
    for _ in range(attempts):
        k = rm_prime_kapow(base, m, n)

        alarm = k > 1 and k < n1

        for _ in range(twos):
            if k == n1:
                alarm = False
            elif k == 1:
                if alarm:
                    return False
                else:
                    break
            k = k * k % n
        else:
            if k != 1:
                return False
        if base < 4:
            base += 1
        else:
            base = randint(5, n1 - 1)
    return True


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        gcd, x, y = egcd(b % a, a)
        return (gcd, y - (b // a) * x, x)


def rev(n, mod):
    _, x, _ = egcd(n, mod)
    return x % mod


def lcm(*args):
    if not args:
        return 1
    ret = args[0]
    for i in args[1:]:
        ret = ret * i // gcd(ret, i)

    return ret


def iterate_primez_stage(n):
    """works up to ~100 trillions; does not save the data"""
    p20 = list(iterate_primez(20))
    windown = lcm(*p20)
    assert n < windown ** 2
    v0 = np.ones(windown, dtype=np.bool)
    v = v0.copy()
    for p in p20:
        v0[::p] = False

    vp = list(p for p in iterate_primez(int(sqrt(n)) + 2) if p >= 23)

    yield from iterate_primez(min(windown, n))
    bottom = windown
    while bottom <= n:
        v = v0.copy()
        for p in vp:
            v[p - bottom % p::p] = False

        for i in range(min(windown, n - bottom + 1)):
            if v[i]:
                yield bottom + i
        bottom += windown


def memdecompose(n, d={}):
    if n not in d:
        d[n] = decompose(n)
    return d[n]


def totient(m, d={}):
    if m in d:
        return d[m]
    for p in decompose(m):
        m = m // p * (p - 1)
    return m
