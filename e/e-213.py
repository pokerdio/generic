def burn(v):
    v2 = [[0 for x in row] for row in v]

    for i in range(len(v)):
        for j in range(len(v[0])):
            okdelta = []
            for delta in ((+1, 0), (-1, 0), (0, 1), (0, -1)):
                idelta = i + delta[0]
                jdelta = j + delta[1]
                if idelta >= 0 and idelta < len(v) and jdelta >= 0 and jdelta < len(v[0]):
                    okdelta.append((idelta, jdelta))

            for i2, j2 in okdelta:
                v2[i2][j2] += v[i][j] / len(okdelta)

    return v2


def heat(x, y, w, h, n):
    v = [[0] * w for _ in range(h)]
    v[y][x] = 1
    for i in range(n):
        v = burn(v)
    return v


def mp(m):
    for row in m:
        s = ""
        for x in row:
            s += ("%.5f" % x) + " "
        print(s)
