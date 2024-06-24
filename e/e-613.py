from math import isnan


def lenxysq(xy0, xy1):
    return (xy0[0] - xy1[0]) ** 2 + (xy0[1] - xy1[1]) ** 2


def lenxy(xy0, xy1):
    return sqrt((xy0[0] - xy1[0]) ** 2 + (xy0[1] - xy1[1]) ** 2)


def f(x, y):
    """ odds of an ant at xy randomly going towards the big edge
    of the 30/40/50 triangle with the right angle centered at the origin"""

    l1sq = lenxysq((x, y), (40.0, 0.0))
    l2sq = lenxysq((x, y), (0.0, 30.0))

#    print(l1sq, l2sq, l1sq + l2sq - 2500.0)
    if l1sq == 0.0 or l2sq == 0.0:
        return 0.5

#    print(l1sq, l2sq, l1sq + l2sq - 2500.0, (2.0 * sqrt(l1sq) * sqrt(l2sq)))
    a = arccos((l1sq + l2sq - 2500.0) / (2.0 * sqrt(l1sq) * sqrt(l2sq))) / (2.0 * pi)
    if isnan(a):
        return 0.5
    return a


big3 = ((0.0, 0.0), (40.0, 0.0), (0.0, 30.0))


def tri(epsilon=0.1, xy=big3, l=None, v=None, depth=0, f=f):
    """xy is an array of 3 points (the vertices) 
    l is an array of 3 lengths
    v is an array of vertices function values
    f is a lambda (x, y) -> float that gives the value at a point"""

    if not v:
        v = [f(*xy[i]) for i in (0, 1, 2)]
    if not l:
        l = [lenxy(xy[i], xy[(i + 1) % 3]) for i in (0, 1, 2)]

    p = (l[0] + l[1] + l[2]) / 2.0
    a = sqrt(p * (p - l[0]) * (p - l[1]) * (p - l[2]))
    delta = max(v) - min(v)

    if depth > 60:
        ret = sum(v) * a / 3.0
#        print(" . " * depth, tri, "returning X", ret, delta * a)
        return ret

    if delta * a < epsilon:
        ret = sum(v) * a / 3.0
#        print(" . " * depth, tri, "returning A")
        return ret

    rotate = max((0, 1, 2), key=lambda i: l[i])
    if rotate:
        xy = xy[rotate:] + xy[:rotate]
        l = l[rotate:] + l[:rotate]
        v = v[rotate:] + v[:rotate]

    xymid = (xy[0][0] + xy[1][0]) / 2.0, (xy[0][1] + xy[1][1]) / 2.0
    lmid = lenxy(xy[2], xymid)
    valmid = f(*xymid)
    h1 = tri(epsilon, (xy[0], xy[2], xymid),
             (l[2], lmid, l[0] / 2.0),
             (v[0], v[2], valmid), depth + 1)
    h2 = tri(epsilon, (xy[1], xy[2], xymid),
             (l[1], lmid, l[0] / 2.0),
             (v[1], v[2], valmid), depth + 1)
    # if depth == 10:
    #     print(xy, v)
    return h1 + h2


#print(".10f" % (tri(0.0000000001) / 600.0))
# 0.3916721504
