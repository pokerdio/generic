
def make_div_sum(n):
    a = [0] + [1] * (n - 1)
    for i in range(2, n):
        a[i * 2:n:i] = (a[j] + i for j in range(i * 2, n, i))
    return a


def find_chain(v, i0):
    ok = set((i0, ))
    ret = [i0]
    n = len(v)
    i = i0
    while True:
        i = v[i]
        if i >= n:
            return None, ok
        if i in ok:
            return ret[ret.index(i):], ok

        ok.add(i)
        ret.append(i)


def find_longest_chain(v):
    ok = set(range(len(v)))
    ok -= set((0, 1))

    bestcycle = [1]
    while ok:
        chain, removable = find_chain(v, ok.pop())
        ok -= removable
        if chain:
            if len(chain) > len(bestcycle):
                bestcycle = chain
    return bestcycle


v = make_div_sum(10**6)
print(min(find_longest_chain(v)))
