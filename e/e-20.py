#!/usr/bin/env python3


import random
import math


def str_mul_digit(s1, digit):
    s = ""
    assert(digit < 10)
    if digit == 0:
        return "0"
    over = 0
    for i in s1[-1::-1]:
        k = int(i) * digit + over
        s = str(k % 10) + s
        over = k // 10
    if over > 0:
        s = str(over) + s
    return s


def str_mul(s1, s2):
    s = "0"
    z = ""
    for i in reversed(s2):
        s3 = str_mul_digit(s1, int(i)) + z
        s = str_add(s, s3)
        z = z + "0"
    return s


def str_add(s1, s2):
    maxlen = max(len(s1), len(s2))
    s1 = "0" * (maxlen - len(s1)) + s1
    s2 = "0" * (maxlen - len(s2)) + s2
    s = ""
    over = 0
    for i, j in reversed(list(zip(s1, s2))):
        k = int(i) + int(j) + over
        over = k // 10
        s = str(k % 10) + s

    if over:
        s = "1" + s
    return s


def str_fact(n):
    if n <= 1:
        return "1"
    return str_mul(str(n), str_fact(n - 1))


def test_add(n=500, rng=10**10):
    for i in range(n):
        a, b = random.randrange(rng), random.randrange(rng)
        assert(int(str_add(str(a), str(b))) == a + b)


def test_mul(n=500, rng=10**10):
    for i in range(n):
        a, b = random.randrange(rng), random.randrange(rng)
        assert(int(str_mul(str(a), str(b))) == a * b)


def test_mul_digit(n=500, rng=10**10):
    for i in range(n):
        a, k = random.randrange(rng), random.randrange(10)
        assert(int(str_mul_digit(str(a), k)) == a * k)


test_add(5000)
test_mul_digit(5000)
test_mul(5000)
assert(str_fact(50) == str(math.factorial(50)))


print (sum(int(x) for x in str_fact(100)))
