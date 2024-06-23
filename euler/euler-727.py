def sig(n):
    one, two, three = 1, 2, 1
    ret = 0
    while one <= 16384:
        ret = ret + ((one & n > 0) + (two & n > 0)) * three
        one, two, three = two, two * 2, three * 3
    return ret


def p(n, b=2):
    s = ""
    while n > 0:
        s += str(n % b)
        n //= b
    return s[::-1]


def foo():
    ret = {}
    for i in range(2 ** 16):
        s = sig(i)
        if s == 7174453:
            print(i)
        if s in ret:
            ret[s].append(i)
        else:
            ret[s] = [i]
    return ret
