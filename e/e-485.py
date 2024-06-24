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


def ndiv(n, v=sieve(10**8 + 3)):
    g = {}
    update_ndiv(g, n, v)
    ret = 1
    for i in g.values():
        ret *= i + 1
    return ret


class MaxWindow:
    def __init__(self, k):
        self.k = k  # window size
        self.dq = deque()
        self.i = 0  # index of incoming element

    def __repr__(self):
        return str(self.dq)

    def add(self, value):
        dq = self.dq
        if dq and self.i - dq[0][1] == self.k:
            dq.popleft()
        while dq and value >= dq[-1][0]:
            dq.pop()
        dq.append((value, self.i))
        self.i += 1

    def max(self):
        return self.dq[0][0]


def go(u, k):
    m = MaxWindow(k)
    for i in range(1, k):
        m.add(ndiv(i))
    ret = 0
    for i in range(k, u + 1):
        m.add(ndiv(i))
        ret += m.max()
    return ret


print(go(10**8, 10**5))
