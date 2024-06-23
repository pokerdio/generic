import color
exec(open("matrix.py").read())


def g(m, n):
    return (m ^ n) + (m | n) + (m & n)


def gg(m, n):
    gmn = g(m, n)
    bitz = len(bin(max(m, n, gmn))) - 2
    s = "{0:0%db}" % bitz

    print(s.format(m))
    print(s.format(n))
    print(s.format(m ^ n), "xor")
    print(s.format(m | n), "or")
    print(s.format(m & n), "and")

    print(s.format(gmn))


def G(N):
    s = 0
    for n in range(N + 1):
        for k in range(n + 1):
            s += g(k, n - k)
    return s


def G2(n):
    w = 1
    empty_max = 2 ** (n - 1)

    N = 2 ** n

    s = N * (N + 1) // 2

    ret = 0
    for i in range(n):
        ret += (s - (w * w * empty_max * (empty_max + 1) // 2)) * w * 2

        w = w * 2
        empty_max = empty_max // 2
    return ret


def foo(N, two):
    two = 2 ** two
    s = [["." for _ in range(N + 1)] for _ in range(N + 1)]
    for n in range(N + 1):
        for k in range(n + 1):
            s[n-k][k] = str(int((k | (n - k)) & two > 0))
    print("\n".join(("".join(line) for line in reversed(s))))


def p(lst):
    print(" ".join(str(x) for x in lst))


def ps(lst):
    lst2 = []
    s = 0
    for i in lst:
        s += i
        lst2.append(s)
    p(lst2)


def p2(lst):
    print(" " + "".join((color.OKGREEN if x >= 0 else color.OKWARN) + str(abs(x)) for x in lst) + color.ENDC)


def bar(N, two):
    two = 2 ** two
    ret = []
    for n in range(N + 1):
        s = 0
        for k in range(n + 1):
            s += (k | (n - k)) & two > 0
        ret.append(s)
    return ret


def delta(lst):
    ret = []
    for i in range(1, len(lst)):
        ret.append(lst[i] - lst[i - 1])
    return ret


def go(N, two):
    v = bar(N, two)
    foo(N, two)
    p(delta(v))
    p(v)
    ps(v)
    return sum(v)


v = [0, 0, 0, 1]
m1 = [[1, 1, 1, 0], [0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
m2 = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, -1, 2], [0, 0, 0, 1]]
m3 = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, -1, 1], [0, 0, 0, 1]]


def mulmm(m0, *mrest):
    for m in mrest:
        m0 = mulm(m0, m)
    return m0


def s(n, w):
    w2 = w+w
    v0 = v.copy()

    if n // w2 > 0:
        m = pow(m1, w)
        m = mulmm(m3, m, m2, m)
        m = pow(m, n // w2)
        v0 = mulv(m, v0)
#        print("A", v0)

    n = n % w2
    if n > 0:
        m = pow(m1, min(n, w))
        m = mulm(m2, m)
        v0 = mulv(m, v0)
#        print("B", v0)
    if n > w:
        m = pow(m1, n - w)
        v0 = mulv(m, v0)
#        print("C", v0)
    return v0[0]


def G3(n):
    n += 1
    w = 1
    ret = 0
    while w < n:
        ret += s(n, w) * w * 2
        w *= 2
    return ret


print(G3(10**18) % 1000000007)
