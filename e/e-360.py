from builtins import sum
from math import sqrt
from primez import decompose_iterate


def gcd3(x, y, z):
    return gcd(x, gcd(y, z))


def foo3d(k):
    for m in range(0, k):
        sm = m * m
        if sm >= k:
            break
        for n in range(0, k):
            sn = sm + n * n
            if sn >= k:
                break
            for p in range(0, k):
                sp = sn + p * p
                if sp >= k:
                    break

                for q in range(0, k):
                    sq = sp + q * q
                    if sq > k:
                        break
                    if sq > 0 and k % sq == 0:
                        x, y, z = m * m + n * n - p * p - q * q, \
                            2 * (m * q + n * p), 2 * (n * q - m * p)

                        d = k // sq
                        if x > 0 and y > 0 and z > 0:
                            yield x * d, y * d, z * d


def foo3d2(k):
    divk = sorted(decompose_iterate(k))

    for m in range(1, k):
        sm = m * m
        if sm >= k:
            break
        for n in range(0, k):
            sn = sm + n * n
            if sn >= k:
                break
            for p in range(0, k):
                if p * p >= sn:
                    break
                sp = sn + p * p

                if sp >= k:
                    break
                xrest = sn - p * p

                for d in divk:
                    if d > sp:
                        q2 = d - sp

                        if q2 >= xrest:
                            break
                        q = int(sqrt(q2))

                        if q * q == q2:
                            x, y, z = m * m + n * n - p * p - q * q, \
                                2 * (m * q + n * p), 2 * (n * q - m * p)
                            if x > 0 and y > 0 and z > 0:
                                yield tuple(sorted((x * k // d, y * k // d, z * k // d)))


def foo2d(k):
    k2 = k * k
    for i in range(1, k):
        i2 = i * i
        j = int(sqrt(k2 - i2))
        if j * j + i2 == k2:
            yield i, j


def bar(k, rotate=[0, 1, 3, 6]):
    s = k * 6
    for x, y in foo2d(k):
        s += 12 * (x + y)

    for xyz in set(tuple(sorted(x)) for x in foo3d2(k)):
        s += 8 * sum(xyz) * rotate[len(set(xyz))]

    # for x, y, z in foo3d(k):
    #     s += 8 * (x + y + z)

    return s


def bork(k):
    k2 = k * k
    for x in range(1, k):
        x2 = x * x
        for y in range(1, k):
            y2 = y * y
            for z in range(1, k):
                if x2 + y2 + z * z == k2:
                    yield x, y, z
#--------------------


def foo(five):
    m = 5 ** (five - 1)

    d2 = 5 ** (2 * five)
    for a in range(1, m):
        aa = (a * 5)
        a2 = aa ** 2
        for b in range(1, m):
            for bplus in (2, 3):
                bb = (b * 5 + bplus)
                b2 = bb ** 2

                left = d2 - a2 - b2

                if left > 0:
                    cc = int(sqrt(left))
                    if cc * cc == left:
                        yield aa, bb, cc

            if b2 + a2 >= d2:
                break


def bar(five):
    for i, j, k in foo(five):
        print(i, j, k, int(sqrt(i * i + j * j + k * k)))


def boo(five):
    for f in range(1, five + 1):
        for a, b, c in foo(f):
            m = 2 ** (2 * five) * 5
            yield


def foo():
    for i in range(25):
        for j in range(25):
            for k in range(25):
                if (i * i + j * j + k * k) % 25 == 0:
                    yield tuple(sorted((i, j, k)))
