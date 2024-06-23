import sys

input = sys.stdin.readline


def gen_input():
    while True:
        yield [int(c) for c in input().split()]


def gen_fake():
    yield 666,


def ints(g=gen_fake()):
    return next(g)


test_count, = ints()
# all coords will be 0 inclusive, the 1 based input will need conversion


def poz(x, y):
    return x * 16 + y


def pozxy(poz):
    return poz // 16, poz % 16


def pair_code(x, y, x2, y2):
    return x * 4096 + y * 256 + x2 * 16 + y2


def pair_decode(code):
    ret = []
    for _ in range(4):
        ret.insert(0, code % 16)
        code //= 16
    return ret


def foo(n, m, x, y):
    ret = {}
    for x1 in range(n - 1):
        for x2 in range(x1+1, n):
            for y1 in range(m - 1):
                for y2 in range(y1+1, m):
                    code = pair_code(x1, y1, x2, y2)
                    md = abs(x1 - x) + abs(x2 - x) + abs(y1 - y) + abs(y2 - y)
                    ret[md] = ret.get(md, 0) + 1  # md: manhattan distance
    return ret, max(ret.values())


def best(n, m):
    best = (0, 0)
    best_val = 999
    for x in range((n + 1) // 2 + 1):
        for y in range((m + 1) // 2 + 1):
            _, val = foo(n, m, x, y)
            print(x, y, val)
            if val < best_val:
                best_val = val
                best = (x, y)
    return best, best_val


def genpairs(n, m, manh_dist):
    for x1 in range(n - 1):
        for x2 in range(x1+1, n):

            for y1 in range(m - 1):
                for y2 in range(y1+1, m):
                    pass
