import primez
import numpy as np

primez.init_primes(40000000)


def totient(n):
    v = np.array(range(n))
    for i in primez.iterate_primez(n):
        v[i:n:i] //= i
        v[i:n:i] *= i - 1

    v[0] = 0
    v[1] = 1
    return v


def go(n, chain):
    v = totient(n + 1)
    for i in range(2, n + 1):
        v[i] = v[v[i]] + 1

    ret = []
    for p in primez.iterate_primez(n + 1):
        if v[p] == chain:
            ret.append(p)
    return ret
