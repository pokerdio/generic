from builtins import sum


def rn():
    x = 55
    r = 1
    for _ in range(100000):
        yield r % 101 + 50
        r = r * 5 % 1000000007


def take3(it):
    for _ in range(100000):
        yield(next(it), next(it), next(it))


def make_data(n):
    maker = take3(rn())
    ret = list(next(maker) for _ in range(n))
    return ret, int(ceil(sum(x[0] for x in ret) / sqrt(2)))


def solve(troll, pit, shortie):
    v = [0] + [None] * pit
    for h, l, q in troll:
        v2 = [None] * (pit + 1)
        for i in range(pit):
            if v[i] != None:
                v2[i] = v[i] + q
            if i >= h and v[i - h]:
                if i + h + l >= pit:
                    if v[i] is None or v2[i] < v[i - h] + q:
                        v2[i] = v[i - h] + q
                elif v[i] is None or v2[i] < v[i - h]:
                    v2[i] = v[i - h]
        v = v2
    return max(x or 0 for x in v[pit - shortie:])


def go(n=1000):
    data, pit_h = make_data(n)

    top = sorted(list(set(h + l for h, l, q in data)))[:3]
    best = None
    for hl in top:
        sol = solve([x for x in data if x[0] + x[1] > hl],
                    pit_h - sum(x[0] for x in data if x[0] + x[1] <= hl), hl)

        if not best or sol > best:
            best = sol

    return best
