import sys


def add(x, y):
    return (x + y) % 1000000007


def vadd(x, y):
    return tuple((a + b) % 1000000007 for a, b in zip(x, y))


vzero = (0, 0, 0, 0, 0, 0)


class SegTree:
    def __init__(self, a, b, f=add, zero=0):
        self.a = a
        self.b = b
        self.n = b - a
        self.half = (a + b) // 2
        self.value = 0
        self.f = f
        self.zero = zero
        if b - a > 1:
            self.left = SegTree(a, self.half, f, zero)
            self.right = SegTree(self.half, b, f, zero)

    def Value(self, a, b):
        if self.a >= a and self.b <= b:
            return self.value
        if self.a >= b or self.b <= a:
            return self.zero
        assert self.n > 1
        return self.f(self.left.Value(a, b), self.right.Value(a, b))

    def __repr__(self):
        if self.n == 1:
            return f"({self.a}:{self.value})"
        return f"[{self.left}:{self.right}]={self.value}"

    def SetV(self, a, b, value):
        #print(f"set {a}, {b}, {value}")
        assert len(value) == b - a
        assert a >= self.a and b <= self.b
        if self.n == 1:
            self.value = value[0]
            return
        if b <= self.half:
            self.left.SetV(a, b, value)
        elif a >= self.half:
            self.right.SetV(a, b, value)
        else:
            self.left.SetV(a, self.half, value[:self.half - a])
            self.right.SetV(self.half, b, value[self.half - a:])
        self.value = self.f(self.left.value, self.right.value)

    def SetF(self, a, b, f):
        #print(f"set {a}, {b}, {value}")
        assert len(value) == b - a
        assert a >= self.a and b <= self.b
        if a == self.a and b == self.b:
            self.value = f(a, b)
            return

        if b <= self.half:
            self.left.SetF(a, b, f)
        elif a >= self.half:
            self.right.SetF(a, b, f)
        else:
            self.left.SetF(a, self.half, f)
            self.right.SetF(self.half, b, f)
        self.value = self.f(self.left.value, self.right.value)


def MakeValueSetter(value):
    def f(a, b):
        print(value)
    return f


n, m = (int(x) for x in input().split())
a = [int(c) for c in input().split()]
requests = [input() for _ in range(m)]


# n, m = 4, 5
# a = [5, 10, 2, 1]

# requests = ["? 1 2 1",
#             "= 2 2 0",
#             "? 2 4 3",
#             "= 1 4 1",
#             "? 1 4 5"]

v = SegTree(1, n + 1, vadd, vzero)

v.Set(1, n + 1, [tuple(a[i] * ((i + 1) ** k) % 1000000007 for k in range(6)) for i in range(n)])

for req in requests:
    c, *lrx = req.split()
    l, r, x = (int(x) for x in lrx)

    if c == "=":
        v.Set(l, r + 1, [tuple(x * (i ** k) for k in range(6)) for i in range(l, r + 1)])

    elif c == "?":
        val = v.Value(l, r + 1)
        if x == 0:
            print(val[0])
        delta = l - 1
        if x == 1:
            a, b = val[:2]
            print((b - a * delta) % 1000000007)
        if x == 2:
            # (n-delta)**2 == n*n-2delta*n-delta*delta
            a, b, c = val[:3]
            print((c - 2 * delta * b + delta * delta * a) % 1000000007)

        if x == 3:
            # (n - delta) ** 3 == n * n * n -3 * n * n * delta + 3 * n * n * delta - delta ** 3
            a, b, c, d = val[:4]
            print((d - 3 * delta * c + 3 * delta * delta * b - delta ** 3 * a) % 1000000007)
        if x == 4:
            a, b, c, d, e = val[:5]
            print((e - 4 * delta * d + 6 * delta * delta * c - 4 * (delta**3) * b + a * delta ** 4) % 1000000007)
        if x == 5:
            a, b, c, d, e, f = val
            print((f - 5 * delta * e + 10 * delta * delta * d - 10 *
                   (delta ** 3) * c + 5 * (delta ** 4) * b - (delta ** 5) * a) % 1000000007)
