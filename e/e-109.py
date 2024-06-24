# project euler problem 109


def maekdict():
    d = {"d25": 50, "s25": 25}
    for i in range(1, 21):
        d["s%d" % i] = i
        d["d%d" % i] = 2 * i
        d["t%d" % i] = 3 * i
    return d


def maekdoubles(d):
    return [s for s in d.keys() if s[0] == "d"]


def maekcomboz(d):
    none = [tuple()]
    one = list((key,) for key in d.keys())
    two = list(set(tuple(sorted((i, j)))
                   for i in d.keys()
                   for j in d.keys()))
    return none + one + two


def go():
    d = maekdict()
    first = maekcomboz(d)
    final = maekdoubles(d)

    return sum(1 for i in first for j in final
               if sum(d[x] for x in i + (j,)) < 100)
