from fractions import Fraction as F


def blum(n):
    s = 290797
    for _ in range(n):
        c = ()
        for _ in range(4):
            s = (s * s) % 50515093
            c = (*c, s % 500)
        yield c


def abc(x0, y0, x1, y1):
    a = y0 - y1
    b = x1 - x0
    c = (x0 * y1 - x1 * y0)
    return (a, b, c)


def go():
    v = list(blum(5000))

    eq = [abc(*s) for s in v]

    retset = set()

    for i in range(len(v) - 1):
        ai, bi, ci = eq[i]
        for j in range(i + 1, len(v)):
            aj, bj, cj = eq[j]

            s1 = (ai * v[j][0] + bi * v[j][1] + ci) * \
                (ai * v[j][2] + bi * v[j][3] + ci)

            if s1 >= 0:
                continue

            s2 = (aj * v[i][0] + bj * v[i][1] + cj) * \
                (aj * v[i][2] + bj * v[i][3] + cj)

            if s2 >= 0:
                continue

            if ai == 0:
                y = F(-ci, bi)
                x = F(bj * y + cj, -aj)
            else:
                # ai x + biy + ci = 0
                # x = -(biy + ci) / ai

                # -aj(biy + ci) / ai + bjy + cj = 0

                # y(-ajbi / ai + bj) = ajci / ai - cj
                # y(-ajbi + bjai) = ajci - cjai

                y = F(aj * ci - cj * ai, bj * ai - aj * bi)
                x = -F(ci + bi * y, ai)
            retset.add((x, y))

            # ai x + bi y + ci = 0
            # aj x + bj y + cj = 0

    return len(retset)
