import primez
from math import log


def meld(products):
    if not products:
        return
    ret = set()
    for p in products:
        for i in range(len(p) - 1):
            for j in range(i + 1, len(p)):
                ret.add(tuple(reversed(sorted(p[:i] + p[i + 1:j] + p[j + 1:] + (p[i] * p[j],)))))
    return ret


def foo():
    products = ((2, 2, 5, 5, 5, 7, 11, 13), )

    best = 10**100
    best_product = None

    while products:
        for p in products:
            value = 0
            pr = primez.iterate_primez()
            for k in p:
                value += log(next(pr)) * (k - 1)
            if value < best:
                best = value
                best_product = p
        products = meld(products)
    return best_product


def bar(p):
    pr = primez.iterate_primez()
    ret = 1
    for k in p:
        ret *= (next(pr) ** (k - 1))
    return ret % 500500507
#-------------------------------------------------- above I solved a completely different problim


def foo2(n=500500):

    pr_it = primez.iterate_primez()
    pr = next(pr_it)
    v = {}

    lastn = n // 1000
    while n > 0:
        if n // 1000 < lastn:
            lastn = n // 1000
            print(n)
        best = None
        bestp = None
        for p, k in v.items():
            newp = p ** (k + 1)
            if not best or newp < best:
                best = newp
                bestp = p
        if not best:
            v[pr] = 1
            pr = next(pr_it)
            n -= 1
        elif best < pr:
            v[bestp] = v[bestp] * 2 + 1
            n -= 1
        else:
            while pr < best and n > 0:
                v[pr] = 1
                pr = next(pr_it)
                n -= 1

    ret = 1
    for p, k in v.items():
        ret = (ret * (p ** k % 500500507) % 500500507)
    return ret


#----------------------------------- let's optimize it some


class SortedQueue:
    def __init__(self, keyf=None):
        self.queue = []
        if keyf:
            self.keyf = keyf
        else:
            self.keyf = lambda x: x

    def __nonzero__(self):
        return len(self.queue) == 0

    def __getitem__(self, index):
        return self.queue[index]

    def __repr__(self):
        return str(self.queue)

    def __iter__(self):
        return iter(self.queue)

    def pop(self):
        if self.queue:
            return self.queue.pop()

    def push(self, item):
        i, j = 0, len(self.queue)

        if j <= 0:
            self.queue.append(item)
            return

        value = self.keyf(item)

        while i < j:
            k = (i + j) // 2
            if value >= self.keyf(self.queue[k]):
                i = k + 1
            else:
                j = k
        self.queue.insert(i, item)


def testqueue():
    control = []
    s = SortedQueue()
    for i in range(100):
        control.append(randint(100))
        s.Push(control[-1])
    assert(sorted(control) == s.queue)


def test():
    for _ in range(1000):
        testqueue()


def foo(n=500500, mod=500500507):
    q = SortedQueue(lambda x: -x[0] * x[1])
    ipr = primez.iterate_primez()
    pr = next(ipr)
    q.push((pr, pr))
    pr = next(ipr)
    n -= 1
    while n > 0:
        qlast = q[-1]
        qlastvalue = qlast[0] * qlast[1]
        if qlastvalue > pr:
            q.push((pr, pr))
            pr = next(ipr)
        else:
            a, b = q.pop()
            q.push((a * a * b, b))
        n -= 1
    ret = 1
    for x in q:
        ret = (ret * x[0]) % mod
    return ret
