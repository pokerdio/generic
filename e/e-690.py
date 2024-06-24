def combos(n):
    for leaves in range(1, n):
        #        print(leaves)
        yield leaves + 1  # star trees (center+0 or more leaves)
    for big in range(1, n - 2):
        for small in range(1, min(big, n - big - 2) + 1):
            #            print(big, small)
            yield small + big + 2
            if small + big + 2 < n:
                yield small + big + 3


def go(n):
    v = [1] * (n + 1)
    for combo_size in combos(n):
        for i in range(0, n - combo_size + 1):
            v[i + combo_size] += v[i]
        print(v)
    return v[n]


# vineri 18: 00


def step(g, v):
    v2 = [0] * len(v)
    for i, j in g:
        v2[i] |= v[j]
        v2[j] |= v[i]
    for i in range(len(v)):
        k = v2[i]
        v2[i] = 0
        yield tuple(v2)
        v2[i] = k


def gn(g):
    return max(max(i) for i in g) + 1


def test(g, n=None):
    if not n:
        n = gn(g)

    zero = (0, ) * n

    opened = set(((1,) * n,))
    closed = set()
    father = dict()
    while opened:
        a = opened.pop()
        closed.add(a)
        for i in step(g, a):
            if (i not in closed) and (i not in opened):
                father[i] = a
                opened.add(i)
                if i == zero:
                    while i:
                        print(i)
                        i = father.get(i, None)
                    return True


def gline(n):
    return tuple((i, i + 1) for i in range(n - 1))


def gcycle(n):
    return gline(n) + ((0, n - 1),)


def gstar(n):
    return tuple((0, i) for i in range(1, n))


def gfractal(depth, split):
    if depth <= 1:
        return gstar(split + 1)

    base = gtree(depth - 1, split)
    nbase = gmax(base)

    ret = tuple()

    for subtree in range(split):
        delta = split * subtree + 1
        ret += ((0, delta),)
        ret += tuple((delta + i, delta + j) for i, j in base)
    return ret


def gtree(*leaves):
    ret = tuple()
    leaf_idx = 1
    for father in range(len(leaves)):
        sons = leaves[father]
        ret += tuple((father, son + leaf_idx) for son in range(sons))

        leaf_idx += sons
    return ret


def grndtree(n, max=4):
    return gtree(randint(max) + 1, *(randint(max) for _ in range(n - 1)))


#------------------------------------------------------------


def sums(n, maxsum=None):
    maxsum = maxsum or (n + 1)

    yield ((1, n),)
    for i in range(2, maxsum):
        for j in range(1, n // i + 1):
            if n > i * j:
                for s in sums(n - i * j, i):
                    yield ((i, j), *s)
            else:
                yield ((i, j),)
