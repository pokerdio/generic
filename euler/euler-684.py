import matrix


def ess(n):
    ret = 0
    ten = 1
    while n >= 9:
        n -= 9
        ret = ret * 10 + 9
        ten = ten * 10
    return ret + ten * n


def ess2(n, mod=1000000007):
    if n < 9:
        return ess(n)
    v = [0, 1, 1]
    m = [[10, 0, 9], [0, 10, 0], [0, 0, 1]]
    ret, ten, _ = matrix.mul(matrix.pow(m, n // 9, mod), v, mod)
    return (ret + ten * (n % 9)) % mod


def S(n):
    ret = 0
    for i in range(1, n + 1):
        ret += ess2(i)
    return ret


def f(n, data=[0, 1]):
    if len(data) <= n:
        for i in range(len(data), n + 1):
            data.append(data[-1] + data[-2])
    return data[n]


def S2(n):
    ret = 0
    s = 45
    for _ in range(0, n // 9):
        ret = ret + s
        s = s * 10 + 81
    return ret


def S3(n, mod=1000000007):
    if n < 9:
        return S(n)
    v = [0, 45, 1]
    m = [[1, 1, 0], [0, 10, 81], [0, 0, 1]]

    m2 = matrix.pow(m, n // 9, mod)
    ret, _, _ = matrix.mul(m2, v, mod)

    for i in range(n // 9 * 9 + 1, n + 1):
        ret += ess2(i)

    return ret % mod


def go():
    s = 0
    for i in range(2, 91):
        print(i)
        s += S3(f(i))
    return s % 1000000007
