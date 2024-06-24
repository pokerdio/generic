#!/usr/bin/env python3

# https://projecteuler.net/problem=577 counting hexagons inside
# triangular grid


# main trick is you make slanted hexagons by inscribing them inside a normal one
# (its sides are paralel to the triangle edges) - you make the six vertices of the
# slant hexagon by taking a grid point on each edge of the circumscribed hexagon
# you always take that point at the same distance from a vertex
# therefore a normal hexagon with edges of length n have n-1 inscribed slanted hexes

def H(n):
    s = 0
    for h in range(1, n // 3 + 1):  # hex edge
        max_points = n - 3 * h + 1
        normies = max_points * (max_points + 1) // 2
        s += normies * h  # including slanties
    return s


def go(n):
    return sum(H(i) for i in range(3, n + 1))
