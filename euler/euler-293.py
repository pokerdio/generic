import heapq
from math import sqrt


def listp(n):
    sieve = list(range(n + 2))
    ret = []
    for i in range(2, n + 1):
        if sieve[i] == i:
            ret.append(i)
            for j in range(i, n + 1, i):
                sieve[j] = i
    return ret


def chop_iterate(n0, n, buckitz):
    n -= n0
    for i in range(buckitz - 1):
        yield n0 + (n + 1) * i // buckitz, n0 + (n + 1) * (i + 1) // buckitz
    yield n0 + (n + 1) * (buckitz - 1) // buckitz, n0 + n + 1


def listp_buckitz(n):
    n2 = int(sqrt(n) + 1)
    vp = listp(n2)

    ret = vp.copy()
    for base, top in chop_iterate(n2, n, 1000):
        print("doing", base, top, len(ret))
        nsieve = (top - base)
        sieve = [0] * nsieve
        for p in vp:
            for i in range((p - (base % p)) % p, nsieve, p):
                sieve[i] = 1
        ret.extend(x + base for x in range(nsieve) if not sieve[x])
    return ret


#primez = listp_buckitz(10**9 + 2500)


def gen_admin(n):
    last = [1]
    ret = []
    pv = listp(1000)

    for p in pv:
        new = []
        for i in last:
            while i * p <= n:
                i *= p
                new.append(i)
        if not new:
            break
        ret.extend(new)
        last = new

    return sorted(ret)


def go(n):
    global primez
    assert(primez[-1] > n)

    primez_idx = 0

    s = set()
    for a in gen_admin(n):
        while primez[primez_idx] <= a + 1:
            primez_idx += 1
        s.add(primez[primez_idx] - a)
    return sum(list(s))
