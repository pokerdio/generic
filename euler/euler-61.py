#!/usr/bin/env python3

# https://projecteuler.net/problem=61
#


def p3(n):
    return n * (n + 1) // 2


def p4(n):
    return n * n


def p5(n):
    return n * (3 * n - 1) // 2


def p6(n):
    return n * (2 * n - 1)


def p7(n):
    return n * (5 * n - 3) // 2


def p8(n):
    return n * (3 * n - 2)


def make_4digit():
    gen = {3: p3, 4: p4, 5: p5, 6: p6, 7: p7, 8: p8}
    four = {}
    for i, f in gen.items():
        four[i] = []
        j = 1
        while True:
            val = f(j)
            if val > 9999:
                break
            if val > 999:
                four[i].append(val)
            j += 1
    return four


four = make_4digit()


class nuchain:
    def __init__(self, gons_set, nums):
        self.nums = nums
        self.gons_set = gons_set

    def compatible(self, num):
        return self.nums[-1] % 100 == num // 100

    def iscycle(self):
        return self.compatible(self.nums[0])

    def grow(self, num, gon):
        if gon not in self.gons_set and self.compatible(num):
            newgons = self.gons_set.copy()
            newgons.add(gon)
            return nuchain(newgons, self.nums + [num])


def step(nulist):
    ret = []
    for nu in nulist:
        for gon in four.keys():
            for num in four[gon]:
                newnu = nu.grow(num, gon)
                if newnu:
                    ret.append(newnu)

    return ret


def go():
    nulist = []
    for i in four[3]:
        nulist.append(nuchain(set((3,)), [i]))
    for i in range(5):
        nulist = step(nulist)
    return [nu.nums for nu in nulist if nu.iscycle()]
