from primez import iterate_primez as itp


def expand(s, m, n):
    space = s.find("S")
    l = len(s)

    if space + m < l:
        yield(s[:space] + s[space + m] + s[space + 1:space + m] + "S" + s[space + m + 1:])

    if space - m >= 0:
        yield(s[:space - m] + "S" + s[space - m + 1:space] + s[space - m] + s[space + 1:])

    if space % m > 0:
        yield s[:space - 1] + s[space] + s[space - 1] + s[space + 1:]
    if space % m < m - 1:
        yield s[:space] + s[space + 1] + s[space] + s[space + 2:]


def sprint(s, m, n):
    for i in range(n):
        print(s[i * m: (i + 1) * m])
    print()


# def foo(s, m, n):
#     sprint(s, m, n)
#     print("=>\n")
#     [sprint(x, 5, 4) for x in expand(s, 5, 4)]


def go(m, n):
    start = "R" + "b" * (m * n - 2) + "S"

    father = {}

    v = [start]
    vis = set((start,))

    k = 1
    while v:
        v2 = []

        for i in v:
            for i2 in expand(i, m, n):
                if i2 not in vis:
                    father[i2] = i
                    vis.add(i2)
                    v2.append(i2)
                    if i2[-1] == "R":
                        # seq = [i2]
                        # while seq[-1] in father:
                        #     seq.append(father[seq[-1]])
                        # i = 0
                        # for x in reversed(seq):
                        #     i += 1
                        #     print(i)
                        #     sprint(x, m, n)

                        return k
        v = v2
        k += 1


def foo(m, n):
    m, n = min(m, n), max(m, n)

    if m < n:
        one = m - 1 + n - 1
        two = 3 * (2 * m - 2)
        three = 5 * (n - m - 1)
    if m == n:
        one = m - 1 + n - 1
        two = 3 * (2 * m - 3)
        three = 0
    return one + two + three


def foo2(m, n):
    m, n = min(m, n), max(m, n)

    if m < n:
        return 2 * m + 6 * n - 13
    if m == n:
        return 8 * m - 11


def test():
    for i in range(2, 11):
        for j in range(2, 11):
            assert(foo(i, j) == go(i, j))
    for i in range(2, 111):
        for j in range(2, 111):
            assert(foo(i, j) == foo2(i, j))


def foobar(n=10**6):
    ret = 0
    it = itp(n)
    next(it)
    for p in it:
        if (p * p + 11) % 8 == 0:
            print("weird")
            ret += 1

        x = (p * p + 13) // 2
        minn = x // 4 + 1
        maxn = (x - 2) // 3
        ret += (maxn - minn + 1) * 2
    return ret
