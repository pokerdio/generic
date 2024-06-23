#!/usr/bin/env python3

# https://projecteuler.net/problem=69


def load():
    tri = []
    for s in open("p102_triangles.txt").readlines():
        tri.append([int(w) * 3 for w in s.split(",")])
    return tri


def oss(x1, y1, x2, y2, c_x, c_y):
    """origin on same side as c_x, c_y"""
    a = y1 - y2
    b = x2 - x1
    c = y2 * x1 - y1 * x2

    sign_c = a * c_x + b * c_y + c
    return sign_c * c >= 0


def hasorigin(xy):
    cx, cy = (xy[0] + xy[2] + xy[4]) // 3, (xy[1] + xy[3] + xy[5]) // 3
    return oss(xy[0], xy[1], xy[2], xy[3], cx, cy) and \
        oss(xy[0], xy[1], xy[4], xy[5], cx, cy) and \
        oss(xy[2], xy[3], xy[4], xy[5], cx, cy)


triangles = load()
print(sum(hasorigin(tri) for tri in triangles))
