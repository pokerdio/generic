def xy(a):
    return cos(a), sin(a)


def black_above(a, b):
    # assuming a, b are angles less than pi/2,  a biggest, b lowest
    ax, ay = xy(a)  # ax lowest bx biggest
    bx, by = xy(b)  # ay biggest by lowest
    return (bx - ax) * (1.0 - ay)


def black_total(v):
    s = 0.0
    for i in range(len(v) - 1):
        s += black_above(v[i], v[i + 1])
    return s


def optimize(a, b, c, delta):
    """optimize the angle b, within the angles a and c"""

    delta = delta * min(c - b, b - a)

    return max((black_above(a, b2) + black_above(b2, c), b2)
               for b2 in (b - delta, b, b + delta))[1]


def go(n):
    """this one stabilizises in like 10 mins"""
    a = list(reversed([pi * i / 2.0 / n for i in range(0, n + 1)]))

    delta2 = 0.6345435394589305
    for k in range(1, 10000):
        print(k, 4.0 - black_total(a) * 4.0)
        delta = 0.454354654
        for _ in range(100):
            delta = delta * 0.70211231932139
            for i in range(1, n):
                a[i] = optimize(a[i - 1], a[i], a[i + 1], delta)

    return 4.0 - black_total(a) * 4.0


def go2(n):
    """this one stabilizes like in 30 seconds much better"""
    a = list(reversed([pi * i / 2.0 / n for i in range(0, n + 1)]))

    delta = 0.454354654
    for k in range(1, 100):
        print(k, 4.0 - black_total(a) * 4.0)
        ok = True
        while ok:
            ok = False
            for i in range(1, n):
                new = optimize(a[i - 1], a[i], a[i + 1], delta)
                if a[i] != new:
                    ok = True
                    a[i] = new
        delta = delta * 0.6343232

    return 4.0 - black_total(a) * 4.0


# go2(201)
