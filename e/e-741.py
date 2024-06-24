def gen1d(n):
    for i in range(n - 1):
        for j in range(i + 1, n):
            yield (0,) * i + (1,) + (0,) * (j - i - 1) + (1,) + (n - j - 1) * (0,)


def go(n, lvl=0, rows=()):
    sum = [0] * n
    for row in rows:
        sum = [sum[i] + row[i] for i in range(n)]
    for row in gen1d(n):
        ok = True
        for i in range(n):
            if sum[i] + row[i] > 2:
                ok = False
                break
        if not ok:
            continue
        newrows = rows + (row,)
        if lvl + 1 == n:
            yield newrows
        else:
            yield from go(n, lvl + 1, newrows)


def rot(rows):
    n = len(rows)
    return tuple(tuple(rows[i][j] for i in range(n - 1, -1, -1)) for j in range(n))


def mir(rows):
    return rows[::-1]


def mirv(rows):
    return tuple(x[::-1] for x in rows)


def diag1(rows):
    return tuple(tuple(x[y] for x in rows) for y in range(len(rows)))


def diag1(rows):
    n = len(rows)
    return tuple(tuple(rows[x][y] for x in range(n)) for y in range(n))


def diag2(rows):
    n = len(rows)
    return tuple(tuple(rows[n - 1 - x][n - 1 - y] for x in range(n)) for y in range(n))


def variant(rows):
    r = rows
    for i in range(3):
        r = rot(r)
        yield r
    r = mir(rows)
    yield r
    for i in range(3):
        r = rot(r)
        yield r

    r = diag1(rows)
    yield r
    for i in range(3):
        r = rot(r)
        yield r

    r = diag2(rows)
    yield r
    for i in range(3):
        r = rot(r)
        yield r


def filter_var(gen, k=-1):
    g = {}
    for x in gen:
        ok = True
        for v in variant(x):
            if v in g:
                ok = False
                g[v] += 1
                break
        if ok:
            g[x] = 1
    if k < 0:
        return g
    else:
        return [x for x, y in g.items() if y == k]


def filter_pp(gen):
    d = filter_var(gen)
    dk = list(d.keys())
    for i in range(len(dk)):
        pp(dk[i], (i, d[dk[i]]))


def filter_stats(gen):
    d = filter_var(gen)
    dk = list(d.keys())

    stats = {}
    for i in range(len(dk)):
        x = dk[i]
        s = (x == mir(x) and "MH " or "") + (x == mirv(x) and "MV " or "") + \
            (x == diag1(x) and "D1 " or "") + (x == diag2(x) and "D2 " or "") + \
            ((x == mir(x) and x == mirv(x)) and "MM " or "") + \
            (x == rot(rot(x)) and "R180 " or "") + \
            (x == rot(x) and "R90 " or "") + str(d[x])
        stats[s] = stats.get(s, 0) + 1
    return stats


def pp(x, postfix=""):
    for line in x:
        print("".join(i and "*" or "." for i in line))
    print((x == mir(x) and "MH " or "") +
          (x == mirv(x) and "MV " or "") +
          (x == diag1(x) and "D1 " or "") +
          (x == diag2(x) and "D2 " or "") +
          ((x == mir(x) and x == mirv(x)) and "MM " or "") +
          (x == rot(rot(x)) and "R180 " or "") +
          (x == rot(x) and "R90 " or "") + str(postfix))
    print()


def R(g):
    n = len(g)
    for i in range(n):
        for j in range(n):
            if g[i][j] != g[j][i]:
                return False
    return True


def go_mirror(n, verbose=False):
    ret = 0
    for rows in go(n):
        if rows == mir(rows):
            if verbose:
                pp(rows)
            ret += 1
    return ret


def go_mirrorv(n, verbose=False):
    ret = 0
    for rows in go(n):
        if rows == mirv(rows):
            if verbose:
                pp(rows)
            ret += 1
    return ret


def go_mirrorhv(n, verbose=False):
    ret = 0
    for rows in go(n):
        if rows == mirv(rows) and rows == mir(rows):
            if verbose:
                pp(rows)
            ret += 1
    return ret


def go_rot180(n, verbose=False):
    ret = 0
    for rows in go(n):
        if rows == rot(rot(rows)):
            if verbose:
                pp(rows)
            ret += 1
    return ret


def go_rot180_2(n, verbose=False):
    ret = 0
    for rows in go(n):
        if rows == mir(mirv(rows)):
            if verbose:
                pp(rows)
            ret += 1
    return ret


def go_rot(n, verbose=False):
    ret = 0
    for rows in go(n):
        if rows == rot(rows):
            if verbose:
                pp(rows)
            ret += 1
    return ret


