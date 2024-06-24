#!/usr/bin/env python3

# https://projecteuler.net/problem=483
# repeated permutations


# the solution doesnt' work for large numbers sadly

from math import gcd


def lcm(a, b):
    return a * b // (gcd(a, b))


def reset_g_data():
    global g_data
    g_data = {1: {1: 1}, 0: {1: 1}}


reset_g_data()


def go(n):
    if n in g_data:
        return g_data[n]

    d = go(n - 1).copy()
    k = 1
    for i in range(2, n + 1):
        k *= (n - i + 1)

        d2 = go(n - i)
        for cycle, combs in d2.items():
            cycle2 = lcm(cycle, i)
            d[cycle2] = k * combs + d.get(cycle2, 0)
    g_data[n] = d
    return d


def g(n):
    d = go(n)

    total_combs = 0
    s = 0
    for cycle, combs in d.items():
        s += combs * cycle ** 2
        total_combs += combs

    print("%.10E" % (s / total_combs))


from random import randint
from math import gcd
from functools import reduce


def lcm_lst(v):
    return reduce(lambda x, y: x * y // gcd(x, y), v)


def cycle_random(n):
    v = []
    while n > 0:
        k = randint(1, n)
        v.append(k)
        n -= k
    return lcm_lst(v)


def estimate(n):
    total = 0
    total_count = 0
    while True:
        for i in range(100000):
            k = cycle_random(n)
            total_count += 1
            total += k * k
        print("%.11e" % (total / total_count))


def go(n):
    data = [{1: 1.0}]

    for i in range(1, n + 1):
        d = {}

        i_1 = 1 / i
        for j in range(1, i + 1):
            for cycle, freq in data[i - j].items():
                new_cycle = lcm(cycle, j)
                d[new_cycle] = d.get(new_cycle, 0.0) + freq * i_1

        data.append(d)
        print("count for %d is %d" % (i, len(d)))

    return data


def g(n):
    data = go(n)[n]
    s = 0.0
    for cycle, freq in data.items():
        s += freq

    s = 1.0 / s
    for cycle, freq in data.items():
        data[cycle] *= s
    s = 0.0
    for cycle, freq in data.items():
        s = s + cycle * cycle * freq
    print("%.9e" % s)
    print("%.12e" % s)
