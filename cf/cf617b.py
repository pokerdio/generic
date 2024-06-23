from functools import reduce
n = int(input())
v = [int(c) for c in input().split()]
nuts = [x for x in range(len(v)) if v[x]]

if nuts:
    delta = [y - x for x, y in zip(nuts[:-1], nuts[1:])]

    print(reduce(lambda a, b: a * b, delta, 1))
else:
    print(0)
