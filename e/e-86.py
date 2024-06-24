from math import gcd


def pyth_trips(n):
    basic = set()

    for j in range(1, n):
        for i in range(j + 1, n + 1):
            a, b, c = i * i - j * j, i * i + j * j, 2 * i * j
            d = gcd(c, gcd(a, b))
            a, b, c = a // d, b // d, c // d

            if max(a, b, c) < n:
                basic.add(tuple(sorted((a, b, c))))

    extended = set()
    for a, b, c in basic:
        for i in range(1, n // c + 1):
            extended.add((a * i, b * i, c * i))

    return extended


def solutions(n):
    maxedge = {}

#    test_set = set()
    for a, b, c, in pyth_trips(n * 2):
        maxedge[b] = maxedge.get(b, 0) + a // 2

#        for i in range(1, a // 2 + 1):
#            test_set.add((i, a - i, b))

        if 2 * a >= b:
            maxedge[a] = maxedge.get(a, 0) + b // 2 - (b - a) + 1

#            for i in range((b - a), b // 2 + 1):
#                test_set.add((i, b - i, a))

    return maxedge


def go(n, min_size):
    d = solutions(min_size)
    for i in sorted(d.keys()):
        n -= d[i]
        if n < 0:
            if i < min_size:
                return i


def naive(m):
    nsol = 0
    sol = set()
    for i in range(1, m + 1):
        for j in range(i, m + 1):
            ij2 = (i + j) ** 2
            for k in range(j, m + 1):
                q2 = ij2 + k ** 2
                q = int(math.sqrt(q2))
                if q ** 2 == q2:
                    nsol += 1
                    sol.add((i, j, k))

    return nsol, sol


print(go(1000000, 2250))
