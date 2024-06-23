n = int(input())
v = sorted([int(c) for c in input().split()])

x = v[0] - 1
ret = 0
for y in v:
    if y <= x:
        ret += x - y + 1
        x = x + 1
    else:
        x = y
print(ret)
