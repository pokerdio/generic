# 16x2 +y4 =z2
# y4=(z+4x)(z-4x)
# for all ys within acceptable range (1..sqrt(n)) we factorize y^4
# in products of two numbers in all ways and
# retrieve x and z by making (z-4x) and (z+4x) the two numbers

# experimentally:
# if y is odd gcd(z+4x,z-4x) is always 1
# if y is even, y is divizible by 4
# if y is even, gcd(z+4x, z-4x) is always 8
# this allows for a large speed increase by limiting the ways
# to split y^4 in factors


import math
from itertools import product


def gen_sieve_seed(n):
    p = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    l = 1
    for i in range(n):
        l *= p[i]
    ret = [0] * l
    for i in range(n):
        for j in range(0, l, p[i]):
            ret[j] = p[i]
    return ret


def gen_sieve(n):
    i = [0] * (n + 1)
    seed = gen_sieve_seed(3)
    v = seed * ((n + len(seed) - 1) // len(seed))
    n2 = int(math.sqrt(len(v)))
    for i in range(2, 30):
        if v[i] == i:
            v[i] = 0

    for i in range(2, n2 + 1):
        if v[i] == 0:
            for j in range(2 * i, len(v), i):
                v[j] = i
    return v


def decompose(n, div=gen_sieve(10**8)):
    while n >= 2:
        divn = div[n]
        k = 0
        if divn == 0:
            yield n, 1
            return
        while n % divn == 0:
            n //= divn
            k += 1
        yield divn, k


def gen_div(n):
    v = list(decompose(n))
    ndiv = len(v)
    for pow in (product(*(range(x[1] + 1) for x in v))):
        ret = 1
        for i in range(ndiv):
            ret *= v[i][0] ** pow[i]
        yield ret


def gen_div_odd(n):
    v = list(decompose(n))
    ndiv = len(v)
    for pow in (product(*((0, x[1] * 4) for x in v))):
        ret = 1
        for i in range(ndiv):
            ret *= v[i][0] ** pow[i]
        yield ret


def gen_div_even(n):
    v = sorted(decompose(n))
    assert(v[0][0] == 2)
    assert(n % 4 == 0)

    powahs = [(3, v[0][1] * 4 - 3), *((0, x[1] * 4) for x in v[1:])]
    ndiv = len(v)
    for pow in (product(*powahs)):
        ret = 1
        for i in range(ndiv):
            ret *= v[i][0] ** pow[i]
        yield ret


def gen_div_4(n):
    v = list(decompose(n))
    ndiv = len(v)
    for pow in (product(*(range(x[1] * 4 + 1) for x in v))):
        ret = 1
        for i in range(ndiv):
            ret *= v[i][0] ** pow[i]
        yield ret


def gcd3(a, b, c):
    return math.gcd(a, math.gcd(b, c))


def _go(n):
    """slow early version"""
    n2 = int(math.sqrt(n))
    s = 0
    for y in range(1, n2 + 1):
        if y % 10000 == 0:
            print("doing", y)
        y4 = y ** 4
        for d in gen_div_4(y):
            d2 = y4 // d
            if d < d2 and (d2 - d) % 8 == 0:
                x = (d2 - d) // 8
                z = (d + d2) // 2
                if x > 0 and x <= n and z > 0 and z <= n and gcd3(x, y, z) == 1:
                    print(x, y, z, gcd(z - 4 * x, z + 4 * x), y % 4, y % 16)

                    s += (x + y + z)
    return s


def go(n):
    n2 = int(math.sqrt(n))
    s = 0
    for y in range(1, n2 + 1):
        if y % 4 == 2:
            continue
        if y % 10000 == 0:
            print("doing", y)
        y4 = y ** 4
        for d in (y % 2 and gen_div_odd or gen_div_even)(y):
            d2 = y4 // d
            if d < d2 and (d2 - d) % 8 == 0:
                x = (d2 - d) // 8
                z = (d + d2) // 2
                if x > 0 and x <= n and z > 0 and z <= n and gcd3(x, y, z) == 1:
                    s += (x + y + z)
    return s


print(go(10**16))
