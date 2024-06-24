import primez


def go(n):
    d = {2: 1}
    s = 3
    ret = 3
    mod = 1000000087
    for i in range(3, n + 1):
        if i % 10000 == 0:
            print(i)
        for p, q in primez.decompose(i).items():
            if p in d:
                s = (s * primez.rev(1 + d[p] * 2, mod)) % mod
            d[p] = d.get(p, 0) + q
            s = (s * (1 + d[p] * 2)) % mod
        ret = (ret + s) % mod
    return ret
