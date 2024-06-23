def naive(n):
    ret = 0
    for i in range(1, n + 1):
        val = i * i * (n // i)
        ret += val
        print(val, ret)
    return ret


def go(n):
    i = 1
    ret = 0
    lasti = 1
    while i <= n:
        if lasti // 1000000 != i // 1000000:
            print(i)
        lasti = i
        p, r = n // i, n % i
        if p < r and i < n:
            j = min(n - i, r // p)
            ret += (j + 1) * i * i * p
            ret += i * j * (j + 1) * p
            ret += j * (j + 1) * (2 * j + 1) * p // 6

            ret %= 1000000000
            i += j + 1
        else:
            ret = (ret + (n // i) * i * i) % 1000000000
            i += 1
    return ret
