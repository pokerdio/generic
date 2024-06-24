def modpow(p, q, mod):
    v = [p % mod]
    two = 1

    while two <= q:
        two *= 2
        v.append(v[-1] ** 2 % mod)

    two = 1
    ret = 1
    k = 0
    while two <= q:
        if two & q:
            ret *= v[k]
            ret %= mod
        two *= 2
        k += 1
    return ret


def go():
    v = [1] + [0] * 249
    for i in range(1, 250251):
        mew = modpow(i, i, 250)
        v = list((v[i] + v[(i + mew) % 250]) % 10000000000000000
                 for i in range(250))
    return v[0] - 1
