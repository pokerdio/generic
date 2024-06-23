from collections import Counter as C


def ints():
    return [int(x) for x in input().split()]


p = [ints() for _ in range(3)]

x, y = zip(*p)


if len(set(x)) == 1 or len(set(y)) == 1:
    print(1)
elif len(set(x)) == 2:
    c = C(x)
    xcommon = [x for x in c if c[x] == 2][0]
    xodd = [x for x in c if c[x] == 1][0]

    ycommon1, ycommon2 = sorted(y for x, y in p if x == xcommon)
    yodd = [y for x, y in p if x == xodd][0]
    if ycommon1 < yodd < ycommon2:
        print(3)
    else:
        print(2)
elif len(set(y)) == 2:
    c = C(y)
    ycommon = [y for y in c if c[y] == 2][0]
    yodd = [y for y in c if c[y] == 1][0]

    xcommon1, xcommon2 = sorted(x for x, y in p if y == ycommon)
    xodd = [x for x, y in p if y == yodd][0]
    if xcommon1 < xodd < xcommon2:
        print(3)
    else:
        print(2)
else:
    print(3)
