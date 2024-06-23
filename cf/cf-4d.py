def ints():
    return [int(x) for x in input().split()]


n, w, h = ints()

env = [ints() for _ in range(n)]
env = sorted([(*xy, id) for id, xy in enumerate(env) if xy[0] > w and xy[1] > h])

if not env:
    print(0)
    exit()

n = len(env)

v = [1] * n
for i, ipair in enumerate(env[1:], start=1):
    wi, hi, _ = ipair
    for j, jpair in enumerate(env[:i]):
        wj, hj, _ = jpair
        if wi > wj and hi > hj:
            v[i] = max(v[i], v[j] + 1)


big = max(range(n), key=lambda x: v[x])
ret = []

print(v[big])

while True:
    ret.append(env[big][2])
    if v[big] == 1:
        print(" ".join(str(x + 1) for x in reversed(ret)))
        exit()
    bigx, bigy, _ = env[big]
    for i in range(big - 1, -1, -1):
        if v[i] != v[big] - 1:
            continue

        x, y, _ = env[i]
        if bigx > x and bigy > y:
            big = i
            break
