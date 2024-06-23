def foo(v):
    sign = 1
    ret = 0
    for x in v:
        ret += x * sign
        sign *= -1
    return ret


def go(n, d, l):
    nplus = (n + 1) // 2
    nminus = n - nplus

    maxval = l * nplus - nminus
    minval = nplus - l * nminus
    if d < minval or d > maxval:
        return (-1,)

    ret = [1] * n
    for i in range(n):
        val = foo(ret)
        if val < d and i % 2 == 0:  # increase pozitive contributor
            ret[i] += min(l - 1, d - val)
        if val > d and i % 2 == 1:
            ret[i] += min(l - 1, val - d)
    return ret


print(" ".join(str(a) for a in go(*(int(x) for x in input().split(" ")))))
