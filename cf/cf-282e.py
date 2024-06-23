from random import randint
n = int(input())
v = [int(x) for x in input().split(" ")]


# def randv(n):
#     return [randint(1, 10000000000) for _ in range(n)]


# v = randv(185000)
# n = len(v)


def int2b(n):
    return [int(x) for x in f"{n:041b}"]


class BiTrie():
    def __init__(self):
        self.data = [None, None]
        self.depth = 1
        self.empty = True

    def __repr__(self):
        return str(self.data)

    def __getitem__(self, n):
        return self.data[n]

    def __lshift__(self, n):
        bitz = int2b(n)
        if len(bitz) > self.depth:
            if not self.empty:
                for _ in range(len(bitz) - self.depth):
                    self.data = [self.data, None]
            self.depth = len(bitz)
        self.empty = False
        if len(bitz) < self.depth:
            bitz = [0] * (self.depth - len(bitz)) + bitz
        data = self.data

        for bit in bitz[:-1]:
            if not data[bit]:
                data[bit] = [None, None]
            data = data[bit]
        data[bitz[-1]] = n

    def __and__(self, n):
        """funny overload for retrieving the stored number 
        that xors to the biggest value with n"""
        bitz = int2b(n)

        if len(bitz) > self.depth:
            bitz = bitz[len(bitz) - self.depth:]
        if len(bitz) < self.depth:
            bitz = [0] * (self.depth - len(bitz)) + bitz
        data = self.data
        for bit in bitz:
            desired = not bit
            if data[desired] != None:
                data = data[desired]
            else:
                data = data[1 - desired]
        return data


def xor(v):
    ret = 0
    for x in v:
        ret ^= x
    return ret


def _go(v=v):
    n = len(v)
    xor_all = xor(v)
    best = xor_all
    besti, bestj = 0, len(v) - 1
    for i in range(n):
        mid_xor = 0
        for j, x in enumerate(v[i:], start=i):
            mid_xor ^= x
            if xor_all ^ mid_xor > best:
                best = xor_all ^ mid_xor
                besti = i
                bestj = j

    return best, besti, bestj


def go(v=v):
    n = len(v)
    pre = xor(v)
    post = 0
    best = pre
    b = BiTrie()
    b << 0
    for x in reversed(v):
        pre ^= x
        post ^= x
        b << post
        new = pre ^ (b & pre)
        if new > best:
            best = new
    return best


print(go())
