#!/usr/bin/env python3

import itertools

f = {"0": 1}


def make_f():
    k = 1
    global f
    for i in range(1, 10):
        k = k * i
        f[str(i)] = k


make_f()


def foo(n):
    return sum((f[c] for c in str(n)))


data = {}


def process(n):
    global data

    v = []
    s = set()
    while n not in data and n not in s:
        v.append(n)
        s.add(n)
        n = foo(n)

    if n in data:
        for i in range(len(v)):
            data[v[i]] = data[n] + len(v) - i
        return
    assert(n in s)

    first = v.index(n)
    cycle_len = len(v) - first
    for i in range(first):
        data[v[i]] = cycle_len + first - i
    for i in range(first, len(v)):
        data[v[i]] = cycle_len


def go(n):
    global data
    data = {}
    for i in range(2, n + 1):
        if i not in data:
            process(i)
    return [x for x in range(2, n + 1) if data[x] == 60]
