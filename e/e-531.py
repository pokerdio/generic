import primez
from builtins import sum


def mydecompose(n, d={}):
    if n not in d:
        d[n] = primez.decompose(n)
    return d[n]


def toti(m, d={}):
    if m in d:
        return d[m]
    for p in primez.decompose(m):
        m = m // p * (p - 1)
    return m


def totislow(m):
    return sum(gcd(i, m) == 1 for i in range(1, m))


def totitest(n=1000):
    for i in range(2, n):
        assert toti(i) == totislow(i), i


def g(a, n, b, m):
    mn = gcd(m, n)
    if mn > 1:
        r = a % mn

        if r != b % mn:
            return 0

        n1, m1 = n // mn, m // mn

        x1 = g(a // mn, n1, b // mn, m1)
        return mn * x1 + r
    else:
        _, n1, m1 = primez.egcd(n, m)
        return (b * n * n1 + a * m * m1) % (m * n)


def g2(a, n, b, m):
    mn, n1, m1 = primez.egcd(m, n)
    if mn > 1:
        r = a % mn

        if r != b % mn:
            return 0

        x1 = g(a // mn, n // mn, b // mn, m // mn)
        return (mn * x1 + r) % (m * n)
    else:
        return (b * n * n1 + a * m * m1) % (m * n)


def foo(start, stop):
    for n in range(start, stop - 1):
        print(n)
        for m in range(n + 1, stop):
            yield g2(toti(n), n, toti(m), m)


def go():
    return sum(foo(1000000, 1005000))


# 4515432351156203105
