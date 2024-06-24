from collections import Counter

import operator as op
from functools import reduce


def _ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom


def pascal_step(v):
    return [(a + b) % 1000000007 for a, b in zip([0, *v], v + [0])]


def pascal_precalc(n):
    ret = [[1]]
    for i in range(1, n):
        ret.append(pascal_step(ret[-1]))
    return ret


def ncr(n, r, pascal=pascal_precalc(2050)):
    return pascal[n][r]


def pow9mod_gen(n):
    ret = [1]
    for i in range(n):
        ret.append(ret[-1] * 9 % 1000000007)
    return ret


def pow9mod(n, precalc=pow9mod_gen(2050)):
    return precalc[n]


def isdom(n):
    s = str(n)
    ndigitz = len(s)
    c = Counter(s)
    if max(c.values()) > ndigitz // 2:
        return True
    return False


def is_nonzero_dom(n):
    s = str(n)
    ndigitz = len(s)
    c = Counter(s)
    if max(c, key=lambda x: c[x]) == "0":
        return False

    if max(c.values()) > ndigitz // 2:
        return True
    return False


def gen(n, testf):
    return [i for i in range(1, n + 1) if testf(i)]


def _count_dom(n):
    return len(gen(10 ** n - 1, isdom))


def _count_nonzero_dom(n):
    return len(gen(10**n - 1, is_nonzero_dom))


def _count_zero_dom(n):
    return _count_dom(n) - _count_nonzero_dom(n)


def count_nonzero_dom(ndigit):
    ret = 0
    for big in range(1, ndigit + 1):
        smol = min(big - 1, ndigit - big)
        delta = ncr(big + smol, big) * pow9mod(smol + 1)
#        print(big, smol, delta)
        ret = (delta + ret) % 1000000007
    return ret


def count_zero_dom(ndigit):
    ret = 0
    for zero in range(2, ndigit):
        for poz in range(1, min(zero, ndigit - zero + 1)):
            delta = ncr(zero + poz - 1, zero) * pow9mod(poz)
            ret = (ret + delta) % 1000000007

    return ret


def count_dom(ndigit):
    return (count_nonzero_dom(ndigit) + count_zero_dom(ndigit)) % 1000000007
