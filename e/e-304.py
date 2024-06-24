import primez
import numpy as np
import matrix
from builtins import sum


def p_interval(n, m):
    """works up to ~100 trillions; does not save the data"""

    sieve = np.ones(m - n + 1, dtype=np.bool)

    for p in primez.iterate_primez(int(sqrt(m)) + 1):
        p0 = n % p
        if p0 > 0:
            p0 = p - p0
        sieve[p0::p] = False
    return [n + x for x in range(m - n) if sieve[x]]


def fibo(n, mod=1234567891011):
    if n < 2:
        return n
    a = matrix.pow([[0, 1], [1, 1]], n - 1, mod)
    return sum(a[0]) % mod


def go():
    v = p_interval(10**14, 10**14 + 4000000)
    assert(len(v) > 100000)

    return sum(fibo(x) for x in v[:100000]) % 1234567891011
