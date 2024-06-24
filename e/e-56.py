#!/usr/bin/env python3

#


def digital_sum(n):
    return sum(int(x) for x in str(n))


def solve():
    return max(((a, b, digital_sum(a ** b)) for a in range(1, 101)
                for b in range(1, 101)), key=lambda x: x[2])
