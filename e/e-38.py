#!/usr/bin/env python3

#


def concat_product(n, k):
    return "".join((str(n * x) for x in range(1, k + 1)))


def test(n, k, digitz=set("123456789")):
    s = concat_product(n, k)
    return len(s) == 9 and set(s) == digitz


import math


def go():
    for n in range(1, 10000):
        for k in range(1, 10):
            if test(n, k):
                yield(int(concat_product(n, k)))


print(max(go()))
