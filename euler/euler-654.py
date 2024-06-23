import numpy
import sys


def triangle(n):
    return [[1] * (n - x) + [0] * x for x in range(n)]


def randmatrix(n):
    return numpy.array([[randint(1, 10) for _ in range(n)] for _ in range(n)])


def pow(matrix, n, mod=None):
    v = []
    while n > 0:
        print(n)
        if n % 2 == 0:
            n //= 2
            matrix = matrix.dot(matrix)
            if mod:
                matrix %= mod
        else:
            v.append(matrix)
            n -= 1
    for i in range(1, len(v)):
        v[0] = v[0].dot(v[i])
        if mod:
            v[0] %= mod
    return v[0]


def T(n, m, mod=None):
    a = numpy.array([1] * (n - 1))
    matrix = numpy.array(triangle(n - 1))
    matrix = pow(matrix, m - 1, mod)
    ret = sum(a.dot(matrix))
    return ret % mod if mod else ret
