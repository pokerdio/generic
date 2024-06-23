points = [[int(c) for c in input().split()] for _ in range(3)]

#points = [[1, 1], [3, 5], [8, 6]]
# from random import randint
# points = [[randint(1, 10) for _ in range(2)] for _ in range(3)]


def desired(p=points):
    x = [xy[0] for xy in p]
    y = [xy[1] for xy in p]
    return max(y) - min(y) + max(x) - min(x)


def clean(v):
    return [[a, b, c, d] for a, b, c, d in v if a != c or b != d]


def seglen(v):
    ret = 0
    for a, b, c, d in v:
        ret += abs(a - c) + abs(b - d)
    return ret


def connect2(a, b, c, d):
    """yields two segments and a mid point"""
    yield [[a, b, c, b], [c, b, c, d]], [c, b]
    yield [[a, b, a, d], [a, d, c, d]], [a, d]


def connect3_ordered(a, b, c, d, e, f):
    "yields four segments by connecting ab to cd then this to ef"
    for s1, mid in connect2(a, b, c, d):
        for s2, _ in connect2(a, b, e, f):
            yield s1 + s2
        for s2, _ in connect2(c, d, e, f):
            yield s1 + s2
        for s2, _ in connect2(*mid, e, f):
            yield s1 + s2


def connect3(a, b, c, d, e, f):
    yield from connect3_ordered(a, b, c, d, e, f)
    yield from connect3_ordered(a, b, e, f, c, d)
    yield from connect3_ordered(c, d, e, f, a, b)


def go(a, b, c, d, e, f):
    best = abs(a - c) + abs(a-e) + abs(b-d) + abs(b-f) + 1
    bestv = 0

    for v in connect3(a, b, c, d, e, f):
        v = clean(v)
        vlen = seglen(v)
        if vlen < best:
            best = vlen
            bestv = v
    return bestv


bestv = go(*points[0], *points[1], *points[2])
#print(seglen(bestv), desired())
print(len(bestv))
for seg in bestv:
    print(" ".join(str(c) for c in seg))
