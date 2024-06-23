from itertools import islice
from builtins import sum


def f(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return 2 * f(n // 2)
    n2 = n//2
    return n + 2 * f(n2) + f(n2) // n2


def g(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return g(n // 2)
    else:
        return 1 + g(n//2)


def ff(n):
    return g(n) * n


def f(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return 2 * f(n // 2)
    n2 = n//2
    return n + 2 * f(n2) + f(n2) // n2


def _s(n):
    ret = 0
    for i in range(1, n + 1):
        ret += f(i) ** 2
    return ret


def g(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return g(n // 2)
    else:
        return 1 + g(n//2)


def ff(n):
    return g(n) * n


def _sg_maker(xpow, gpow=1):
    def ret(segment, delta):
        if not delta:
            return 0
        ran = range(2 ** segment, 2 ** segment + min(2 ** segment, delta))
        return sum((g(x) ** gpow) * (x ** xpow) for x in ran)
    return ret


def _sum_by_two(base, count):
    ret = 0
    for plus in range(count):
        ret += base + 2 * plus
    return ret


def sum_by_two(base, count):
    # return (base + (base + delta * 2 - 2)) * count // 2
    return (base + count - 1) * count


# slow test versions of sums of g(x)*x**n functions over an interval of x
_sg0, _sg1, _sg2 = (_sg_maker(x) for x in range(5))
# slow test versions of sums of g(x)^2*x**n functions over an interval of x
_sgg0, _sgg1, _sgg2 = (_sg_maker(x, 2) for x in range(5))


def fix_interval(segment, delta):
    assert delta
    base = 2 ** segment
    assert(delta <= base)
    up = base + delta
    return up, base, delta


def memoize(f):
    d = {}

    def f2(*args):
        if args in d:
            return d[args]
        else:
            ret = f(*args)
            d[args] = ret
            return ret
    return f2


@memoize
def sg0(segment, delta):
    if not delta:
        return 0
    if segment < 3:
        return _sg0(segment, delta)

    up, base, delta = fix_interval(segment, delta)

    return (sg0(segment - 1, (delta + 1) // 2) +
            sg0(segment - 1, (delta // 2)) + delta // 2) % 1000000007


@memoize
def sgg0(segment, delta):
    """summing g**2 over an interval"""
    if segment < 3:
        return _sgg0(segment, delta)

    if not delta:
        return 0
    up, base, delta = fix_interval(segment, delta)

    # sum g(2i+1)**2 = sum((g(i)+1) **2)=sum(g2(i)+2g(i)+1)

    return (sgg0(segment - 1, (delta + 1) // 2) +
            sg0(segment - 1, (delta // 2)) * 2 +
            sgg0(segment - 1, (delta // 2)) +
            delta // 2) % 1000000007


@memoize
def sg1(segment, delta):
    if not delta:
        return 0
    if segment < 3:
        return _sg1(segment, delta)

    up, base, delta = fix_interval(segment, delta)

    evens = sg1(segment - 1, (delta + 1) // 2) * 2
    odds = sg1(segment - 1, (delta // 2)) * 2 + \
        sg0(segment - 1, (delta // 2)) + \
        sum_by_two(base + 1, delta // 2)
    return (evens + odds) % 1000000007


@memoize
def sgg1(segment, delta):
    """summing g(i)*g(i)*i"""
    if delta == 0:
        return 0
    if segment < 3:
        return _sgg1(segment, delta)

    up, base, delta = fix_interval(segment, delta)
    evens = sgg1(segment - 1, (delta + 1) // 2) * 2

    # odds
    # sum(g(2i+1)**2*(2i+1) ) = sum((g(i)+1)**2*(2i+1))=sum((g2(i)+2g(i)+1)*(2i+1))=
    # sum(2g2(i)i +4g(i)i+g2(i)+2g(i)+(2i+1) )
    odds = sgg1(segment - 1, (delta // 2)) * 2 + \
        sgg0(segment - 1, (delta // 2)) + \
        sg1(segment - 1, (delta // 2)) * 4 + \
        sg0(segment - 1, (delta // 2)) * 2 + \
        sum_by_two(base + 1, delta // 2)
    return (evens + odds) % 1000000007


def sum_odds_squared(n):
    "first n odds squared and summed"
    "n=3 sums 1**3+3**3+5**3"
    return n * (4 * n * n - 1) // 3


def sum_odds_squared_interval(base, count):
    assert base % 2
    return sum_odds_squared((base + 1) // 2 + count - 1) - sum_odds_squared(base // 2)


def _sum_odds_squared_interval(base, count):
    ret = 0
    for i in range(count):
        ret += (base + i * 2)**2
    return ret


@memoize
def sg2(segment, delta):
    if segment < 3:
        return _sg2(segment, delta)

    if not delta:
        return 0

    up, base, delta = fix_interval(segment, delta)

    evens = sg2(segment - 1, (delta + 1) // 2) * 4

#    sum(g(2n+1)*(2n+1)**2)
#    sum((g(n) + 1) * (4n2+4n+1))
    odds = sg0(segment - 1, (delta // 2)) + \
        sg1(segment - 1, (delta // 2)) * 4 + \
        sg2(segment - 1, (delta // 2)) * 4 + \
        sum_odds_squared_interval(base + 1, delta // 2)
    return (evens + odds) % 1000000007


@memoize
def sgg2(segment, delta=0):
    """summing g(x)*g(x)*x*x"""
    if segment < 3:
        return _sgg2(segment, delta)
    if not delta:
        return 0

    up, base, delta = fix_interval(segment, delta)

    evens = sgg2(segment - 1, (delta + 1) // 2) * 4

    # sum((g2(n)+2g(n) + 1) * (4n2+4n+1))
    odds = sg0(segment - 1, (delta // 2)) * 2 + \
        sg1(segment - 1, (delta // 2)) * 8 + \
        sg2(segment - 1, (delta // 2)) * 8 + \
        sgg0(segment - 1, (delta // 2)) + \
        sgg1(segment - 1, (delta // 2)) * 4 + \
        sgg2(segment - 1, (delta // 2)) * 4 + \
        sum_odds_squared_interval(base + 1, delta // 2)
    return (evens + odds) % 1000000007


def _sum_odd_pow(n, p):
    v = [1]
    for i in range(1, n):
        v.append(v[-1] + (i * 2 + 1) ** p)
    return v


def go(n):
    two = 1
    i = 0
    ret = 0

    while n > 0:
        #        print("adding sgg2", i, min(n, two))
        add = sgg2(i, min(n, two))
        #print(add, _sgg2(i, min(n, two)) % 1000000007)
        ret += add
        n -= two
        two *= 2
        i += 1
    return ret % 1000000007


def foo():
    for i in range(1, 100):
        print(i, go(i) - _s(i))


.
