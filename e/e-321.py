def start(n):
    return "R" * n + " " + "B" * n


def end(n):
    return "B" * n + " " + "R" * n


def expand(p):
    a, b = p.split(" ")
    if a:
        yield a[:-1] + " " + a[-1] + b
    if len(a) >= 2:
        yield a[:-2] + " " + a[-1] + a[-2] + b
    if b:
        yield a + b[0] + " " + b[1:]
    if len(b) >= 2:
        yield a + b[1] + b[0] + " " + b[2:]


def expand2(p):
    a, b = p.split(" ")
    if a and a[-1] == "R":
        yield a[:-1] + " " + a[-1] + b
    if len(a) >= 2 and a[-2] == "R":
        yield a[:-2] + " " + a[-1] + a[-2] + b
    if b and b[0] == "B":
        yield a + b[0] + " " + b[1:]
    if len(b) >= 2 and b[1] == "B":
        yield a + b[1] + b[0] + " " + b[2:]


def go(n):
    opened = set([start(n)])
    closed = set()
    win = end(n)

    for k in range(1, 150000):
        newstuff = set()
        for p in opened:
            for x in expand(p):
                if x == win:
                    return k, len(closed) + len(newstuff) + len(opened)
                if x not in opened and x not in closed:
                    newstuff.add(x)
        closed.update(opened)
        opened = newstuff


def go2(n):
    opened = set([start(n)])
    closed = set()
    win = end(n)

    for k in range(1, 150000):
        newstuff = set()
        for p in opened:
            for x in expand2(p):
                if x == win:
                    return k, len(closed) + len(newstuff) + len(opened)
                if x not in opened and x not in closed:
                    newstuff.add(x)
        closed.update(opened)
        opened = newstuff


# go2 is a bit faster by requiring R to go -> and B to go <-

# running go2 guess that the number we're after is n*(n+2)


def solve(n=100000):
    triangles = set(x * (x + 1) // 2 for x in range(1, n))
    ret = []
    for i in range(1, n):
        k = i * (i + 2)
        if k in triangles:
            ret.append(i)
            if len(ret) == 40:
                return ret
    return ret


def solve2(n=100000):
    for i in range(1, n):
        k = i * (i + 2)
        q = int(math.sqrt(k * 2))
        if q * (q + 1) // 2 == k:
            yield i, q


# cheating


v = [2, 5, 15, 32, 90, 189, 527, 1104, 3074, 6437, 17919, 37520,
     104442, 218685, 608735, 1274592, 3547970, 7428869, 20679087,
     43298624, 120526554, 252362877, 702480239, 1470878640, 4094354882,
     8572908965, 23863649055, 49966575152, 139087539450, 291226541949,
     810661587647, 1697392676544, 4724881986434, 9893129517317, 27538630330959,
     57661384427360, 160506899999322, 336075177046845, 935502769664975, 1958789677853712]


v2 = [int(math.sqrt(x * (x + 1) // 2)) for x in v]


def foo(q):
    m = q * (q + 1) // 2 + 1
    m2 = int(math.sqrt(m))
    while m2 * m2 < m:
        m2 += 1
    assert(m2 * m2 == m)
    return m2 - 1


v3 = [foo(x) for x in v]
