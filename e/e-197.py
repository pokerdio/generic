def f(x, quantum=10**-18):
    xp = 30.403243784 - (x * x * quantum)
    return int(2 ** xp)


v = [-1]

s = set((-1,))


def step():
    global s, v
    new = f(v[-1])
    if new in s:
        return v.index(new)
    v.append(new)
    s.add(new)


def stepn(n):
    global s, v
    for i in range(n):
        loop = step()
        if loop:
            v = v[loop:]
            l = len(v)
            un = v[(n - loop) % l]
            un1 = v[(n - loop + 1) % l]

            return un + un1
