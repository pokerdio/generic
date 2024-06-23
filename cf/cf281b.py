from fractions import Fraction as Fr
x, y, n = (int(c) for c in input().split())
xy = Fr(x, y)

v = []
for b in range(1, n + 1):
    a = b * x // y
    v.append((abs(Fr(a, b) - xy), a, b))
    v.append((abs(Fr(a + 1, b) - xy), a + 1, b))

_, a, b = min(v)
print("%d/%d" % (a, b))
