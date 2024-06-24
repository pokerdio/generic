import primez
import numpy as np


def itp(p1, p2):
    for p in primez.iterate_primez(p2):
        if p >= p1:
            yield p


def analyze_prime(p):
    starter_pack = []

    x = 1
    delta = 6 % p
    k = 1
    steps = 0
    while True:
        steps += 1
        x, delta, dk = jump4(x, delta, p)
        x %= p
        delta %= p
        k += dk

        if x == 0:
            starter_pack.append(k)
        if k >= p:
            print(p, steps, k)
            return starter_pack


def foo(n):
    v = np.array([1] * (n + 1))

    for p in itp(3, n * 3 // 2):
        starter_pack = analyze_prime(p)
        print(p, "starter pack", starter_pack)
        for start in starter_pack:
            v[start::p] = 0
    ret = 0

    for p in itp(3, n * 3 // 2):
        k = int(sqrt((p + 1) // 2))
        if k * k * 2 - 1 == p:
            v[k] = 1
    print("end a")
    for i in range(2, n + 1):
        if v[i]:
            #            print(i, 2 * i * i - 1, primez.isprime(2 * i * i - 1))
            ret += 1
    return ret


def test(n=100):
    for p in primez.iterate_primez(n):
        k = 1
        delta = 6 % p
        v = {k}
        for _ in range(1000):
            k = (k + delta) % p
            delta = (delta + 4) % p
            v.add(k)
        print(p // 2 + 1, len(v))


def jump4(x, delta, p):

    # k = 3

    # delta + delta + 4 + delta + 8

    # x + k * delta + k * (k-1) * 2

    # x + k * (delta - 2) + 2 * k * k >= p

    k = int(sqrt(p // 2))
    while x + k * (delta - 2) + 2 * k * k > p:
        k -= 1
    while x + k * (delta - 2) + 2 * k * k < p:
        k += 1

    return x + k * (delta - 2) + 2 * k * k, delta + (k * 4), k


def jump(x, delta, p):
    k = 0
    while x < p:
        #        print(x, delta)
        x += delta
        delta += 4
        k += 1

    return x, delta, k


def testjump(n=1000):
    for p in itp(3, 1000):
        assert(jump(1, 6, p) == jump4(1, 6, p))
