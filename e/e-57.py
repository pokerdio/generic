#!/usr/bin/env python3

#

from itertools import islice


def step(a, b):
    return a + 2 * b, a + b


def stepper(a, b):
    while True:
        a, b = step(a, b)
        yield a, b


print(sum(len(str(a)) > len(str(b)) for a, b in islice(stepper(1, 1), 999)))
