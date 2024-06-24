#!/usr/bin/env python3


from itertools import islice, count

v = {(1, 1): 1}


def foo():
    global v
    for i in range(2, 100):
        s = 0
        for j in range(1, i):
            s += v.get((i - j, min(i - j, j)), 0)
            v[(i, j)] = s
        v[(i, i)] = s + 1
        if s % 1000000 == 0:
            print(i)
            break


def bi(n):
    i = 1
    s = ""
    sep = ""
    while i <= n:
        if i & n:
            s += (sep + str(i))
            sep = " + "
        i *= 2
    print("%s = %d" % (s, n))


def p(n):
    v = [1, 1]

    for i in range(2, n):
        if i % 1000 == 0:
            print(i)
        s = 0
        k = 1
        for j in range(1, i):
            a, b = i - j * (3 * j - 1) // 2, i - j * (3 * j + 1) // 2
            a = 0 if a < 0 else v[a]
            b = 0 if b < 0 else v[b]
            s += k * (a + b)
            k = -k

            if a == 0 and b == 0:
                break
        if s % (10 ** 6) == 0:
            print(i, s)
            return v
        v.append(s)
    return v


def penta(n):
    return n * (3 * n - 1) // 2, n * (3 * n + 1) // 2
