p = print
n, m, k = (int(s) for s in input().split())
roads = [[int(x) for x in input().split()] for _ in range(m)]
v = [[] for _ in range(n)]
for a, b in roads:
    v[a - 1].append(b - 1)
    v[b - 1].append(a - 1)

tri = [[int(x) for x in input().split()] for _ in range(k)]

forbid_tripl = set()
forbid = {}
pred = {x:set() for x in range(n)}

for a, b, c in tri:
    a, b, c = a - 1, b - 1, c - 1
    forbid_tripl.add((a, b, c))
    ab = (a, b)
    pred[b].add(a)
    if (a, b) in forbid:
        forbid[ab].append(c)
    else:
        forbid[ab] = [c]



vis = {(-1,0):None}
o = {(-1, 0):None}

while True:
    done = False
    new_batch = {}

    for xp in o.keys():
        a, b = xp
        for c in v[b]:
            bc = (b, c)
            if bc in vis:
                continue
            c1 = (-1, c)
            if (c1 in new_batch) or (c1 in vis):
                continue

            triplet = (a, b, c)
            if triplet in forbid_tripl:
                continue

            if not (b in pred[c]):
                new_batch[c1] = xp
            else:
                new_batch[bc] = xp

            if c == n - 1:
                done = True

    if not new_batch:
        p(-1)
        break

    vis.update(new_batch)
    o = new_batch
    if done:
        count = 0
        path = []
        for ab in new_batch.keys():
            if ab[1] == n - 1:
                break
        while ab:
            path.append(ab[1])
            ab = vis.get(ab, None)

        p(len(path) - 1)
        p(" ".join(str(x + 1) for x in reversed(path)))
        break

