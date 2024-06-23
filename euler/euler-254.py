

def fact(n):
    if n <= 1:
        return 1
    return n * fact(n - 1)


def sdigitz(n):
    ret = 0
    while n > 0:
        ret += n % 10
        n //= 10
    return ret


def go(n, cycles):
    f = [fact(i) for i in range(0, 10)]
    v = {i: (f[i],) for i in range(1, 10) if f[i] <= n}
    ret = v.copy()

    for _ in range(cycles):
        v2 = {}
        for i, digitz in v.items():
            for xtra in range(1, 10):
                s = i + f[xtra]
                sd = sdigitz(s)
                if s <= n and s not in ret:
                    new_digitz = tuple(sorted((*digitz, xtra)))
                    if s not in v2:
                        v2[s] = new_digitz
                    else:
                        v2[s] = min(new_digitz, v2[s])
        ret.update(v2)
        v = v2
    return ret
