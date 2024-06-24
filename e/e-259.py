from fractions import Fraction as Fr


def foo(i, j):
    ret = 0
    for k in range(i, j):
        ret = ret * 10 + k
    yield ret

    for mid in range(i + 1, j):
        for a in foo(i, mid):
            for b in foo(mid, j):
                yield a + b
                yield a - b
                if b != 0:
                    yield Fr(a, b)
                yield a * b


def go():
    v = set()
    for f in foo(1, 10):
        if type(f) == int:
            v.add(f)
        elif f.denominator == 1:
            v.add(int(f))
    return v


print(sum(x for x in go() if x > 0))
