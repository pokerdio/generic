#from operator import add


def add(x, y):
    return (x + y) % 1000000007


class SegTree:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.value = 0
        if b - a > 1:
            half = (self.a + self.b) // 2
            self.left = SegTree(a, half)
            self.right = SegTree(half, b)

    def Value(self, a, b):
        if self.a >= a and self.b <= b:
            return self.value
        if self.a >= b or self.b <= a:
            return 0
        assert self.b - self.a > 1
        return (self.left.Value(a, b) + self.right.Value(a, b)) % 1000000007

    def __repr__(self):
        if self.b - self.a == 1:
            return f"({self.a}:{self.value})"
        return f"[{self.left}:{self.right}]={self.value}"

    def Set(self, a, b, value):
        #print(f"set {a}, {b}, {value}")
        assert len(value) == b - a
        assert a >= self.a and b <= self.b
        if self.b - self.a == 1:
            self.value = value[0]
            return
        half = (self.a + self.b) // 2
        if b <= half:
            self.left.Set(a, b, value)
        elif a >= half:
            self.right.Set(a, b, value)
        else:
            self.left.Set(a, half, value[:half - a])
            self.right.Set(half, b, value[half - a:])
        self.value = (self.left.value + self.right.value) % 1000000007


n, m = (int(x) for x in input().split())
a = [int(c) for c in input().split()]
requests = [input() for _ in range(m)]

v = [SegTree(1, n + 1) for _ in range(6)]

for k in range(6):
    v[k].Set(1, n + 1, [a[i] * ((i + 1) ** k) % 1000000007 for i in range(n)])

for req in requests:
    c, *lrx = req.split()
    l, r, x = (int(x) for x in lrx)

    if c == "=":
        for k in range(6):
            v[k].Set(l, r + 1, [x * (i ** k) for i in range(l, r + 1)])

    elif c == "?":
        if x == 0:
            print(v[0].Value(l, r + 1))
        delta = l - 1
        if x == 1:
            a, b = (v[x].Value(l, r + 1) for x in range(2))
            print((b - a * delta) % 1000000007)
        if x == 2:
            a, b, c = (v[x].Value(l, r + 1) for x in range(3))
            print((c - 2 * delta * b + delta * delta * a) % 1000000007)

        if x == 3:
            a, b, c, d = (v[x].Value(l, r + 1) for x in range(4))
            print((d - 3 * delta * c + 3 * delta * delta * b - delta ** 3 * a) % 1000000007)
        if x == 4:
            a, b, c, d, e = (v[x].Value(l, r + 1) for x in range(5))
            print((e - 4 * delta * d + 6 * delta * delta * c - 4 * (delta**3) * b + a * delta ** 4) % 1000000007)
        if x == 5:
            a, b, c, d, e, f = (v[x].Value(l, r + 1) for x in range(6))
            print((f - 5 * delta * e + 10 * delta * delta * d - 10 *
                   (delta ** 3) * c + 5 * (delta ** 4) * b - (delta ** 5) * a) % 1000000007)
