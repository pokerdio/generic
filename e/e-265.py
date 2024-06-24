def code(v):
    two = 1
    ret = 0
    for i in v[::-1]:
        if i:
            ret += two
        two *= 2
    #print(ret, v)
    return ret


def go(s, v, n, digitz):
    if digitz == 0:
        for i in range(1, n):
            if (*v[-i:], *v[:n - i]) in s:
                return 0

        return code(v)

    ret = 0

    n1 = v[-n + 1:]
    one = (*n1, 1)
    zero = (*n1, 0)

    for i in (one, zero):
        if i not in s:
            s.add(i)
            ret += go(s, v + i[-1:], n, digitz - 1)
            s.remove(i)
    return ret


def solve(n):
    return go(set(((0,) * n,)), (0,) * n, n, 2**n - n)


print(solve(5))
