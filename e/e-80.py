#!/usr/bin/env python3

# root
import math
from itertools import islice


def is_square(n):
    root = int(math.sqrt(n))

    return n == root * root


def root_digits(n):
    assert(n > 0)
    ten = 1
    while ten * ten <= n:
        ten = ten * 10
    ten = ten // 10

    root = 0
    while True:
        k = 0
        for i in range(10):
            new_root = root + ten * i
            if new_root * new_root <= n:
                k = i
        yield k
        root = (root + ten * k) * 10
        n = n * 100


def foo(n):
    if is_square(n):
        return 0
    else:
        return sum(list(islice(root_digits(n), 100)))


def go():
    return sum(foo(x) for x in range(1, 101))
