import primez


def twelve(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    n -= 2
    return 2 + 6 * n + 3 * n * (n - 1)


def D(*x):
    return sum(primez.isprime(i) for i in x)


def loop(n):
    a, b, c, d = twelve(n - 1), twelve(n), twelve(n + 1), twelve(n + 2)
    da, db, dc = n - 2, n - 1, n

    if D(c - b - 1, c - b + 1, d - b - 1) == 3:
        yield b

    dlast = D((d - 1) - (c - 1), (d - 2) - (c - 1), (c - 1) - b,
              (c - 1) - a, (c - 1) - (b - 1))
    clast = c - 1

    for _ in range(5):
        a += da
        b += db
        c += dc
        if D(c - b - 1, c - b + 1, b - a) == 3:
            yield b

    if dlast == 3:
        yield clast


def go(tile=2000):
    n, k = 2, 1
    while True:
        for i in loop(n):
            k += 1
            if k % 10 == 0:
                print(k)
            if k == tile:
                return i
        n += 1
