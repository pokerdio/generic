def vspread(v):
    return max(v.keys()) - min(v.keys())


def vmin(v):
    return min(v.keys())


def foo(n):
    v0 = {-3: n, -1: n}
    v = {-3: [v0]}

    for i in range(-3, -10, -1):
        x = 0
        s = set(v[i])
        v[i] = list(s)

        while x < len(v[i]):
            pos = v[x]
            for explo in explode(pos):
                explo_i = min(explo.keys())
                if explo_i
            x += 1