# [len(filter_var(go(i))) for i in range(1, 8)]
# [0, 1, 2, 20, 288, 8791, 390816]

# [len(list(go(i))) for i in range(1, 7)]
# [0, 1, 6, 90, 2040, 67950]


def pg(g, max_count=8):
    for rows, count in g.items():
        if count <= max_count:
            for row in rows[:-1]:
                print("".join(str(x) for x in row))
            print("".join(str(x) for x in rows[-1]), count, "\n")


def statsg(g):
    g2 = {}
    for i, k in g.items():
        g2[k] = g2.get(k, 0) + 1
    return g2


# alll
# h(n) ways to paint a virgin n * n square
# g(n) ways to paint a n lines n+1 columns with two columns already +1
# h(n) = c(2,n) * g(n - 1)
# g(n) = n * h(n - 1)  +  n * (n - 1) * g(n - 1)

def All(n):
    h = [0, 0]
    g = [0, 1]

    for i in range(2, n + 1):
        g.append(i * h[i - 1] + i * (i - 1) * g[i - 1])
        h.append(i * (i - 1) // 2 * g[i - 1])
    return h[-1]


# mirror horiz AND mirror vert
# must even
#

def MM(n):
    if n % 2:
        return 0

    n = n // 2
    return fact(n)


def fact(n, data=[1, 1]):
    while len(data) <= n:
        data.append(data[-1] * len(data))
    return data[n]


# MIRROR H OR V
# has to even

def Mirror(n, data=[0, 1]):
    if n % 2:
        return 0

    n2 = n // 2
    while len(data) <= n2:
        data.append(data[-1] * len(data) * (len(data) * 2 - 1))
    return data[n // 2]


# double rot or double mirror
# different from MM in that a MM mirrors H and a MM independently mirrors V
# whereas a double mirror can not mirror H alone, or V alone, but only must HV
# also a double rot may not rotate 90% but only 180%

# if even; n is the half (no of lines to fill in of the top half)
# h(n)=n * h(n- 1) + n * (n - 1) // 2 * 4 * g (n - 1)
# g(n) = 4 * n * h(n - 1) + 2 * n * 2 * (n - 1) * g(n - 1)

# if odd: the board is 2 * n + 1
# f(n) = n * n * 2 * h(n - 1) + n * n * (n - 1) * 2 * g(n - 1)

def Rot180(n):
    n2 = n // 2
    h = [0, 1]
    g = [0, 4]
    f = [0, 2]

    for i in range(2, n2 + 1):
        h.append(i * h[i - 1] + i * (i - 1) * 2 * g[i - 1])
        g.append(4 * i * h[i - 1] + 2 * i * 2 * (i - 1) * g[i - 1])
        f.append(i * i * 2 * h[i - 1] + i * i * (i - 1) * 2 * g[i - 1])
    return n % 2 and f[n2] or h[n2]


# go_rot180(6) 534
# go_rot180(7) 1764

# go_rot(7) 0
# go_rot(6) 12
# go_rot(4) 2

# g(n) = 2*h(n-2) + (2n-4) * g(n - 1)
# h(n) = h(n - 1) + (n - 1) * h(n - 2) + ((2n-2)(2n-3)/2 - (n - 1))


def Rot90(n):
    if n % 2:
        return 0
    n2 = n // 2
    h = [1, 1]
    g = [0, 1]

    for i in range(2, n2 + 1):
        h.append(h[i - 1] + (i - 1) * h[i - 2] +
                 ((2 * i - 2) * (2 * i - 3) // 2 - i + 1) * g[i - 1])
        g.append(2 * h[i - 2] + (2 * i - 4) * g[i - 1])
    return h[-1]


def solve(n):
    a = All(n)
    mm = MM(n)
    m = Mirror(n)
    r180 = Rot180(n)
    r90 = Rot90(n)

    print("a", a, "mm", mm, "m", m, "r180", r180, "r90", r90)

    ret = 0
    print("(a - r180 - 2 * m + 2 * mm)//8   ", (a - r180 - 2 * m + 2 * mm),
          (a - r180 - 2 * m + 2 * mm) % 8, (a - r180 - 2 * m + 2 * mm) // 8)

    ret += (a - r180 - 2 * m + 2 * mm) // 8
    print("(r180 - r90)//4   ", (r180 - r90), (r180 - r90) % 4,
          (r180 - r90) // 4)

    ret += (r180 - r90) // 4
    print("r90 - mm//2    ", r90 - mm, (r90 - mm) // 2)
    ret += (r90 - mm) // 2
    ret += mm
    print("m - mm", m - mm)
    ret += (m - mm) * 2 // 2

    return ret


# v6 and v7 are filter_var(go(6)) and 7
# len(v7) checks out
