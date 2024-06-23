from math import atan


def xy(n):
    y = (n + 1 - sqrt(2 * n)) / (n * n + 1)
    x = y * n
    return x, y


def proc(n, undercircle=1.0 - pi / 4.0):
    x, y = xy(n)

    x1, y1 = 1.0 - x, 1.0 - y
    a = atan(x1 / y1)

    pie = a / 2  # the area of the pizza pie
    abovepie = x1 * y1 / 2.0
    underpie = x1 - abovepie - pie

    return (x * y / 2 + underpie) / undercircle


def go(p=0.001):
    for i in range(1, 100000):
        if proc(i) < p:
            return i


print(go())
