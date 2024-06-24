from math import comb
from time import sleep


def SlowF():
    for i in range(1, 20000):
        s = str(i)
        if max(s) <= "3" and min(s) > "0" and s.count("1") <= 3 and s.count("2") <= 3 and s.count("3") <= 3:
            yield i


def GenPats():
    f = [0] + list(SlowF())
    n = f[-1]
    d = {}
    for i in f:
        for j in f:
            ij = i + j
            if ij > n:
                continue
            for k in f:
                ijk = ij + k
                if ijk > n:
                    continue
                if ijk in d:
                    d[ijk].append((i, j, k))
                else:
                    d[ijk] = [(i, j, k)]
    return d


class Filtzor:

    def __init__(self, pats):
        self.pats = set(pats)

    def Empty(self):
        return not self.pats or (len(self.pats) == 1 and (0, 0, 0) in self.pats)

    def Refine(self, digit):
        if digit == 1:
            pats2 = set((x - 1, y, z) for x, y, z in self.pats if x > 0)
        elif digit == 2:
            pats2 = set((x, y - 1, z) for x, y, z in self.pats if y > 0)
        elif digit == 3:
            pats2 = set((x, y, z - 1) for x, y, z in self.pats if z > 0)
        else:
            assert None
        return Filtzor(pats2)

    def NDigitz(self):
        return sum(self.pats)

    def NCombos(self):
        ret = 0
        for one, two, three in self.pats:
            ret += comb(one + two + three, one) * comb(two + three, two)
        return ret

    def __repr__(self):
        return str(self.pats)


def Triangularize(f, n):
    if f.Empty():
        return ""
    f1, f2, f3 = f.Refine(1), f.Refine(2), f.Refine(3)
    n1, n2, n3 = f1.NCombos(), f2.NCombos(), f3.NCombos()

    if n1 >= n:
        return "1" + Triangularize(f1, n)
    if n1 + n2 >= n:
        return "2" + Triangularize(f2, n - n1)
    return "3" + Triangularize(f3, n - n1 - n2)


def go(n, d=GenPats()):
    nd = sorted(d.keys())[1:]

    for digitz in nd:
        f = Filtzor(d[digitz])
        nf = f.NCombos()
        if nf >= n:
            return Triangularize(f, n)
        n -= nf


print(int(go(111111111111222333)) % 123123123)  # 57808202
