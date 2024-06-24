from matrix import *


def fact(n):
    ret = 1
    for i in range(2, n + 1):
        ret *= i
    return ret


def fibo(n, mod=fact(15)):
    # small' = big
    # big' = small + big

    matrix = [[0, 1], [1, 1]]
    v = [1, 1]
    if n < 2:
        return max(0, n)
    return mulv(pow(matrix, n - 1, mod), v, mod)[0]


def F(n, x, mod=fact(15)):
    # val2 = val * x + big
    # big = smol
    # smol = big - smol
    matrix = [[x, 0, 1], [0, 0, 1], [0, 1, -1]]
    v = [fibo(n), fibo(n), fibo(n - 1)]
    return mulv(pow(matrix, n, mod), v, mod)[0]


def go():
    return sum(F(10**15, i) for i in range(101)) % (fact(15))
