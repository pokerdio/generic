#!/usr/bin/env python3

# https://projecteuler.net/problem=66
# this is actually called the pell equation
# http://www.math.leidenuniv.nl/~psh/ANTproc/01lenstra.pdf


from itertools import count


def square(x):
    return x == int(sqrt(x)) ** 2


# def step(v, y, xbest):
#     y2 = y * y
#     changed = False
#     for i in range(len(v)):
#         D = v[i]
#         if square(D * y2 + 1):
#             x = int(sqrt(D * y2 + 1))
#             if xbest[0][1] < x:
#                 xbest[0] = (D, x)
#             # it's best because v is growing monotonously
#             v[i] = -1
#             changed = True
#     return changed


# def go():
#     v = [x for x in range(2, 1001) if not square(x)]
#     xbest = [(0, 0)]
#     for y in range(1, 100000000):
#         oldbest = xbest[0]
#         if step(v, y, xbest):
#             v = [i for i in v if i > 0]
#             print(xbest[0], "y", y, "unsolved", len(v))


# def possible_x_moduloD(D):
#     return [i for i in range(D) if i * i % D == 1]


# def solve(D):
#     pv = possible_x_moduloD(D)
#     if square(D):
#         return
#     for c in count(0, 1):
#         for p in pv:
#             x = c * D + p
#             x2 = x * x
#             y = int(sqrt((x2 - 1) // D))

#             if (y > 0) and (y * y * D + 1 == x2):
#                 return x, y


import math
import itertools
from fractions import Fraction as Fr


def cf(m):
    while m > 0:
        floor = math.floor(m)
        yield floor
        m = m - floor
        print(m)
        if m > 0:
            m = 1 / m


(1766319049, 226153980)


def cf_to_f(cf):
    m = fr(cf[-1])
    for x in cf[-2::-1]:
        print(m)
        m = fr(x) + 1 / m

    return m


def topn(it, n):
    return list(itertools.islice(it, n))


class RootApprox:
    def __init__(self, n):
        self.root = n
        self.min = Fr(0)
        self.max = Fr(n + 1)
        self.step = Fr(n + 1)

    def Step(self):
        self.step /= 8
        newmin = self.min
        for i in range(8):
            newmax = newmin + self.step
            if newmax ** 2 > self.root:
                self.min, self.max = newmin, newmax
                return self.min
            newmin = newmax
        assert(0)

    def MinMax(self):
        return self.min, self.max


def gen_root(n):
    ap = RootApprox(n)
    a, b = Fr(0), Fr(1)
    while True:
        min, max = ap.MinMax()
        min = a + min * b
        max = a + max * b

        m = int(min)
        if m != int(max):
            ap.Step()
            continue

        yield m

        a -= m

        denom = a * a - b * b * n

        a, b = a / denom, -b / denom


def gen_root_rep(n):
    d = {}
    k = 0

    ap = RootApprox(n)
    a, b = Fr(0), Fr(1)

    ap = RootApprox(n)
    while True:
        min, max = ap.MinMax()
        min = a + min * b
        max = a + max * b

        m = int(min)
        if m != int(max):
            ap.Step()
            continue

        a -= m
        denom = a * a - b * b * n
        a, b = a / denom, -b / denom

        if (a, b, m) in d:
            #            print("repeating index", d[(a, b, m)])
            assert(d[(a, b, m)] == 1)  # dunno why but they all do be like that
            return
        yield m

        d[(a, b, m)] = k
        k += 1


def exp_to_fr(exp):
    s = Fr(exp[-1])
    for i in exp[-2::-1]:
        s = Fr(i) + 1 / s
    return s


def go(n):
    nosquares = list(x for x in range(2, n + 1) if not square(x))
    print(len([666 for i in nosquares if len(list(gen_root_rep(i))) % 2 == 0]))
