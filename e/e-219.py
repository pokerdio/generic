def stepn(x, n, v):
    v[x] -= n
    if v[x] <= 0:
        v.pop(x)

    v[x + 1] = v.get(x + 1, 0) + n
    v[x + 4] = v.get(x + 4, 0) + n


def go(n):
    v = {1: 1, 4: 1}
    n -= 2
    while n > 0:
        x = min(v.keys())
        count = v[x]
        if count > n:
            count = n

        n -= count
        stepn(x, count, v)

    return sum(i * v[i] for i in v.keys())
