def s():
    s0 = 290797

    while True:
        yield s0
        s0 = (s0 * s0) % 50515093


def gen(n):
    v = []
    gen = s()
    for _ in range(n):
        v.append(next(gen))
    return sorted(v)


def median(n):
    v = g(n)
    pairs = []
    for i in range(n - 1):
        for j in range(i + 1, n):
            pairs.append(v[i] * v[j])
    print(len(pairs), max(pairs))
    return sorted(pairs)[len(pairs)//2]


def less_than(v, thresh):
    """how many pairs in v multiply to less than thresh"""
    n = len(v)
    ret = 0
    j = n - 1
    best = 50515093**2
    for i in range(n - 1):
        while (j > i) and (v[i] * v[j] >= thresh):
            if v[i] * v[j] < best:
                best = v[i] * v[j]
            j -= 1
        if i >= j:
            break
        ret += (j - i)
    return ret, best


def go(n):
    assert(n % 2 == 1)  # I can't even
    v = gen(n)
    desired_less = n * (n - 1) // 4

    low, high = 0, 50515093**2

    while high > low:
        mid = (high + low)//2
        less, best_fit = less_than(v, mid)
        #print(mid, high - mid, less, best_fit)
        if less == desired_less:
            return best_fit
        if less < desired_less:
            low = mid
        else:
            high = mid
    assert(False)
