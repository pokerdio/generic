# project euler problem 107


def load(fname):
    ret = {}
    i = 0
    for line in open(fname).readlines():
        line = line.strip()
        j = 0
        for w in line.split(","):
            if w != "-" and i < j:
                ret[(i, j)] = int(w)
            j += 1
        i += 1

    return ret


def load_problim():
    return load("p107_network.txt")


def load_test():
    return load("p107_net2.txt")


def purge_tree(g):
    n = max(max(i) for i in g.keys())
    colors = list(range(n + 1))

    bestg = {}
    while g:
        print(colors)

        print(bestg)
        i, j = min(g, key=lambda x: g[x])
        c1, c2 = colors[i], colors[j]
        assert(c1 != c2)

        bestg[(i, j)] = g[(i, j)]

        c = set((c1, c2))

        purge = []
        for a, b in g.keys():
            if colors[a] in c and colors[b] in c:
                purge.append((a, b))
        for p in purge:
            del g[p]

        colors = [c1 if c == c2 else c for c in colors]
    return bestg


def gvalue(g):
    return sum(list(g.values()))


def go(load=load_problim):
    g = load()
    return gvalue(g) - gvalue(purge_tree(g))
