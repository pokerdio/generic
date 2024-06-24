# project euler problem 109

from itertools import count, islice


def rev(n):
    ret = 0
    while n:
        ret = ret * 10 + n % 10
        n //= 10
    return ret


def rev2(n):
    return int("".join(reversed(str(n))))


def go(n=10**9):
    odd = set("13579")
    k = 0
    for i in range(1, n + 1):
        if i % 10 > 0:
            if set(str(i + rev(i))) <= odd:
                k += 1
        if i % 250000 == 0:
            print(i)
    return k
