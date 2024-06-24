from primez import decompose as dc


def mul(a, b):
    for p, m in b.items():
        a[p] = a.get(p, 0) + m
    return a


def div(a, b):
    for p, m in b.items():
        a[p] = a.get(p, 0) - m
        assert(a[p] >= 0)
        if not a[p]:
            a.pop(p)
    return a


def num(f):
    ret = 1
    for p, m in f.items():
        ret *= (p ** m)
    return ret


def gorow(row, vf=[]):
    free = set()
    while (row + 1 >= len(vf)):
        vf.append(dc(len(vf)))
    x = {}

    for i in range(0, row):
        mul(x, vf[row - i])
        div(x, vf[1 + i])
        square_free = (max(x.values(), default=1) <= 1)
        if square_free:
            free.add(num(x))
    return free


def go(row):
    ret = set()
    for i in range(row):
        ret.update(gorow(i))
    return sum(list(ret))
