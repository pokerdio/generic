from itertools import islice
from builtins import sum


def makerecdec():
    data = [0]
    verbose = [1]
    global logpush, logpop

    def logpush(n):
        verbose.append(n)

    def logpop():
        verbose.pop()
        if not verbose:
            verbose.append(0)

    def recdec(f):
        def f2(*args):
            str_args = str(args).strip("(),")
            if verbose[-1]:
                print(" > " * data[0], f"f({str_args})")
            data[0] += 1
            ret = f(*args)
            data[0] -= 1
            if verbose[-1]:
                print(" < " * data[0], f"f({str_args})={ret}")
            return ret
        return f2
    return recdec


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
    def ret(n):
        ran = range(1, n + 1)
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
_sg0, _sg1, _sg2 = (_sg_maker(x) for x in range(3))
# slow test versions of sums of g(x)^2*x**n functions over an interval of x
_sgg0, _sgg1, _sgg2 = (_sg_maker(x, 2) for x in range(3))


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
def sg0(n):
    if n < 3:
        return _sg0(n)
    return (1 + sg0(n // 2) +
            sg0((n - 1) // 2) + (n - 1) // 2) % 1000000007


def test(n, f1, f2):
    for i in range(1, n + 1):
        assert f1(i) % 1000000007 == f2(i) % 1000000007, i


test(500, sg0, _sg0)


@memoize
def sgg0(n):
    """summing g**2 over an interval"""
    if n < 3:
        return _sgg0(n)

    # sum g(2i+1)**2 = sum((g(i)+1) **2)=sum(g2(i)+2g(i)+1)

    return (1 + sgg0(n // 2) + sg0((n - 1) // 2) * 2 +
            sgg0((n - 1) // 2) + (n-1) // 2) % 1000000007


test(500, sgg0, _sgg0)


@ memoize
def sg1(n):
    if n < 3:
        return _sg1(n)

    evens = sg1(n // 2) * 2

    odds = sg1((n - 1) // 2) * 2 + sg0((n - 1) // 2) + sum_by_two(3, (n - 1) // 2)
    return (1 + evens + odds) % 1000000007


test(500, sg1, _sg1)


@ memoize
def sgg1(n):
    """summing g(i)*g(i)*i"""
    if n < 3:
        return _sgg1(n)

    evens = sgg1(n // 2) * 2

    # odds
    # sum(g(2i+1)**2*(2i+1) ) = sum((g(i)+1)**2*(2i+1))=sum((g2(i)+2g(i)+1)*(2i+1))=
    # sum(2g2(i)i +4g(i)i+g2(i)+2g(i)+(2i+1) )
    odds = sgg1((n - 1) // 2) * 2 + sgg0((n - 1) // 2) + \
        sg1((n - 1) // 2) * 4 + sg0((n - 1) // 2) * 2 + \
        sum_by_two(3, (n - 1) // 2)
    return (1 + evens + odds) % 1000000007


test(500, sgg1, _sgg1)


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


@ memoize
def sg2(n):
    if n < 3:
        return _sg2(n)

    evens = sg2(n // 2) * 4

#    sum(g(2n+1)*(2n+1)**2)
#    sum((g(n) + 1) * (4n2+4n+1))
    odds = sg0((n - 1) // 2) + sg1((n - 1) // 2) * 4 + \
        sg2((n - 1) // 2) * 4 + sum_odds_squared_interval(3, (n - 1) // 2)
    return (1 + evens + odds) % 1000000007


test(500, sg2, _sg2)


@ memoize
def sgg2(n):
    """summing g(x)*g(x)*x*x"""
    if n < 3:
        return _sgg2(n)
    evens = sgg2(n // 2) * 4

    # sum((g2(n)+2g(n) + 1) * (4n2+4n+1))
    odds = sg0(((n - 1) // 2)) * 2 + sg1(((n - 1) // 2)) * 8 + sg2(((n - 1) // 2)) * 8 + \
        sgg0(((n - 1) // 2)) + sgg1(((n - 1) // 2)) * 4 + sgg2(((n - 1) // 2)) * 4 + \
        sum_odds_squared_interval(3, (n - 1) // 2)
    return (1 + evens + odds) % 1000000007


test(500, sgg2, _sgg2)


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
        # print(add, _sgg2(i, min(n, two)) % 1000000007)
        ret += add
        n -= two
        two *= 2
        i += 1
    return ret % 1000000007


def foo():
    for i in range(1, 100):
        print(i, go(i) - _s(i))
