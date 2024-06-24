#!/usr/bin/env python3



# the prime divisors of a number appear in its unitary divisors with
# either a 0 coefficient or the maximum coefficient


# for a prime divisor of a number, the sum of the squares of the
# unitary divisors of the numbers can be divided in the sum of the
# squares of the unitary divisors that contain that prime, and those
# that don't; let these be p as the prime, x its power coefficient in
# the number and S_with_p, S_without_p the sums; then
# S_with_p = p^2x * S_without_p; inductively, the total S becomes the
# product of (1 + p ^ 2x) for all the primes

from math import sqrt
import itertools

from bitarray import bitarray as ba


def init_primes(n):
    sieve = ba(n)
    sieve[:] = True
    primez = []
    for i in range(2, n):
        if sieve[i]:
            sieve[i * 2:n + 1:i] = False
            primez.append(i)

    return primez


def prime_expo_in_factorial(prime, n):
    a = prime
    ret = 0
    while a <= n:
        ret += n // a
        a *= prime
    return ret


def expo(n, power, modulo):
    if power == 0:
        return 1

    ret = 1

    while power > 0:
        if power % 2 == 1:
            power -= 1
            ret *= n
            ret %= modulo

        n = (n ** 2) % modulo
        power = power // 2
    return ret


def solve(n, modulo):
    primes = init_primes(n)
    print("primes initialized count %d" % len(primes))

    ret = 1
    for p in primes:
        exp = prime_expo_in_factorial(p, n)
        p2exp = expo(p, exp * 2, modulo)
        ret = ((1 + p2exp) * ret) % modulo

    return ret


def test():
    p = init_primes(15)
    assert(p == [2, 3, 5, 7, 11, 13])

    p = init_primes(666)
    p2 = []
    for i in range(2, 667):
        ok = True
        for j in range(2, i):
            if i % j == 0:
                ok = False
                break
        if ok:
            p2.append(i)
    assert(p == p2)

    total = 0

    for i in range(1, 666):

        k = i
        while k % 5 == 0 and k > 0:
            total += 1
            k //= 5
        assert total == prime_expo_in_factorial(5, i), \
            "error at %d; total %d" % (i, total)

    for i in range(1, 66666, 237):
        for j in range(1, 235, 17):
            a = 1
            for k in range(j):
                a = (a * i) % j
            assert(expo(i, j, j) == a), "error at %d %d" % (i, j)


test()
print(solve(100000000, 1000000009))
