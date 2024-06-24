def makev(n):
    v = {1: 0, 2: 1}
    a, b = 2, 1

    while b < n:
        a, b, c = a + b, a, b
        v[a] = v[b] + v[c] + (a - b)

    return v, list(sorted(v.keys()))


def go(n, v=None, k=None):
    if not v:
        v, k = makev(n + 1)

    if n in v:
        return v[n] + 1

    sub_n = max(i for i in k if i < n)
    return v[sub_n] + n - sub_n + 1 + go(n - sub_n)


print(go(10**17 - 1))
