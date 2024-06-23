def readints():
    return [int(x) for x in input().split(" ")]


x, y, z = readints()
x0, y0, z0 = readints()
a1, a2, a3, a4, a5, a6 = readints()


ret = 0
if y < 0:
    ret += a1
if y > y0:
    ret += a2
if z < 0:
    ret += a3
if z > z0:
    ret += a4
if x < 0:
    ret += a5
if x > x0:
    ret += a6

print(ret)
