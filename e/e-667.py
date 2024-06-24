from numpy import arange


def bar(v):
    return arccos(v * 0.5) + arcsin(1.0 / v) + arccos(0.5 / v)


def bar2(v):
    return arccos(v * 0.5) + arcsin(0.99 / v) + arccos(0.5 / v)


def monoguess(f, wanted_value, x, y):
    x, y = min(x, y), max(x, y)
    fx = f(x)
    fy = f(y)

    if fx > fy:
        x, y = y, x
        fx, fy = fy, fx

    for _ in range(50):
        mid = (x + y) * 0.5
        fmid = f(mid)
        if wanted_value > fmid:
            x, fx = mid, fmid
        else:
            y, fy = mid, fmid
        assert(fx <= fy)
    return mid


def edge(f):
    return monoguess(f, pi, 1.0, 2.0)


def tri_surface(a, b, c):
    p = (a + b + c) / 2
    return sqrt(p * (p - a) * (p - b) * (p - c))


def go(f=bar):
    l = edge(f)
    return 2.0 * tri_surface(l, l, 1.0) + tri_surface(l, 1.0, 1.0)
