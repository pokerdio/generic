import primez
from math import gcd


def maxpow(p, n):
    ret = 1
    for i in range(n):
        if p ** i <= n:
            ret = i
        else:
            return ret


def ham(n):
    maxpow2 = maxpow(2, n)
    maxpow3 = maxpow(3, n)
    maxpow5 = maxpow(5, n)
    for two in range(maxpow2 + 1):
        for three in range(maxpow3 + 1):
            for five in range(maxpow5 + 1):
                k = 2 ** two * 3 ** three * 5 ** five
                if k <= n:
                    yield k


def naive_totient(n):
    return 1 + sum(gcd(i, n) == 1 for i in range(2, n))


def naive_go(n=100):
    h = sorted(ham(n))
    for i in range(1, n):
        if naive_totient(i) in h:
            yield i


def products(p, n, i0=0):
    for i in range(i0, len(p)):
        k = p[i]
        if k > n:
            return
        yield k
        for j in products(p, n // k + 1, i + 1):
            if k * j <= n:
                yield k * j


def go(n=10**12):
    h = sorted(ham(n))
    p = [x + 1 for x in h[5:] if primez.rm_prime(x + 1)]
    p = [1] + sorted(products(p, n))
    for i in h:
        for j in p:
            if i * j > n:
                break
            yield i * j


print(sum(go(10**12)) % 2 ** 32)
