def foo(m, n):
    f = (2 * m - n) / (2 * m + 2 * n)
    if f >= 1.0:
        return True
    if exp(log(1 + 2 * f) * m + log(1 - f) * n) >= 1000000000:
        return True


def bar():
    v = [1, 1]
    for i in range(999):
        v = list(a + b for a, b in zip(v + [0], [0] + v))
    assert(len(v) == 1001)

    s = 0
    for i in range(1000, 250, -1):
        if foo(i, 1000 - i):
            s += v[i]
        else:
            break
    assert(s == sum(v[i + 1:]))
    return s / (2 ** 1000)


print("%.12f" % bar())
