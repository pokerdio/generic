from math import atan, pi, sin, cos
w, h, alpha = (int(c) for c in input().split())
w, h = max(w, h), min(w, h)
rect_surface = w * h
w /= 2.0
h /= 2.0

if alpha > 90:
    alpha = 180 - alpha

if alpha == 90:
    print(4.0 * min(w, h) ** 2)
    exit()

if alpha == 0:
    print(rect_surface)
    exit()

pi2 = pi / 2.0

alpha = pi * alpha / 180


def rot(v, theta):
    s, c = sin(theta), cos(theta)
    return [(x*c-y*s, x*s+y*c) for x, y in v]


rec = [(w, h), (-w, h), (-w, -h), (w, -h)]
beta = atan(h/w)  # angle of the first corner (0..pi/2)
rec2 = rot(rec, alpha)


def horiz(xy0, xy1, h):
    """intersects line xy0xy1 with the horizontal line at height h"""
    x0, y0 = xy0
    x1, y1 = xy1

    # ay0+b = x0
    # ay1+b = x1

    a = (x0-x1)/(y0-y1)
    b = x0 - a * y0

    return a * h + b


def vert(xy0, xy1, w):
    """intersects line xy0xy1 with the vertical line at x=w"""
    x0, y0 = xy0
    x1, y1 = xy1

    # ax0+b = y0
    # ax1+b = y1

    a = (y0-y1)/(x0-x1)
    b = y0 - a * x0
    return a * w + b


if alpha < 2.0 * beta:    # type 1
    x1 = horiz(rec2[0], rec2[3], h)
    x2 = horiz(rec2[0], rec2[1], h)

    y1 = vert(rec2[0], rec2[3], w)
    y2 = vert(rec2[0], rec2[1], -w)

    print(rect_surface - (w - x1) * (h - y1) - (w + x2) * (h - y2))
else:  # type 2
    x1 = horiz(rec2[0], rec2[1], h)
    x2 = horiz(rec2[2], rec2[3], h)
    print(rect_surface - (x1 + w + w - x2) * (2.0 * h))
