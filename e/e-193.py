#import primez
from math import sqrt


def mobi(n):
    v = [0] * (n + 1)

    for i in range(2, n + 1):
        if v[i] == 0:
            for j in range(i * i, n + 1, i * i):
                v[j] = -1
            for j in range(i, n + 1, i):
                if v[j] >= 0:
                    v[j] += 1
    for i in range(2, n + 1):
        k = v[i]
        if k == -1:
            v[i] = 0
        elif k % 2 == 0:
            v[i] = 1
        else:
            v[i] = -1
    return v


def square_free(n):
    n2 = int(sqrt(n))

    m = mobi(n2)

    s = 0
    for i in range(2, n2 + 1):
        s += m[i] * (n // (i * i))
    return n + s


# def _square_free(n):
#     v = [True] * (n + 1)
#     v[0] = False
#     for p in primez.iterate_primez(int(sqrt(n)) + 1):
#         for i in range(p * p, n + 1, p * p):
#             v[i] = False
#     return sum(v)


print(square_free(2**50))
