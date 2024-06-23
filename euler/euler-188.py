def go(x, y, mod):
    if y == 1:
        return x % mod
    if y == 2:
        return (x ** x) % mod
    if mod == 1:
        return 0

    k = 1
    v = [k]
    s = {k}

    while True:
        k = (k * x) % mod
        if k in s:
            assert(v[0] == k)
            cycle = len(v)
            break
        s.add(k)
        v.append(k)

    rec = go(x, y - 1, cycle)

#    print(v, rec, cycle)
    ret = v[rec]

    return ret


print(go(1777, 1855, 10**8))
