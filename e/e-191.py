def expand(late, last):
    if not late:
        yield (True, (last + "L")[-4:])
    yield (late, (last + "O")[-4:])
    if last[-2:] != "AA":
        yield (late, (last + "A")[-4:])


def step(v):
    ret = {}
    for key, count in v.items():
        for newkey in expand(*key):
            ret[newkey] = ret.get(newkey, 0) + count
    return ret


def go(n):
    ret = {(False, ""): 1}
    for i in range(n):
        ret = step(ret)
    return sum(list(ret.values()))
