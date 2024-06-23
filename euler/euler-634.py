#!/usr/bin/env python3

# https://projecteuler.net/problem=634


from math import sqrt
import itertools


def root_floor(n, base):
    root = int(n ** (1.0 / base))
    if root ** base > n:
        root -= 1
    elif (root + 1) ** base <= n:
        root += 1
#    print("root of ", n, "in bae", base, "rets", root)
    return root


def dumb_count(cube, n):
    cubed = cube ** 3
    maxn = root_floor(n // cubed, 2)
    if maxn > 1:
        ret = maxn - 1
    else:
        ret = 0

#    print("dumb_count (%d**3 == %d)" % (cube, cubed), n, "returns", ret)
    return ret


def cubes(n=25):
    print("\n")
    for i in range(2, n + 1):
        print("%d ** 3 == %d" % (i, i ** 3))

# cubes()


def init_prime_squares_cubes(n):
    n = root_floor(n // 8, 6) + 2

    sieve = set(range(2, n))

    primez = []
    for i in range(2, n):
        if i in sieve:
            sieve -= set(range(i * 2, n, i))
            primez.append(i)

    return primez, [x * x for x in primez], [x * x * x for x in primez]


def solve2(n):
    s = 0

    dumb_ones = set(range(2, 8))

    for i in dumb_ones:
        s += dumb_count(i, n)

    print("dumbs", s)
    noms = set()
    for i in range(8, root_floor(n // 4, 3) + 1):
        i3 = i * i * i
        for j in range(2, root_floor(n // i3, 2) + 1):
            noms.add(i3 * j * j)

    s += len(noms)
    for i in dumb_ones:
        i3 = i * i * i
        for nom in noms:
            if nom % i3 == 0:
                j = root_floor(nom // i3, 2)
                if i3 * j * j == nom:
                    s -= 1
    return s


def drain(n, primez, divizors, swamp=None):
    swamp_ret = None
    for i in range(len(primez)):
        root, div = primez[i], divizors[i]
        if div > n:
            break
        while n % div == 0:
            n //= div
            if not swamp_ret:
                swamp_ret = swamp.copy() if swamp else {}

            swamp_ret[root] = swamp_ret.get(root, 0) + 1

    return n, swamp_ret


def number_variants(iresidue, jresidue, six_total):
    if not six_total:
        return 1
    frac = 1
    for k in six_total.values():
        frac *= k + 1
    if iresidue == 1:
        frac -= 1
    if jresidue == 1:
        frac -= 1
    return frac


def brute_solve(n):
    primes, prime_squares, prime_cubes = init_prime_squares_cubes(n)

    count = {}

    for i in range(root_floor(n // 4, 3), 1, -1):
        if (i < 10000) or (i % 10000 == 0):
            print("solving", i)
        i3 = i ** 3

        iresidue, six = drain(i, primes, prime_squares)

        for j in range(2, root_floor(n // i3, 2) + 1):
            jresidue, six_total = drain(j, primes, prime_cubes, six)

            frac = number_variants(iresidue, jresidue, six_total or six)

            assert(frac > 0)
            count[frac] = count.get(frac, 0) + 1

    s = 0
    for frac, x in count.items():
        assert (x % frac == 0)
        s += x // frac

    return s


big = 9 * 10**18

assert(brute_solve(20000) == 130)
assert(brute_solve(3000000) == 2014)

# print(brute_solve(9 * (10 ** 18))) # 4 019 680 944

for i in range(3000000, 30000000, 1000000):
    assert(brute_solve(i) == solve2(i))
