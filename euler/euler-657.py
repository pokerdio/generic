def _I(a, n):
    v = [1] + [0] * (a - 1)  # of 0 length incomplete words, 1 has
    total = v.copy()

    for i in range(1, n + 1):
        v2 = [0] * a
        for j in range(a):
            v2[j] += v[j] * j
            if j < a - 1:
                v2[j + 1] += v[j] * (a - j)
            total[j] += v2[j]
        v = v2
    return sum(total)
