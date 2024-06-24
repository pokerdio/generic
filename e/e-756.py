import numpy as np
import primez


def totient_sieve(n):
    ret = np.zeros(n + 1, dtype=np.uintc)

    for i in range(2, n + 1):
        if not ret[i]:
            ret[2 * i::i] = i

    d = {}
    for i in range(n, 1, -1):
        if not ret[i]:
            ret[i] = i - 1
            continue
        d.clear()

        k = i
        while k > 1:
            j = ret[k]
            if j == 0:
                d[k] = 1
                break
            while k % j == 0:
                k //= j
                d[j] = d.get(j, 0) + 1
        k = i
        for p in d:
            k = (k // p) * (p - 1)
        ret[i] = k

    return ret


def test_totient_sieve(n):
    v = totient_sieve(n)
    for i in range(2, n + 1):
        assert primez.totient(i) == v[i], i


#v = totient_sieve(12345678)


def go(n, v=v):
    print(v[5])
