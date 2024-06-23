import math
from fractions import Fraction as Fr
from functools import reduce


xy = [[float(c) for c in input().split()] for _ in "foo"]

#xy = [[31.312532, 151.532355], [182.646053, 56.534075], [15.953947, 127.065925]]


def circumcenter(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3

    d = 2 * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
    ux = ((x1**2 + y1**2) * (y2 - y3) + (x2**2 + y2**2)
          * (y3 - y1) + (x3**2 + y3**2) * (y1 - y2)) / d
    uy = ((x1**2 + y1**2) * (x3 - x2) + (x2**2 + y2**2)
          * (x1 - x3) + (x3**2 + y3**2) * (x2 - x1)) / d
    return ux, uy


def dist(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)


def angle_from_points(p1, p2, p3):
    a = dist(p2, p3)
    b = dist(p1, p3)
    c = dist(p1, p2)
    try:
        angle = math.acos((a**2 + b**2 - c**2) / (2*a*b))
    except ValueError:
        return 180.0
    return math.degrees(angle)


def denom(x: float, max_denominator=1000):
    return Fr(x).limit_denominator(max_denominator).denominator


def lcm(*args):
    return reduce(lambda a, b: a*b // math.gcd(a, b), args)


def regular_polygon_area(n, r):
    return (n * (r ** 2)) * math.sin(2 * math.pi / n) / 2


def go(xy=xy):
    center_xy = circumcenter(*xy)
    a1 = angle_from_points(xy[0], xy[1], center_xy)
    a2 = angle_from_points(xy[1], xy[2], center_xy)
    a3 = angle_from_points(xy[2], xy[0], center_xy)
    n = lcm(denom(a1 / 360.0), denom(a2 / 360.0), denom(a3 / 360.0))

    return regular_polygon_area(n, dist(center_xy, xy[0]))


print(go())
