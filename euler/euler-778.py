
def cd(digit, m, ten=1):
    d = m // ten % 10
    if d > digit:
        return ten + m // (ten * 10) * ten
    elif d == digit:
        return m % ten + 1 + m // (ten * 10) * ten
    else:
        return m // (ten * 10) * ten


def _cd(digit, m, ten=1):
    ret = 0
    for i in range(m + 1):
        if i // ten % 10 == digit:
            ret += 1
    return ret


def test_cd(ten=1):
    for digit in range(10):
        for i in range(1000):
            assert cd(digit, i, ten) == _cd(digit, i, ten)


def go(m, r, ten=1):
    k = [cd(digit, m, ten) for digit in range(10)]
    dp = [0] * 10
    dp[1] = 1

    for i in range(r):
        dp2 = [0] * 10
        for p in range(1, 10):
            for q in range(1, 10):
                pqten = p * q % 10
                dp2[pqten] = (dp2[pqten] + k[p] * dp[q]) % 1000000009
        dp = dp2
    return sum(ten * i * dp[i] for i in range(10)) % 1000000009


def solve(r, m):
    ret = 0
    ten = 1
    while ten <= m:
        ret += go(m, r, ten)
        ten *= 10
    return ret % 1000000009


print(solve(234567, 765432))
