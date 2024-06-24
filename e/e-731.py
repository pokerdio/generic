from primez import rm_prime_kapow as kapow


def get(n, ten):
    three = 3 ** n

    if three - ten > 20:
        return [0] * 20

    ret = []

    while three >= ten:
        ret.append(0)
        ten += 1

    r = kapow(10, ten - 1, three)
    for _ in range(20):
        r = r * 10
        ret.append(r // three)
        r %= three
    return ret[:20]


def a(n):
    ret = [0] * 20
    for i in range(1, 100000):
        v = get(i, n)
        if sum(v) == 0:
            return ret[:10]
        ret = [ret[i] + v[i] for i in range(20)]
        for j in range(19, 0, -1):
            ret[j - 1] += ret[j] // 10
            ret[j] %= 10
        ret[0] %= 10
    return ret[:10]
