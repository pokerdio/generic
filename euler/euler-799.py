from math import sqrt


def p(n):
    return n * (3 * n - 1) // 2


possibles = set()


def count_sums(v):
    if len(v) < 4:
        return 0

    val = v[-1]

    n = len(v)
    k = n - 2
    count = 0

    for i in range(n - 2):
        while k >= 0 and v[i] + v[k] > val:
            k -= 1
        if i >= k:
            break
        if v[i] + v[k] == val:
            print(f"{val} = {v[i]}+{v[k]}")
            possibles.add(v[i])
            possibles.add(v[k])
            count += 1
    return count


def first(n):
    x = 1
    v = []
    while True:
        v.append(p(x))
        x += 1
        count = count_sums(v)
        if count == n:
            return v
