from copy import deepcopy
from builtins import sum
import random
from collections import deque


def sieve(n):
    v = list(range(n + 2))

    for i in range(2, n // 2 + 1):
        if i == v[i]:
            for j in range(i * 2, n + 1, i):
                v[j] = i
    return v


def update_ndiv(g, n, v):
    while n > 1:
        div = v[n]
        while n % div == 0:
            g[div] = g.get(div, 0) + 1
            n //= div


def dT(n, v=sieve(60000005)):
    """n * (n + 1) / 2 div count"""
    g = {}
    update_ndiv(g, n, v)
    update_ndiv(g, n + 1, v)
    g[2] -= 1

    ret = 1
    for i in g.values():
        ret *= i + 1
    return ret


def go(n):
    v = [dT(x) for x in range(1, n + 1)]
    vals = sorted(set(v))
    nvals = len(vals)
    gvals = {x: vals.index(x) for x in vals}
    for x in range(len(v)):
        v[x] = gvals[v[x]]

    dp = [[0] * nvals for _ in range(3)]

    print(nvals)
    for i in range(n):
        if i % 10000 == 9999:
            print("***", i, "/", n)
        dp2 = deepcopy(dp)
        for a in range(2):
            for j in range(v[i] + 1, nvals):
                dp2[a + 1][v[i]] = (dp[a][j] + dp2[a + 1][v[i]])
        dp2[0][v[i]] += 1

        # for a in range(3):
        #     for j in range(nvals):
        #         dp2[a][j] %= 1000000000000000000
        dp = dp2
        # print(i, v[i])
        # print(dp)
    return sum(dp[2]) % 1000000000000000000


class Fenwick():
    def __init__(self, n):
        self.n = n
        self.v = [0] * (n + 1)
        self.val = [0] * (n + 1)
        self.two = 1
        self.sum = 0
        while self.two < n:
            self.two *= 2
        if self.two > n:
            self.two //= 2

    def __repr__(self):
        return str(self.val[1:])

    def add(self, value, place=None):
        if not place:
            place = value
            value = 1

        assert(place > 0)  # sorry, just 1..n locations allowed
        self.sum += value
        self.val[place] += value
        two = 1
        while place > 0:
            self.v[place] += value
            while two & place == 0:
                two *= 2
            place ^= two

    def sum_above(self, place):
        """inclusive"""
        if place > self.n:
            return 0
        two = 1
        ret = 0
        while two <= self.two and place <= self.n:
            if two & place:
                ret += self.v[place]
                place += two
            two *= 2
        return ret

    def sum_below(self, place):
        """inclusive"""
        if place < 1:
            return 0
        return self.sum - self.sum_above(place) + self.val[place]

    def sum_above_test(self, place):
        """sum_above with a slooow verification of correctness"""
        ret = self.sum_above(place)
        assert ret == sum(self.val[x] for x in range(place, self.n + 1))
        return ret


def foo(n=100):
    f = Fenwick(n)
    for i in range(1, n * n):
        f.add(1, random.randint(1, n + 1))
    for i in range(1, n + 1):
        f.sum_above_test(i)


def go2(n):
    """go with fenwick tree optimization"""
    v = [dT(x) for x in range(1, n + 1)]
    vals = sorted(set(v))
    nvals = len(vals)
    gvals = {x: vals.index(x) + 1 for x in vals} """1 based values"""
    for x in range(len(v)):
        v[x] = gvals[v[x]]

    dp = [[0] * nvals for _ in range(3)]

    f1 = Fenwick(n)
    f2 = Fenwick(n)
    ret = [0] * (n + 2)
    for i in range(n):
        if i % 10000 == 9999:
            print("***", i, "/", n)

        vi = v[i]

        ret[vi] += f2.sum_above(vi + 1)
        f2.add(f1.sum_above(vi + 1), vi)
        f1.add(vi)
    return sum(ret) % 1000000000000000000


print(go2(6*10**7))
