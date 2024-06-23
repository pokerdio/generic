def get_ints():
    return [int(x) for x in input().split(" ")]


n, k = get_ints()
v = get_ints()
d = {}
for x in v:
    d[x] = d.get(x, 0) + 1

vx = sorted(d.keys())
vd = [d[x] for x in vx]

best = 0
bestx = 666
for i, x in enumerate(vx):
    k0 = k
    count = d[x]
    for j in range(i - 1, -1, - 1):
        vxj = vx[j]
        interval = x - vxj
        if k0 // interval + count < best:
            break
        delta = min(k0 // interval, vd[j])
        count += delta
        k0 -= delta * interval
        if k0 < interval:
            break
    if count > best:
        best = count
        bestx = x

print(best, bestx)
