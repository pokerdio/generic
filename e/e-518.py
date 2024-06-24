import primez
import itertools as it
from math import gcd


def iterate_ab(n):
    """makes ordered pairs of divisors that are prime to each other"""

    d = primez.decompose(n)
    nd = len(d)
    for combo in it.product(*(tuple(i ** p for p in range(j + 1)) for i, j in d.items())):
        big = sum(x > 1 for x in combo)
        for k in range(2 ** big):
            a, b = 1, 1
            for i in range(nd):
                if combo[i] > 1:
                    if k % 2:
                        a *= combo[i]
                    else:
                        b *= combo[i]
                    k //= 2
            if a < b:
                yield a, b


def go(n):
    progress = 0
    for i in primez.iterate_primez(n):
        if i * 100 // n > progress:
            progress += 1
            print(progress, "%")
        for a, b in iterate_ab(i + 1):
            j, k = (i + 1) * a // b - 1, (i + 1) * b // a - 1
            if k < n and primez.isprime(j) and primez.isprime(k):
                yield j, i, k

# go(10**8) -> 100315739184392
