def split_go(n, s):
    ten = 1
    while True:
        s += (n % 10) * ten
        n //= 10
        ten *= 10
        if n > 0:
            yield from split_go(n, s)
        else:
            yield s
            return


def split_set(n):
    return set(split_go(n, 0))


def split_dict(n):
    return {i: split_set(i) for i in range(1, n + 1)}


def split2(n, targetn, v):
    if n < targetn:
        return False

    if n <= 10000:
        return targetn in v[n]

    ten = 1
    while True:
        targetn = targetn - (n % 10) * ten
        if targetn < 0:
            return False
        n //= 10
        ten *= 10

        if n == 0:
            return targetn == 0
        else:
            if split2(n, targetn, v):
                return True


def go2(n):
    v = split_dict(10000)

    ret = 0
    for i in range(2, n + 1):
        if i % 10000 == 0:
            print(i)

        if split2(i * i, i, v):
            ret += i * i
    return ret
