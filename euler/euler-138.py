# using euclid formula for generating primitive trips without bothering to check
# for mutual primality


def foo1(n):
    for i in range(2, n):
        for j in range(1, i):
            a, b, c = sorted((i * i - j * j, 2 * i * j, i * i + j * j))

            if abs(2 * a - b) == 1:
                yield i, j, i - j, (i - j) / j, a * 2, b, c


def foo(n):
    for j in range(1, n):
        bestd = int(j * 3.236067977499794)
        for d in range(max(bestd - 3, 1), bestd + 3):
            i = j + d

            a, b, c = sorted((i * i - j * j, 2 * i * j, i * i + j * j))

            if abs(2 * a - b) == 1:
                yield d / j, a, b, c


def go():
    print(sum(sorted(v[2] for v in list(foo(10000))[:12])))


v = [(16, 15, 17),
     (16, 15, 17),
     (272, 273, 305),
     (272, 273, 305),
     (4896, 4895, 5473),
     (4896, 4895, 5473),
     (87840, 87841, 98209),
     (87840, 87841, 98209),
     (1576240, 1576239, 1762289),
     (1576240, 1576239, 1762289),
     (28284464, 28284465, 31622993),
     (28284464, 28284465, 31622993),
     (507544128, 507544127, 567451585),
     (507544128, 507544127, 567451585)]


def fibo(n=100):
    x, y = 1, 1
    yield 1
    yield 1
    for _ in range(n):
        yield x + y
        x, y = y, x + y
