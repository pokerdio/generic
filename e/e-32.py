#!/usr/bin/env python3

# https://projecteuler.net/problem=32
#


d = {}

for a in range(1, 10000):
    b = 1
    while True:
        c = a * b
        abc = str(a) + str(b) + str(c)
        if (len(abc) > 9):
            break

        if len(set(abc) - set("0")) == 9:
            d[c] = (a, b)

        b += 1

print(sum(list(d.keys())))
