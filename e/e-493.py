def f(n):
    ret = 1
    for i in range(2, n + 1):
        ret *= i
    return ret


def c(m, n):
    return f(n) // f(m) // f(n - m)


def foo():
    v = [c(20, col * 10) * c(col, 7) for col in range(2, 8)]

    v2 = []
    for i in range(len(v)):
        v2.append(v[i])
        for j in range(i):
            v2[-1] -= v2[j] * c(i - j, 5 - j)

    return sum((i + 2) * v2[i] for i in range(len(v2))) / sum(v2)
