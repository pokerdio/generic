import primez


def cube(x):
    return round(x ** (1 / 3)) ** 3 == x


def go(n):
    s = 0
    for i in primez.iterate_primez(n):
        for k in range(1, int(sqrt(i / 3)) + 5):
            if cube(k ** 3 + i):
                s += 1
                break
    return s
