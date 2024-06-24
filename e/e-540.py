
from itertools import count, islice


#from fractions import gcd


def make_pythagoras_triples(maxn):
    ret = 0

    for m in range(1, int(1 + math.sqrt(maxn * 2)), 2):
        if m % 100 == 1:
            print(m)

        limit = min(m - 1, maxn // m, int(sqrt(maxn * 2 - m*m))) + 1
        for n in range(1, limit, 2):
            if gcd(m, n) == 1:
                #abc = tuple(sorted((m * n, (m * m + n * n) // 2, (m * m - n * n) // 2)))
                #assert (abc not in ret)
                # if max(abc) < maxn:
                #    ret.add(abc)
                ret += 1
    return ret


def go(maxperimeter=10**8):
    k = 0
    trips = make_pythagoras_triples(maxperimeter)
    for abc in trips:
        a, b, c = abc
        if c % (b - a) == 0:
            k += trips[abc]
    return k


def sieve_odd(n):
    """finds prime odds; the first odd (index 0) is 1"""
    n2 = int(sqrt(n)) // 2
    n = (n - 1) // 2

    ret = [0] * (n + 1)
    ret[0] = 1  # 1 is not a prime
    for i in range(1, n2 + 1):
        if not ret[i]:
            for j in range(i * 3 + 1, n + 1, 2 * i + 1):
                ret[j] = i
    return ret


def primes(n):
    v = sieve_odd(n)
    return [2 * x + 1 for x in range(1, len(v)) if not v[x]]


def foo(n):
    """prints readably the output of sieve"""
    v = sieve_odd(n)
    return "".join("%d(%d) " % (2 * x + 1, v[x]*2+1)for x in range(len(v)))


def partial_totient():
    pass
