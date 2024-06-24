from math import sqrt
from itertools import islice
import sys

sys.setrecursionlimit(15000)


def sieve_primez(n):
    sieve = [0] * (n + 1)
    for i in range(2, n):
        if not sieve[i]:
            for j in range(i * 2, n + 1, i):
                if not sieve[j]:
                    sieve[j] = i
    return [x for x in range(2, n + 1) if not sieve[x]]


pv = sieve_primez(int(10**6))


def foo2(n=80):
    sieve = [0] * n
    d = {}
    for i in range(2, n):
        if not sieve[i]:
            for j in range(i * 2, n, i):
                if not sieve[j]:
                    sieve[j] = i
        else:
            a = 0
            p = sieve[i]
            i2 = i
            while i2 % p == 0:
                i2 //= p
                a += 1

            if a > 1:
                val = (a - 1) / (p - 1)
                d[p] = d.get(p, 0) + val
    return {p: x/n for p, x in d.items()}
    # return sum(d.values()) / n


def _phi(n, p, pv=pv):
    ret = 0

    for i in range(1, n + 1):
        for q in pv[:p]:
            if i % q == 0:
                break
        else:
            ret += 1
    return ret


def prime_count(n, pv=pv):
    if n == 2:
        return 1
    start = 0
    end = len(pv) - 1
    while end - start > 1:
        mid = (start + end) // 2
        if pv[mid] > n:
            end = mid
        else:
            start = mid
    return start + 1


def phi(n, p, pv=pv, buf={}):
    if p == 1:
        return (n + 1) // 2

    if n == 1:
        return 1

    cur_prime = pv[p - 1]
    np = (n, p)

    if np in buf:
        return buf[np]

    if n < 10:
        ret = _phi(n, min(p, 4))
    elif cur_prime * cur_prime >= n and n < pv[-1]:
        return prime_count(n, pv) - p + 1
    else:
        ret = phi(n, p - 1, pv) - phi(n // cur_prime, p - 1, pv)

    if n < 500000:
        buf[np] = ret
    return ret


def go(m, pv=pv):
    ret = 0.0
    for i, p in enumerate(pv):
        x = p*p
        a = 1

        geometric_sum = 1.0 / (p - 1)

        while x <= m:
            k = m // x
            count = phi(k, i + 1, pv)
            ret += count * a * geometric_sum
            x = x * p
            a += 1

    return ret / m


def go2(n=100, pv=pv):
    ret = 0.0
    freq = 1.0
    for p in pv[0:n]:
        v = freq/(p*(p-1)*(p-1))
        freq = freq * (1.0 - 1.0/p)
        ret += v
    return ret


print(go2(10000))
