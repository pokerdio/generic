class Data:
    def __init__(self):
        self._p = [[None] * 100 for _ in range(100)]
        self._q = [[None] * 100 for _ in range(100)]
        # p[x][y] is the probability two will win when playing when
        # one has x and two has y
        # q[x][y] is the same for one

    def setp(self, one, two, p):
        #        print("setp", one, two, p)
        assert(not self._p[one][two])
        self._p[one][two] = p

    def setq(self, one, two, p):
        #        print("setq", one, two, p)
        assert(not self._q[one][two])
        self._q[one][two] = p

    def p(self, one, two):
        if one >= 100:
            assert(two < 100)
            return 0.0
        if two >= 100:
            return 1.0
        assert self._p[one][two]is not None, "p missing %d %d" % (one, two)
        return self._p[one][two]

    def q(self, one, two):
        if one >= 100:
            assert(two < 100)
            return 1.0
        if two >= 100:
            return 0.0
        assert self._q[one][two] is not None, "q missing %d %d" % (one, two)
        return self._q[one][two]


def go():
    d = Data()
    for one in range(99, -1, -1):
        for two in range(99, -1, -1):
            # first we do the new p at one,two
            bestp = 0.0
            for pow in (1, 2, 4, 8, 16, 32, 64, 128):
                pwin = 0.5 / pow

                p = (pwin * (1.0 - d.q(one, two + pow)) +
                     (1.0 - pwin) * 0.5 * d.p(one + 1, two)) / \
                    (1.0 - 0.5 * (1.0 - pwin))
                if p > bestp:
                    bestp = p
                if pow + two >= 100:
                    break
            d.setp(one, two, bestp)
            d.setq(one, two, 1.0 - 0.5 * (d.p(one + 1, two) + bestp))
    return "%.8f" % (1.0 - d.q(0, 0))
