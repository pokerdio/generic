from builtins import sum


def int4(v):
    return v[0] + v[1] * 10 + v[2] * 100 + v[3] * 1000


def expand(n):
    v = [int(c) for c in reversed("%04d" % n)]

    ret = [0] * 4

    base = 0

    for i in range(4):
        over = v[i] - 1
        if over > 0:
            ret[i] += over
            ret[(i + 1) % 4] += over
            base += over
        v[i] = min(v[i], 1)

    for i in range(16):
        v2 = [int(((1 << x) & i) > 0) for x in range(4)]

        if True in (v2[x] > v[x] for x in range(4)):
            continue

        ret2 = ret.copy()
        base2 = base
        for j in range(4):
            if v2[j]:
                ret2[j] += 1
                ret2[(j + 1) % 4] += 1
                base2 += 1
        if base2 and sum(ret2) < 8:
            yield base2, int4(ret2)


def gen_trans():
    g = {}
    new = {1}
    while new:
        new2 = set()
        for x in new:
            g[x] = list(expand(x))
            for delta, y in g[x]:
                if y not in g:
                    new2.add(y)

        new = new2
    return g


def go(n):
    v = [{1: 1}, {}, {}, {}]

    g = gen_trans()
    for _ in range(n):
        for pos, count in v[0].items():
            for delta, pos2 in g[pos]:
                v[delta][pos2] = (v[delta].get(pos2, 0) + count) % 1000000000
        v = v[1:] + [{}]
    ret = 0
    for pos, count in v[0].items():
        if max(str(pos)) == "1":
            ret += count
    return ret % 1000000000
