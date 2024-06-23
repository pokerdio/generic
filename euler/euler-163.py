def tri_count(w, n):
    assert(w <= n)
    upright = (n - w + 1) * (n - w + 2) // 2

    if w * 2 <= n:
        upside_down = (n + 1 - w * 2) * (n + 1 - w * 2 + 1) // 2
    else:
        upside_down = 0

    return upright + upside_down


def go(n):
    s = 6 * tri_count(1, n)
    for i in range(2, n + 1):
        s += 12 * tri_count(i, n)

    for i in range(1, n + 1):
        s += 10 * tri_count(i, n)

    return s
