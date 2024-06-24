#import numpy as np
from mpmath import *
from math import log


class Buckitz:
    def __init__(self):
        self.b = [0.0]
        self.blimit = [10.0]

    def Add(self, x):
        assert(x >= 0)
        if x < 10:
            v = 0
        else:
            v = int(log(x, 10))

        while len(self.b) <= v + 1:
            self.b.append(0.0)
            self.blimit.append(10 * self.blimit[-1])
        self.b[v] += x
        while self.b[v] >= self.blimit[v]:
            if v == len(self.b) - 1:
                self.b.append(self.b[-1])
                self.b[v] = 0.0
                self.blimit.append(10 * self.blimit[-1])
                v += 1
            else:
                self.b[v + 1] += self.b[v]
                self.b[v] = 0.0
                v += 1

    def Value(self):
        return sum(self.b)

    def __repr__(self):
        return str(self.b)


def foo(k, x):
    #    f = np.longfloat
    f = float
    one = f(1)
    q = one - (one / 2 ** x)
    q2 = q * q
    q3 = q * q * q
    n = 1
    qpow = q
    count = 0

    b = Buckitz()
    while True:
        qpow = q ** n
        b.Add((n ** k) * qpow / (one - qpow))

        n += 1
        count += 1
        if count % 1000000 == 0:
            print(count // 1000000, "%.12E" % b.Value())


#foo(15, 25)


# borrowed


mp.dps = 50


def f(k, b):
    t = int(quad(lambda x: x**k*(2**b - 1)**x/(2**(b*x) - (2**b - 1)**x), [1, inf]))
    return "{:.12E}".format(t)


print(f(15, 25))
