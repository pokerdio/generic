import primez
from prime_counting import pi as pc


def fibo(x, d=[0, 1]):
    for _ in range(x - len(d) + 1):
        d.append(d[-1] + d[-2])
    return d[x]


def _tri2(n):
    ret = 0
    while n > 0:
        ret += n
        n -= 2
    return ret


def tri2(n):
    count = n // 2 + 1
    s = n + n % 2
    return count * s // 2


def test_tri2():
    for i in range(1, 10100):
        assert tri2(i) == _tri2(i), i


def go(n):
    if n == 3:
        return 2
    if n == 4:
        return 3
    one = pc(n)
    even2 = n // 2 - 1
    odd2 = pc(n - 2) - 1
    three = n - 5
#    print(one, even2, odd2, three)
    return one + even2 + odd2 + tri2(three)


def solve(n=44):
    ret = 0
    for i in range(3, n + 1):
        ret += go(fibo(i))
    return ret


def foo2(n):
    s = set()
    for i in primez.iterate_primez(n + 1):
        for j in primez.iterate_primez(n + 1):
            if i + j <= n:
                s.add(i + j)

    return len(s)


def go2(n):
    one = pc(n)
    two = foo2(n)
    three = n - 5
    return one + two + tri2(three)
