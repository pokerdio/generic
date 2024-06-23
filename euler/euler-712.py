import primez
import prime_counting as pc
from builtins import sum


def naive_d(m, n):
    m, n = primez.decompose(m), primez.decompose(n)
    ret = 0
    for i in set(m.keys()) | set(n.keys()):
        ret += abs(m.get(i, 0) - n.get(i, 0))
    return ret


def naive_s(n):
    ret = 0
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            ret += 2 * naive_d(i, j)
    return ret


s = naive_s
d = naive_d


def bucketz(p, x):
    ret = [0]
    n = x
    while n >= p:
        ret.append(n // p)
        ret[-2] -= ret[-1]
        n //= p
    ret[0] = x - sum(ret[1:])
    return ret


def bucketz_delta(b):
    s = 0
    for i in range(len(b) - 1):
        for j in range(i + 1, len(b)):
            s += (j - i) * b[i] * b[j]
    return s * 2


def naive_bucketz_s(n):
    ret = 0
    for p in primez.iterate_primez(n + 1):
        b = bucketz(p, n)
        ret += bucketz_delta(b)
    return ret


def bucketz_s(p, n):
    ret = 0
    for p2 in primez.iterate_primez(p + 1):
        ret += bucketz_delta(bucketz(p2, n))
    return ret


def go(n=10**12):
    assert(n <= 10**12)
    primez.init_primes(10**8)

    if n == 10 ** 12:
        pi0 = 37607912018
    else:
        pi0 = pc.pi(n)

    n0 = n
    ret = 0
    for i in range(2, int(n ** (1/3) + 0.001) + 1):
        n1 = n // i
        pi1 = pc.pi(n1)

        dp = (pi0 - pi1) * (i - 1)

        ds = dp * (n - (i - 1)) * 2
        print("%d primez between %d and %d contribute %d" % (pi0 - pi1, n1, n0, ds))
        ret += ds

        n0, pi0 = n1, pi1

    ret += bucketz_s(n0, n)
    return ret


def test_go():
    for i in range(1, 1000):
        if go(i) != s(i):
            return i


# 7571791796889109621082430
