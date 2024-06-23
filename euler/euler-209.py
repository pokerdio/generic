def bar(i):
    return ((((i & 16) and (i & 8)) > 0) != ((i & 32) > 0))


def foo(a, b, c):
    return (a != 0) * 32 + (b != 0) * 16 + (c != 0) * 8


def step(i):
    return ((i & 31) * 2) + bar(i)


def pairs():
    for i in range(64):
        j = step(i)
        if i != j:
            yield i, j


def baz():
    for a in range(2):
        for b in range(2):
            for c in range(2):
                print(a, b, c, foo(a, b, c), bar(foo(a, b, c)))


def graph():
    v = {i: [] for i in range(1, 64)}
    for i, j in pairs():

        v[i].append(j)
        v[j].append(i)

    return v


def islands():
    v = graph()

    colors = {i: i for i in v.keys()}

    for i in v.keys():
        for j in v[i]:
            ci, cj = colors[i], colors[j]
            if ci != cj:
                colors = {i: (c if (c != cj) else ci) for i, c in colors.items()}

    for col in set(colors.values()):
        yield [x for x in v.keys() if colors[x] == col]


def cycle_lens():
    clean = set(range(64))
    for i in range(64):
        if i not in clean:
            continue
        cycle = set()
        j = i
        while True:
            assert(j in clean)
            cycle.add(j)
            j = step(j)
            if i == j:
                clean = clean - cycle
                yield len(cycle)
                break


def cycle_value(n):
    if n == 1:
        return 1
    if n == 2:
        return 3

    x00, x01, x10, x11 = 1, 1, 1, 0

    for i in range(n - 2):
        x00, x01, x10, x11 = x00 + x01, x00, x10 + x11, x10

    return x00 + x01 + x10


def go():
    ret = 1
    for cy in cycle_lens():
        ret *= cycle_value(cy)
    return ret


print(go())
