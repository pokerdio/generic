from math import sqrt, exp
import random
seed = random.randint(1, 10000)
print("seed", seed)
random.seed(seed)
n = random.randint(1, 100)
k = random.randint(1, n)
epsilon = random.randint(1, 999)
epsilon = epsilon / 1000.0


def randxy():
    return (random.randint(1, 100000) - 50000, random.randint(1, 100000) - 50000)


x0, y0 = randxy()
xy = [randxy() for _ in range(n)]


vd2 = [(x - x0)**2+(y - y0) ** 2 for x, y in xy]

maxd = sqrt(sorted(vd2)[k - 1])


def pfail(r):
    r2 = r * r
    sure = 0

    vp = [1.0] + [0.0] * n
    vp2 = [0.0] * (n + 1)
    maybe = 0
    for d2 in vd2:
        if d2 <= r2:
            sure += 1
            continue
        pbomb = exp(1 - d2 / r2)
        pfail = 1.0 - pbomb
        maybe += 1
        vp2[0] = vp[0] * pfail
        for i in range(1, maybe + 1):
            vp2[i] = vp[i] * pfail + vp[i - 1] * pbomb
        vp, vp2 = vp2, vp
    if sure >= k:
        return 0.0
    return sum(vp[:k - sure])


def go():
    a = maxd / 10
    b = maxd
    pa = pfail(a)
    pb = pfail(b)

    while pa - pb > 0.000001 or b - a > 0.000001:
        #print("%.2f %.2f %f %f" % (a, b, pa, pb))
        c = (a + b) / 2.0
        pc = pfail(c)
        if pc < epsilon:
            b, pb = c, pc
        else:
            a, pa = c, pc
    return (a + b) / 2


print(go())
