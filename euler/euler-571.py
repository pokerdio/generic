from functools import reduce
from itertools import permutations as perms


def perm(n):
    return reduce(lambda x, y: x * y, list(range(1, n + 1)))


def ton(p, b):
    ret = 0
    for i in range(len(p)):
        ret = ret * b + p[i]
    return ret


def ntopset(n, b):
    ret = set()
    while n:
        ret.add(n % b)
        n //= b
    return ret


def pandigital(n, b1):
    return len(ntopset(n, b1)) == b1


ret = []


def test(b):
    global ret
    ret = []
    lastfirst = 1
    for p in perms(list(range(1, b)) + [0]):
        if p[0] != lastfirst:
            if p[0] == 0:
                break
            lastfirst = p[0]
            print("doing ", lastfirst)
            if len(ret) > 12:
                return

        n = ton(p, b)
        for b1 in range(b - 1, 2, -1):
            if not pandigital(n, b1):
                break
        else:
            print("success", n)
            ret.append(n)


test(12)
print(ret)


def test(b):
    global ret
    ret = []
    lastfirst = 1
    for p in perms(list(range(1, b)) + [0]):
        if p[0] != lastfirst:
            if p[0] == 0:
                break
            lastfirst = p[0]
            print("doing ", lastfirst)
            if len(ret) > 12:
                return

        n = ton(p, b)
        for b1 in range(b - 1, 2, -1):
            if not pandigital(n, b1):
                break
        else:
            print("success", n)
            ret.append(n)
