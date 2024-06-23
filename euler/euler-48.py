#!/usr/bin/env python3

# https://projecteuler.net/problem=27
#


def pow(a, b, mod):
    ret = 1
    while True:
        if b == 1:
            return (ret * a) % mod

        elif b % 2 == 0:
            a = (a * a) % mod
            b //= 2

        else:
            ret = (ret * a) % mod
            b -= 1


v = 10 ** 10

print(sum(pow(x, x, v) for x in range(1, 1001)) % v)
