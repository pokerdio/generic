def get_ints():
    return [int(x) for x in input().split(" ")]


n, k = get_ints()
v = get_ints()
d = {}
for x in v:
    d[x] = d.get(x, 0) + 1

vx = sorted(d.keys())

best = d[vx[0]]
bestx = vx[0]

trail_idx = 0
lastx = vx[0]
trail_count = 0
trail_count_first_step = d[vx[0]]
trail_cost = 0

for i, x in enumerate(vx):
    k0 = k
    count = d[x]

    if i > 0:
        trail_cost += (x - lastx) * trail_count
        while trail_cost > k:
            assert trail_idx < i
            delta = x - vx[trail_idx]
            erase = min((trail_cost - k + delta - 1) // delta, trail_count_first_step)

            trail_count_first_step -= erase
            trail_count -= erase
            trail_cost -= erase * delta
            if trail_count_first_step == 0:
                trail_idx += 1
                trail_count_first_step = d[vx[trail_idx]]

    trail_count += count
    if trail_count > best:
        best = trail_count
        bestx = x

    lastx = x

print(best, bestx)
