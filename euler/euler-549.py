import primez
import math
import numpy as np


def fact_need(p, k):
    """returns smallest factorial divisible by p**k, where p is prime"""

    for i in range(1, k + 1):
        k -= 1
        j = i
        while j % p == 0:
            j //= p
            k -= 1
        if k <= 0:
            return i * p


def build_prime_demand(n):
    n2 = int(math.sqrt(n)) + 1
    for p in primez.iterate_primez(n2):
        k = 1
        pk = p
        while pk <= n:
            yield pk, fact_need(p, k)
            k += 1
            pk *= p


def go(n):
    p = sorted(build_prime_demand(n), key=lambda x: x[1])

    n2 = int(math.sqrt(n)) + 1
    print("one")
    x = np.arange(n + 1)
    print("two")
    k = 0
    for pk, f in p:
        x[pk::pk] = f
    print("three")
    for i in range(n2, n + 1):
        if i % 1000000 == 0:
            print(i)
        if x[i] == i:
            x[i::i] = i
    return sum(x) - 1


# 476001479068717
