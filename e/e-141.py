from math import sqrt
from builtins import sum


def foo3():
    #    n = a2 * b3 * c + a*c*c

    n = 10**12

    for b in range(2, 10001):
        if b < 100:
            print(b)
        if b % 100 == 0:
            print(b)
        b3 = b ** 3
        for c in range(1, b):
            b3c = b3 * c
            if b3c > n:
                break
            for a in range(1, 1000001):
                x = a * a * b3c + a * c * c
                if x > n:
                    break
                if int(sqrt(x)) ** 2 == x:
                    yield x


def foo4():
    #    n = a2 * b3 * c + a*c*c

    n = 10**12

    for b in range(2, 10001):
        if b < 100:
            print(b)
        if b % 100 == 0:
            print(b)
        b3 = b ** 3
        for a in range(1, 1000001):
            a2b3 = a * a * b3
            if a2b3 > n:
                break

            for c in range(1, b):
                x = a2b3 * c + a * c * c
                if x > n:
                    break
                if int(sqrt(x)) ** 2 == x:
                    yield x


print(sum(set(foo3())))
