#!/usr/bin/env python3



def dot(v0, v1):
    return v0[0] * v1[0] + v0[1] * v1[1]


def dif(v0, v1):
    return (v0[0] - v1[0], v0[1] - v1[1])


def edges(v0, v1, v2):
    return dif(v0, v1), dif(v1, v2), dif(v2, v0)


def test(x1, y1, x2, y2):
    v = edges((0, 0), (x1, y1), (x2, y2))
    if (0, 0) in v:
        return 0
    if (dot(v[0], v[1]) == 0 or dot(v[1], v[2]) == 0 or
            dot(v[2], v[0]) == 0):
        #        print(x1, y1, x2, y2)
        return 1
    return 0


def go(n):
    k = 0

    for x1 in range(n + 1):
        print("%d/%d" % (x1, n))
        for y1 in range(n + 1):
            for x2 in range(n + 1):
                for y2 in range(n + 1):
                    k += test(x1, y1, x2, y2)
    return k // 2
