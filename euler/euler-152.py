from primez import iterate_primez as ip
from itertools import combinations as combs
from itertools import chain

from fractions import Fraction as F

import primez
import sys
import numpy as np

sys.setrecursionlimit(1500)

r2 = {i: F(1, i * i) for i in range(2, 81)}


def goprime(p, n, forbidden=set(), r2=r2):
    s = set(range(p, n + 1, p)) - set(forbidden)
    for i in range(len(s) + 1):
        for combo in combs(s, i):
            frsum = 0
            for c in combo:
                frsum += r2[c]
            if not frsum or (frsum.denominator % p != 0):
                yield combo, s - set(combo)


def foo(*args):
    return sum(F(1, x * x) for x in args)


def bar():
    forbid = {5: [55, 65], 7: [77]}
    for p in p80(5):
        print(p, len(list(goprime(p, 80, forbid.get(p, [])))))


def boo():
    s = set(range(2, 81))
    for p in p80(5):
        s -= set(range(p, 81, p))
    return s


def p80(minprime):
    for p in primez.iterate_primez(80):
        if p >= minprime:
            yield p


def always_forbid(minp):
    ret = set()
    for p in p80(minp):
        f = None
        for want, donotwant in goprime(p, 80):
            f = f or donotwant
            f = f & donotwant
        ret = ret | f
    return ret


always_forbidden = always_forbid(5)


def trans5():
    "groups allowed fives based on signature from threes"
    global always_forbidden
    trans = {}
    for a, f in goprime(5, 80, always_forbidden):
        sign3 = tuple(x for x in a if x % 3 == 0)
        if sign3 not in trans:
            trans[sign3] = [(a, f)]
        else:
            trans[sign3].append((a, f))
    return trans


def glorification(f, r2=r2):
    f = F(1, 2) - f

    ret = set()
    for i in [2, 4, 8]:
        if r2[i] <= f:
            f -= r2[i]
            ret.add(i)
    if f == 0:
        return ret


def main7(required, forbidden, frsum, r2=r2):
    for req, f in goprime(7, 80, forbidden):
        req = set(req)
        frsum2 = frsum
        if (f & required) or (req & forbidden):
            continue
        for x in req:
            if x % 3 != 0 and x % 5 != 0:
                frsum2 += r2[x]

        # frsum3 = 0
        # for x in req | required:
        #     frsum3 += r2[x]
        # assert(frsum3 == frsum2)

        if frsum2.denominator % 7 != 0:
            g = glorification(frsum2)
            if g:
                yield required | req | g


def main5(required, forbidden, frsum, trans=trans5(), r2=r2):
    """do not alter the optional parameter"""

    ret = 0
    for req, f in trans[tuple(x for x in required if x % 5 == 0)]:
        frsum2 = frsum
        for x in req:
            if x % 3 != 0:
                frsum2 += r2[x]
        if frsum2.denominator % 5 != 0:
            yield from main7(set(required) | set(req), forbidden | f, frsum2)


def main3(r2=r2, forbie=always_forbidden):
    ret = 0
    for c, f in goprime(3, 80, forbie):
        s = 0
        for x in c:
            s += r2[x]
        if s.denominator % 3 != 0:
            if 39 in c:
                c = (*c, 13, 52)
                s += r2[13] + r2[52]
                if s.denominator % 13 == 0:
                    continue

            yield from main5(c, f | forbie, s)


def frsum(s, r2=r2):
    ret = 0
    for x in s:
        ret += r2[x]
    return ret
