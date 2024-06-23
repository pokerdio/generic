def mysqrt(x):
    assert(x >= 0)
    return sqrt(x)


mysqrt = sqrt


def outarea(bigr, r1, r2, r):
    assert(bigr > r1 and bigr > r2)
    # big circle centre CBIG radius bigr
    # inside, adjacent to it and each other, circles C1 C2 with r1 r2
    # inside big, outside 1 and 2, circle C of radius r which we want to calculate

    p1 = r1 + r2 + r  # half perimeter of triangle of C1 C2 and C
    area1 = mysqrt(p1 * r1 * r2 * r)

    # p2 = bigr  # 1/2*(r1+r2+bigr-r1+bigr-r2) half perimeter of triangle of C1 C2 and BIG
    # in fact bigr is half perimeter of C1 C BIG and C2 C BIG so i'll just use it
    area2 = mysqrt(bigr * (bigr - r1 - r2) * r1 * r2)
    area_a = mysqrt(bigr * (bigr - r1 - r) * r * r1)
    area_b = mysqrt(bigr * (bigr - r2 - r) * r * r2)

    return area1 + area2 - area_a - area_b


def inarea(r1, r2, r3, r):
    # three circles adjacent to each other outside each other
    # one circle inside the trapped space between the above
    p1 = r1 + r2 + r3  # half perimeter of C1 C2 C3
    a1 = mysqrt(p1 * r1 * r2 * r3)

    aa = mysqrt((r + r2 + r3) * r * r2 * r3)
    ab = mysqrt((r1 + r + r3) * r1 * r * r3)
    ac = mysqrt((r1 + r2 + r) * r1 * r2 * r)

    return a1 - (aa + ab + ac)


def memoize_zeroify(f):
    memory = {}

    # This inner function has access to memory
    # and 'f'
    def inner(*v):
        if not v:
            return memory
        if v not in memory:
            memory[v] = f(*v)
        return memory[v]

    return inner


def processf(value):
    return abs(value) if value != nan else 666666666.0


@memoize_zeroify
def zeroify(r1, r2, r3, f):
    r1, r2, r3 = sorted((r1, r2, r3))

    r = (r1 + r2) / 2.0

    if f(r3, r1, r2, r) == nan:
        for i in arange(0, 1.05, 0.1):
            r = i * r1 + (1.0 - i) * r2
            if f(r3, r1, r2) != nan:
                break

    delta = r / 5.0
    for i in range(60):
        delta *= 0.875433478342837438

        _, r = min((processf(f(r3, r1, r2, x)), x) for x in
                   (r, r + delta, r - delta, r + 2 *
                    delta, r - 2 * delta, r + 3 * delta, r - 3 * delta))

    assert abs(f(r3, r1, r2, r)) < 0.0001, "fuck %.5f - %.5f %.5f %.5f %.5f" % (f(r3, r1, r2, r), r1, r2, r3, r)

    return r


def go_inside(bigr, r1, r2, n):
    r = zeroify(bigr, r1, r2, outarea)
    ret = pi * r * r
    print("inside level %d adding circle radius %.5f area %.5f" % (n, r, ret))
    if n > 0:
        ret += go_inside(bigr, r1, r, n - 1)
        ret += go_inside(bigr, r, r2, n - 1)
        ret += go_outside(r, r1, r2, n - 1)

    print("inside level %d total area %.5f" % (n, ret))
    return ret


def go_outside(r1, r2, r3, n):
    r = zeroify(r1, r2, r3, inarea)
    ret = pi * r * r
    print("outside level %d adding circle radius %.5f area %.5f" % (n, r, ret))

    if n > 0:
        ret += go_outside(r, r1, r2, n - 1)
        ret += go_outside(r, r2, r3, n - 1)
        ret += go_outside(r, r1, r3, n - 1)

    print("outside level %d total area %.5f" % (n, ret))

    return ret


def go(n):
    bigr = 1
    smallr = 3.0 / (2 * mysqrt(3.0) + 3)

    print("smallr", smallr)
    colored = 3.0 * pi * smallr * smallr
    print("zero colored", colored)
    colored += go_outside(smallr, smallr, smallr, n)
    colored += 3.0 * go_inside(smallr, smallr, bigr, n)

    return colored / (pi * bigr * bigr)
