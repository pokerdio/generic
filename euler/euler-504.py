import math


def gcd(a, b):
    b, a = min(a, b), max(a, b)
    while b > 0:
        a, b = b, a % b
        b, a = min(a, b), max(a, b)
    return a


def intri(x, y, g={}):
    xy = (x, y)
    if xy in g:
        return g[xy]
    else:
        ret = 0
        if min(x, y) > 1:
            ret = ((x - 1) * (y - 1) - gcd(x, y) + 1) // 2
        g[xy] = ret
        return ret


def inside(a, b, c, d):
    return intri(a, b) + intri(b, c) + intri(c, d) + intri(a, d) + a + b + c + d - 3


def go(n):
    ret = 0
    s = set(x * x for x in range(1, 2 * n))
    for a in range(1, n + 1):
        print(a)
        for b in range(1, n + 1):
            for c in range(1, n + 1):
                for d in range(1, n + 1):
                    k = inside(a, b, c, d)
                    if k in s:
                        ret += 1
    return ret
