def gen(n=10**6):
    a = 1
    for i in range(n):
        a = a * 153 % 10000019
        yield a


class Bucket:
    def __init__(self, low, high):
        self.g = []
        self.total = [0] * 4
        self.count = [0] * 4
        self.low = low
        self.high = high

    def Update(self, number, vtotal, vcount):
        assert(number >= self.low and number < self.high)
        self.g.append((number, vtotal, vcount))
        for i in range(4):
            self.total[i] = (vtotal[i] + self.total[i]) % 1000000007
            self.count[i] = (vcount[i] + self.count[i]) % 1000000007

    def __contains__(self, n):
        return n >= self.low and n < self.high


def grow(x, total, count, prevt, prevc):
    for i in range(3):
        count[i + 1] = (count[i + 1] + prevc[i]) % 1000000007
        total[i + 1] = (total[i + 1] + prevt[i] + x * prevc[i]) % 1000000007


def go(n=1000000):
    nbuckits = int(sqrt(n)) + 1
    buckits = [Bucket(i * 10000019 // nbuckits, (i + 1) * 10000019 // nbuckits)
               for i in range(nbuckits)]
    k = 0

    for x in gen(n):
        k += 1
        if k % 1000 == 0:
            print("%d/1000000" % k)
        total = [x] + [0] * 3
        count = [1] + [0] * 3
        for b in buckits:
            if x in b:
                for y, ytotal, ycount in b.g:
                    if y < x:
                        grow(x, total, count, ytotal, ycount)
                b.Update(x, total, count)
                break
            else:
                grow(x, total, count, b.total, b.count)
    ret = 0
    for b in buckits:
        ret = (ret + b.total[3]) % 1000000007
    return ret
