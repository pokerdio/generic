import itertools as it
s = """4 6
2S 3S 4S 7S 8S AS
5H 6H 7H 5S TC AC
8H 9H TH 7C 8C 9C
2D 2C 3C 4C 5C 6C"""


# s = """4 6
# 2S 3S 4S 7S 8S AS
# 5H 6H 7H J1 TC AC
# 8H 9H TH 7C 8C 9C
# 2D 2C 3C 4C 5C 6C"""


# s = """4 6
# 2S 3S 4S 7S 8S AS
# 5H 6H 7H QC TC AC
# 8H 9H TH 7C 8C 9C
# 2D 2C 3C 4C 5C 6C"""


s = """6 3
7C 8C 9C
TC 2C 3C
QC 5C J1
2D 3D 4D
5D J2 6D
7D AD KS"""


def input_iterator():
    while True:
        yield input()


def s_iterator(s=s):
    for line in s.split("\n"):
        yield line


def get(f=s_iterator()):
    n, m = (int(x) for x in next(f).split())
    return [next(f).split() for _ in range(n)]


def good_square(v, i, j):
    s0, s1 = set(), set()
    for x in range(3):
        for y in range(3):
            s = v[i + y][j + x]
            s0.add(s[0])
            s1.add(s[1])
    return len(s0) == 9 or len(s1) == 1


def good_grid(v):
    good = []
    for r in range(len(v) - 2):
        for c in range(len(v[0]) - 2):
            if good_square(v, r, c):
                good.append((r, c))

    for j in range(1, len(good)):
        rj, cj = good[j]
        for i in range(j):
            ri, ci = good[i]
            if abs(ri - rj) >= 3 or abs(ci - cj) >= 3:
                return ((ri, ci), (rj, cj))


def deck():
    for rank in "23456789TJQKA":
        for suit in "CDHS":
            yield rank + suit


def gen_repl(j1, j2, rem):
    ret = set()
    for joker1 in rem:
        for joker2 in rem:
            if joker1 != joker2:
                value = []
                if j1:
                    value.append(("J1", joker1))
                if j2:
                    value.append(("J2", joker2))
                ret.add(tuple(value))
    return ret


def go(v):
    s = set(it.chain(*v))
    rem = set(deck()) - s
    j1, j2 = "J1" in s, "J2" in s

    for repl in gen_repl(j1, j2, rem):
        v2 = [vv.copy() for vv in v]
        for vv in v2:
            for joker, replacement in repl:
                if joker in vv:
                    vv[vv.index(joker)] = replacement
        if good_grid(v2):
            print("Solution exists.")
            d = dict(repl)
            if j1 and j2:
                print("Replace J1 with " + d["J1"] + " and J2 with " + d["J2"] + ".")
            elif j1:
                print("Replace J1 with " + d["J1"] + ".")
            elif j2:
                print("Replace J2 with " + d["J2"] + ".")
            else:
                print("There are no jokers.")
            rc1, rc2 = good_grid(v2)
            print("Put the first square to (%d, %d)." % (rc1[0] + 1, rc1[1] + 1))
            print("Put the second square to (%d, %d)." % (rc2[0] + 1, rc2[1] + 1))

            return
    print("No solution.")


v = get(input_iterator())
#v = get()
go(v)
