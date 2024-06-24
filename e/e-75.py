#!/usr/bin/env python3

import math

#!/usr/bin/env python3

#

from bitarray import bitarray as ba


def init_primes(n):
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
primez, primez_set = init_primes(int(750000 ** 0.5 + 10))


def divzsq(n):
    """gets the divizors of n squared"""

    divz = []
    powz = []
    for p in primez:
        k = 0
        while n % p == 0:
            k += 1
            n //= p
        if k > 0:
            divz.append(p)
            powz.append(k * 2)

        if n == 1:
            break
    if n > 1:
        divz.append(n)
        powz.append(2)

    return divz, powz


def subcount(v):
    """returns an interator to v sized lists of positive numbers each
    smaller or equal to the one in v in the same position    """
    ret = [0] * len(v)

    p = 1
    for i in v:
        p *= i + 1

    yield ret[:]
    for _ in range(p - 1):
        ret[0] += 1
        for i in range(len(v)):
            if ret[i] > v[i]:
                ret[i] = 0
                ret[i + 1] += 1
            else:
                break
        yield ret[:]


def decompose_ab(n):
    """iterator to all the pairs of positives whose product is n"""
    divz, powz = divzsq(n)
    n2 = n * n
    count = len(powz)

    for power in subcount(powz):
        k = 1
        for i in range(count):
            for j in range(power[i]):
                k *= divz[i]

        yield k, n2 // k


def pythagoras_triangles(n):
    for a, b in decompose_ab(n):
        if a > b and ((a + b) % 2 == 0):
            hypo = (a + b) // 2  # hypotenuse
            c = (a - b) // 2  # one of the cathetus(n is the other)

            yield hypo, c, n  # c, n can't be equal with all rationals


def solve():
    d = {}
    for i in range(2, 750002):
        if i % 10000 == 1:
            print(i)
        for h, c1, c2 in pythagoras_triangles(i):
            s = h + c1 + c2
            if s <= 1500000:
                d[s] = d.get(s, 0) + 1

    print(len([d[x] for x in d.keys() if d[x] == 2]))
    return d
