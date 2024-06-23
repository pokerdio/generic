def expand(v, n, free):
    assert(free > 0)
    for i in range(len(v)):
        for j in range(i, len(v)):
            if v[i] + v[j] == n:
                yield (*v, n)
                return
    if free == 1:
        return

    minvalue = max(v[-1] + 1, (n + 1) // (2 ** (free - 1)))

    retset = set()
    for i in range(len(v)):
        for j in range(i, len(v)):
            val = v[i] + v[j]
            if val >= minvalue and val < n and val not in retset:
                yield (*v, val)
                retset.add(val)


def bitz(n):
    ret = 1
    k = 2
    while k <= n:
        k *= 2
        ret += 1
    return ret


def go(n):
    ret = {1: 0}
    v = [(1,)]
    depth = 1
    free = bitz(n) * 2 - 2
    while True:
        v2 = []
        for poz in v:
            for poz2 in expand(poz, n, free):
                v2.append(poz2)
                if poz2[-1] not in ret:
                    ret[poz2[-1]] = depth
                    print(poz2[-1], depth, len(ret))
                    if len(ret) == n:
                        return ret

        depth += 1
        v = v2


def solve():
    print("SOLVED", sum(list(go(200).values())))


# the answer is        1582
