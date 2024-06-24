#!/usr/bin/env python3


from primez import isprime
from primez import iterate_primez as ip
from itertools import islice, count

v = {}
n = 11


for i in count(2):
    s = 0
    for j in ip(i):  # ip(7) returns an iterator to 2,3,5 excluding 7
        s += v.get((i - j, min(i - j, j)), 0)
        v[(i, j)] = s
    if isprime(i):
        s += 1
    v[(i, i)] = s
    if s > 5000:
        print(i)
        break
