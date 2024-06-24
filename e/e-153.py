

# n / (a + bi) = (na - nbi) / (a * a + b * b)

from primez import decompose_iterate as dec
from math import gcd


def go(n):
    sr, sg = 0, 0
    for a in range(1, n + 1):
        sr += a * (n // a)
    for a in range(1, int(sqrt(n)) + 1):
        # rational integer divisors
        if a < 10 or a % 100 == 0:
            print("doing", a)
        for b in range(1, int(sqrt(n)) + 1):
            # a+-bi gaussians
            if gcd(a, b) == 1:
                ab2 = (a * a + b * b)
                for k in range(1, n // ab2 + 1):
                    q = ab2 * k
                    nq = n // q
                    sg += 2 * nq * a * k
    return sr + sg, sr, sg
