import sys

input = sys.stdin.readline


def gen_input():
    while True:
        yield [int(c) for c in input().split()]


def gen_fake():
    yield [5, 1, 3, 4]


def ints(g=gen_input()):
    return next(g)


k2, k3, k5, k6 = ints()

k256 = min(k2, k5, k6)
k2 -= k256
k5 -= k256
k6 -= k256

k32 = min(k2, k3)


print(k32 * 32 + k256 * 256)
