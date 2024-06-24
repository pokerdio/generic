def step(want, c):
    want2 = want - (c - 1)  # this needs to go in inout cycles
    inout_cycles = ((want2 + c - 2 - 1) // (c - 2))
    want -= inout_cycles * (c - 2)
    return inout_cycles * c + want + 1


def foo(c, r):
    if c > r:
        return r + 1
    k = c
    for _ in range(r - c + 1):
        k = step(k, c)
    return k


def go(crange, r):
    ret = 0
    for c in crange:
        ret += foo(c, r)
    return ret


print(go(range(3, 41), 30))
