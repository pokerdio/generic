#!/usr/bin/env python3

# https://projecteuler.net/problem=483
# repeated permutations


# the solution doesnt' work for large numbers sadly

from math import gcd


def lcm(a, b):
    return a * b // (gcd(a, b))


def memoize(f):
    memo = {}

    def helper(n):
        if n not in memo:
            memo[n] = f(n)
        return memo[n]

    return helper


@memoize
def t(n):
    if n <= 0:
        return 0
    if n == 1:
        return 10
    if n == 2:
        return 101
    return t(n - 1) * 10 + t(n - 2)


def test3():
    s = 0
    for c in range(1, 4):
        for a in range(1, 4):
            for b in range(1, 4):
                s += math.gcd(t(c ** a) % 987898789, t(c ** b) % 987898789)
    return s % 987898789


class v2:
    def __init__(self, v0, v1, mod=None):
        if mod:
            self.v0 = v0 % mod
            self.v1 = v1 % mod
        else:
            self.v0 = v0
            self.v1 = v1

        self.mod = mod

    def __repr__(self):
        return "[%d, %d]" % (self.v0, self.v1)


class m22:
    def __init__(self, a00, a01, a10, a11, mod=None):
        if mod:
            self.a00 = a00 % mod
            self.a01 = a01 % mod
            self.a10 = a10 % mod
            self.a11 = a11 % mod
        else:
            self.a00 = a00
            self.a01 = a01
            self.a10 = a10
            self.a11 = a11

        self.mod = mod

    def __repr__(self):
        return "[%6d %6d]\n[%6d %6d]\n" % (self.a00, self.a01, self.a10, self.a11)

    def __mul__(self, n):
        if type(n) == int:
            return m22(self.a00 * n, self.a01 * n, self.a10 * n, self.a11 * n, self.mod)
        if type(n) == m22:
            return m22(self.a00 * n.a00 + self.a01 * n.a10,
                       self.a00 * n.a01 + self.a01 * n.a11,
                       self.a10 * n.a00 + self.a11 * n.a10,
                       self.a10 * n.a01 + self.a11 * n.a11, self.mod)

        if type(n) == v2:
            return v2(self.a00 * n.v0 + self.a01 * n.v1,
                      self.a10 * n.v0 + self.a11 * n.v1, self.mod)

        assert(False)

    def __pow__(self, n):
        assert(type(n) == int and n >= 0)

        ret = m22(1, 0, 0, 1, self.mod)
        powm = self
        prod = []
        while n > 0:
            if n % 2 != 0:
                prod.append(powm)

            powm = (powm * powm)
            n //= 2
        for m in prod:
            ret = ret * m
        return ret


recm = m22(10, 1, 1, 0)
v_ini = v2(1, 0)


def T(n):
    return ((recm ** n) * v_ini).v0


def test():
    assert(solve(2) == 10444)
    assert(solve(4) == 670616280)
    assert(solve(3) == (1292115238446807016106539989 % 987898789))


def solve(count=2000, mod=987898789):
    global recm
    global v_ini
#    recm.mod = mod
#    v_ini.mod = mod

    thesum = 10 * count * count
    for c in range(2, count + 1):
        print("progress", c)
        Tlist = {}
        m = recm
        for a in range(1, count + 1):
            m = m ** c
            Tlist[a] = (m * v_ini).v0
#            print("T(%d^%d)=%d" % (c, a, Tlist[a]))

#        print(Tlist)
        for a in range(1, count + 1):
            for b in range(1, count + 1):
                thesum += gcd(Tlist[a], Tlist[b])
                thesum %= mod

    return thesum

# solution => 2000 => 970746056


for i in range(2, int(5 + math.sqrt(987898789))):
    if 987898789 % i == 0:
        print(i)
