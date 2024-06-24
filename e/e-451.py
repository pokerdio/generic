from math import sqrt
import itertools as it


def decomp(n, sv):
    ret = {}
    while sv[n]:
        div = sv[n]
        while n % div == 0:
            ret[div] = ret.get(div, 0) + 1
            n //= div
    if n > 1:
        ret[n] = 1
    return ret


def prod(ittie):
    ret = 1
    for i in ittie:
        ret *= i
    return ret


def decomp_iterate(c):
    for combo in it.product(*(tuple(i ** p for p in range(j + 1))
                              for i, j in c.items())):
        yield prod(combo)


def comp(dec1, dec2):
    ret = dec1.copy()

    for p, q in dec2.items():
        ret[p] = ret.get(p, 0) + q
    return ret


def sieve(n):
    v = [0] * (n + 1)
    for i in range(2, int(sqrt(n)) + 1):
        if not v[i]:
            for j in range(i * 2, n + 1, i):
                v[j] = i
    return v


def go(n):
    sv = sieve(n)
    ret = [1] * (n + 1)
    for a in range(2, n):
        if a % 10000 == 0:
            print(a)
        for d in decomp_iterate(comp(decomp(a - 1, sv), decomp(a + 1, sv))):
            if d - 1 > a and d <= n:
                ret[d] = a
    return sum(ret[3:])


print(go(2 * 10**7))
