a, b, c, d, k = (int(s) for s in input().split())


def gen_lucky(n=10**9):
    ret = [4, 7]
    v = ret
    while True:
        v2 = []
        for x1 in v:
            for digit in (4, 7):
                x2 = x1 * 10 + digit
                if x2 > n:
                    return ret + v2
                v2.append(x2)
        ret = ret + v2
        v = v2


def p_ab_ge_n(a: int, b: int, n: int) -> float:
    """odds a random number between a and b (inclusive) is >= than n"""
    if n <= a:
        return 1.0
    if n > b:
        return 0.0
    return (b - n + 1) / (b - a + 1)


def p_ab_le_n(a: int, b: int, n: int) -> float:
    """odds a random number between a and b (inclusive) is <= than n"""
    if n < a:
        return 0.0
    if n >= b:
        return 1.0
    return (n - a + 1) / (b - a + 1)


def interval_intersect(a: int, b: int, x: int, y: int) -> int:
    """finds the number of ints common to a-b and x-y intervals """
    i, j = max(a, x), min(b, y)
    if i > j:
        return 0
    return j - i + 1


def go(a=a, b=b, c=c, d=d, k=k):
    p = 0.0
    v = gen_lucky(max(a, b, c, d))
    nv = len(v)
    v.append(10**9)

    for i in range(nv - k + 1):
        low, high = v[i], v[i + k - 1]

        sublow = v[i - 1] + 1 if i > 0 else 1
        superhigh = v[i + k] - 1

        if low == high:  #if k is 1 it gets ugly because [sublow,low] and [high,superhigh] intersect
            #so we need to make sure not to count some possible pairs twice
            x = low
            p += interval_intersect(a, b, sublow, x - 1) * \
                interval_intersect(c, d, x + 1, superhigh) / ((b - a + 1) * (d - c + 1))

            p += interval_intersect(c, d, sublow, x - 1) * \
                interval_intersect(a, b, x + 1, superhigh) / ((b - a + 1) * (d - c + 1))

            p += interval_intersect(a, b, sublow, x - 1) * \
                interval_intersect(c, d, x, x) / ((b - a + 1) * (d - c + 1))
            p += interval_intersect(a, b, x + 1, superhigh) * \
                interval_intersect(c, d, x, x) / ((b - a + 1) * (d - c + 1))
            p += interval_intersect(c, d, sublow, x - 1) * \
                interval_intersect(a, b, x, x) / ((b - a + 1) * (d - c + 1))
            p += interval_intersect(c, d, x + 1, superhigh) * \
                interval_intersect(a, b, x, x) / ((b - a + 1) * (d - c + 1))
            p += interval_intersect(a, b, x, x) * \
                interval_intersect(c, d, x, x) / ((b - a + 1) * (d - c + 1))

        else:
            p += interval_intersect(a, b, sublow, low) * \
                interval_intersect(c, d, high, superhigh) / ((b - a + 1) * (d - c + 1))

            p += interval_intersect(c, d, sublow, low) * \
                interval_intersect(a, b, high, superhigh) / ((b - a + 1) * (d - c + 1))

    return p


print(go())
