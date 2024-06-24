import matrix


def TWO(n, v={1: 0, 2: 1}):
    if n in v:
        return v[n]

    ret = TWO(n - 2) + THREE(n - 2)
    v[n] = ret
    return ret


def THREE(n, v={1: 0, 2: 2}):
    if n in v:
        return v[n]

    ret = 2 * TWO(n - 2) + 2 * THREE(n - 2) + THREE(n - 1) + THREE_SPECIAL(n - 1)
    v[n] = ret
    return ret


def THREE_SPECIAL(n, v={1: 0, 2: 2}):
    if n in v:
        return v[n]

    ret = 2 * TWO(n - 2) + 2 * THREE(n - 2) + THREE_SPECIAL(n - 1)
    v[n] = ret
    return ret


def XXX(n, v={1: 0, 2: 1}):
    if n in v:
        return v[n]
    ret = XXX(n - 1) + TWO(n - 2) + THREE(n - 2)
    v[n] = ret
    return ret


def T(n):
    return XXX(n) + TWO(n - 1) + THREE(n - 1)


def rec():
    return [[0, 0, 0, 0, 1, 1, 0, 0],  # 2
            [0, 1, 1, 0, 2, 2, 0, 0],  # 3
            [0, 0, 1, 0, 2, 2, 0, 0],  # 3'
            [0, 0, 0, 1, 1, 1, 0, 0],  # XXX
            [1, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0]]


import pprint


def T2(n, mod=10**8):
    pp = pprint.PrettyPrinter()

    m = matrix.pow(rec(), n - 2, mod)
    pp.pprint(m)
    v = matrix.mul(m, [TWO(2), THREE(2), THREE_SPECIAL(2), XXX(2),
                       TWO(1), THREE(1), THREE_SPECIAL(1), XXX(1)], mod)

    pp.pprint(v)
    return (v[3] + v[4] + v[5]) % mod  # xxx(n) + two(n-1) + three(n-1)
