def ini():
    v = {}
    for i in range(1, 10):
        for j in range(0, 10 - i):
            for k in range(0, 10 - i - j):
                v[(i, j, k)] = 1
    return v


expand_dict = {}


def expand(t):
    global expand_dict

    if t in expand_dict:
        return expand_dict[t]

    ret = []
    for i in range(10 - t[1] - t[2]):
        ret.append((t[1], t[2], i))

    expand_dict[t] = ret
    return ret


def step(v):
    v2 = {}
    for t, k in v.items():
        for t2 in expand(t):
            v2[t2] = v2.get(t2, 0) + k
    return v2


def go():
    v = ini()
    for i in range(17):
        v = step(v)
    return sum(list(v.values()))
