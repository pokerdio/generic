from math import sqrt
import itertools as it


def primez(n):
    v = [1] * (n + 1)
    for i in range(2, int(sqrt(n)) + 1):
        if v[i]:
            for j in range(i * 2, n + 1, i):
                v[j] = 0
    return [x for x in range(2, n + 1) if v[x]]


def decompose(n):
    vp = primez(n)
    ret = []
    for p in vp:
        x = [1]
        while n % p == 0:
            n //= p
            x.append(p * x[-1])
        if len(x) > 1:
            ret.append(x)
        if n == 1:
            break
    return ret


def divz(n):
    for c in it.product(*decompose(n)):
        ret = 1
        for x in c:
            ret *= x
        yield ret


def go(v):
    n = len(v)
    for d in divz(n):
        if n // d >= 3:
            ok = [1] * d
            for i, mood in enumerate(v):
                ok[i % d] &= mood

            if 1 in ok:
                return True


_ = int(input())
v = [int(x) for x in input().split()]
print(go(v) and "YES" or "NO")
