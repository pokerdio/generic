import primez
import numpy as np
from math import gcd


def lcm(*args):
    if not args:
        return 1
    ret = args[0]
    for i in args[1:]:
        ret = ret * i // gcd(ret, i)

    return ret


def foo(n):
    k = 1  # they say 1 counts because it has no prime factors, so

    primez.init_primes(int(sqrt(n + 5) + 1))

    for i in range(4, n + 1):  # 2 and 3 are primez they bad; 1 is counted
        j = i
        if i % 100000 == 99999:
            print(i)
        iroot = int(sqrt(i))
        if iroot * iroot < i:
            iroot += 1
        for p in primez.iterate_primez(iroot):
            while i % p == 0:
                i //= p
            if i < iroot:
                k += 1
                break
    return k


def gen_primez_stage(n):
    """works up to ~100 trillions"""
    p20 = list(primez.iterate_primez(20))
    windown = lcm(*p20)
    v0 = np.ones(windown, dtype=np.bool)
    v = v0.copy()
    for p in p20:
        v0[::p] = False

    vp = list(p for p in primez.iterate_primez(int(math.sqrt(n)) + 2) if p >= 23)

    yield from primez.iterate_primez(min(windown, n))
    bottom = windown
    while bottom <= n:
        v = v0.copy()
        for p in vp:
            v[p - bottom % p::p] = False

        for i in range(min(windown, n - bottom + 1)):
            if v[i]:
                yield bottom + i
        bottom += windown


def go(n=10**10):
    bad = 0
    k = 0
    for p in gen_primez_stage(n):
        if p * 1000 // n > k:
            k = p * 1000 // n
            print(k)
        bad += min(n // p, p)
    return n - bad
