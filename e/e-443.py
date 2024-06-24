import primez
from math import gcd


def step(a, b):
    cd = gcd(a, b)
    if cd > 1:
        return a + 1, b + cd

    jump = b - a
    delta = primez.decompose(b - a)
    for p in delta.keys():
        jump = min(jump, p - (a % p))
    return a + jump, b + jump


def go(n):
    a, b = 5, 13

    k = 0
    while True:
        aa, bb = step(a, b)

        if bb - b > k:
            k = bb - b
            print(k)
        if a == n:
            return bb
        if a > n:
            return b + (n - a) + 1
        a, b = aa, bb
