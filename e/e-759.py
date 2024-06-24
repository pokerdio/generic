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


def pf(n):
    for i in range(1, n + 1):
        fi = f(i)
#        print(i, fi // i, fi)
        yield(fi // i)


def foo(n):
    g = pf(2 ** n)

    for i in range(n):
        j = 2 ** i
        print(list(islice(g, j)))


def bar(n):
    v = [1]
    for i in range(1, n):
        v = v + [x + 1 for x in v]
        print(v)


def ptri_step(count):
    count = count + [0]
    count = [0] + [count[i] + count[i + 1] for i in range(len(count) - 1)]
    return count


def two_below(n):
    i = 0
    j = 1
    while j * 2 <= n:
        i += 1
        j *= 2
    return i, j


def ptri(n, d={1: [0, 1]}):
    """pascal triangle count"""
    if n in d:
        return d[n]
    d[n] = ptri_step(ptri(n - 1))
    return d[n]


def subtri(n):
    if n == 0:
        return []
    i, j = two_below(n)
    return sum_counts(ptri(i + 1), [0] + subtri(n - j))


def s(n):
    c = subtri(n)
    ret = 0
    for i in range(len(c)):
        ret += i * i * c[i]
    return ret


def sum_counts(c1, c2):
    if len(c1) > len(c2):
        c1, c2 = c2, c1

    c = c2.copy()
    for i in range(len(c1)):
        c[i] += c1[i]
    return c

# s = S(i**4 * ff(i))


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


def _sg_maker(xpow):
    def ret(segment, delta=0):
        if delta == 0:
            delta = 2 ** segment
        ran = range(2 ** segment, 2 ** segment + min(2 ** segment, delta))
        return sum(g(x) * x ** xpow for x in ran)
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
_sg0, _sg1, _sg2, _sg3, _sg4 = (_sg_maker(x) for x in range(5))


def fix_interval(segment, delta):
    base = 2 ** segment
    if not delta:
        up = base * 2
        delta = up - base
    else:
        assert(delta <= base)
        up = base + delta
    return up, base, delta


def sg0(segment, delta=0):
    if segment < 3:
        return _sg0(segment, delta)

    up, base, delta = fix_interval(segment, delta)

    return sg0(segment - 1, (delta + 1) // 2) + \
        sg0(segment - 1, (delta // 2)) + delta // 2


# @makerecdec()
def sg1(segment, delta=0):
    if segment < 3:
        return _sg1(segment, delta)

    up, base, delta = fix_interval(segment, delta)

    evens = sg1(segment - 1, (delta + 1) // 2) * 2
    odds = sg1(segment - 1, (delta // 2)) * 2 + \
        sg0(segment - 1, (delta // 2)) + \
        sum_by_two(base + 1, delta // 2)
    return evens + odds


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


def sg2(segment, delta=0):
    if segment < 3:
        return _sg2(segment, delta)
    up, base, delta = fix_interval(segment, delta)

    evens = sg2(segment - 1, (delta + 1) // 2) * 4

#    sum(g(2n+1)*(2n+1)**2)
#    sum((g(n) + 1) * (4n2+4n+1))
    odds = sg0(segment - 1, (delta // 2)) + \
        sg1(segment - 1, (delta // 2)) * 4 + \
        sg2(segment - 1, (delta // 2)) * 4 + \
        sum_odds_squared_interval(base + 1, delta // 2)
    return evens + odds


def sum_odds_cubed(n):
    "first n odds cubed and summed"
    "n=3 sums 1**3+3**3+5**3"
    return n * n * (2 * n * n - 1)


def sum_odds_cubed_interval(base, count):
    assert base % 2
    return sum_odds_cubed((base + 1) // 2 + count - 1) - sum_odds_cubed(base // 2)


def _sum_odds_cubed_interval(base, count):
    ret = 0
    for i in range(count):
        ret += (base + i * 2)**3
    return ret


def sg3(segment, delta=0):
    if segment < 3:
        return _sg3(segment, delta)
    up, base, delta = fix_interval(segment, delta)

    evens = sg3(segment - 1, (delta + 1) // 2) * 8

#    sum(g(2n+1)*(2n+1)**3)
#    sum((g(n) + 1) * (8n3+12n2+6n+1))

    odds = sg0(segment - 1, (delta // 2)) + \
        sg1(segment - 1, (delta // 2)) * 6 + \
        sg2(segment - 1, (delta // 2)) * 12 + \
        sg3(segment - 1, (delta // 2)) * 8 + \
        sum_odds_cubed_interval(base + 1, delta // 2)
    return evens + odds


def _sum_odd_pow(n, p):
    v = [1]
    for i in range(1, n):
        v.append(v[-1] + (i * 2 + 1) ** p)
    return v


def sum_odds_quadded(n):
    "first n odds squared squared and summed"
    "n=3 sums 1**3+3**3+5**3"
    return (48*n ** 5 - 40*n ** 3 + 7*n)//15


def sum_odds_quadded_interval(base, count):
    assert base % 2
    return sum_odds_quadded((base + 1) // 2 + count - 1) - sum_odds_quadded(base // 2)


def _sum_odds_quadded_interval(base, count):
    ret = 0
    for i in range(count):
        ret += (base + i * 2)**4
    return ret


def sg4(segment, delta=0):
    if segment < 3:
        return _sg4(segment, delta)
    up, base, delta = fix_interval(segment, delta)

    evens = sg4(segment - 1, (delta + 1) // 2) * 16

#    sum(g(2n+1)*(2n+1)**4)
#    sum((g(n) + 1) * (8n3+12n2+6n+1)*(2n+1))
#    sum((g(n) + 1) * (8n3+12n2+6n+1 + 16n4+24n3+12n2+2n))
#    sum((g(n) + 1) * (16n4+ 32n3+24n2+8n+1))

    odds = sg0(segment - 1, (delta // 2)) + \
        sg1(segment - 1, (delta // 2)) * 8 + \
        sg2(segment - 1, (delta // 2)) * 24 + \
        sg3(segment - 1, (delta // 2)) * 32 + \
        sg4(segment - 1, (delta // 2)) * 16 + \
        sum_odds_quadded_interval(base + 1, delta // 2)
    return evens + odds
