def pairs():
    for twos in range(28):
        for threes in range(13):
            yield 2 ** twos * 3 ** threes, 2 ** (27 - twos) * 3 ** (12 - threes)


def alt_sq_sum(n):
    return n * (n + 1) // 2


def ff(f, n=1):
    if f <= 3:
        zero = f if f < 3 else 4
    else:
        pairs = (f - 3) // 2
        sumpairs = pairs * (6 + 2 * pairs)
        last = ((f + 1) % 2) * (4 + 2 * pairs)

        zero = 4 + sumpairs + last

    if n == 1:
        return zero

    if f == 1:
        startsq = 2
    else:
        startsq = (f // 2) * 2 + 1
    endsq = startsq + n - 2

    if n % 2 == 1:
        return alt_sq_sum(endsq) - alt_sq_sum(startsq - 1) + zero
    else:
        return alt_sq_sum(endsq) + alt_sq_sum(startsq - 1) - zero


def go():
    ret = sum(ff(a, b) for a, b in pairs())
    return ret, ret % (10**8)


print("the answer", go()[-1])
