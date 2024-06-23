from math import sqrt, exp

try:
    def readints():
        return [int(x) for x in input().split(" ")]

    n = readints()[0]
    k, epsilon = readints()
    epsilon = epsilon / 1000.0

    x0, y0 = readints()

    xy = [readints() for _ in range(n)]

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
            if r2 == 0.0:
                if d2 == 0.0:
                    pbomb = 1.0
                else:
                    pbomb = 0.0
            else:
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
            c = (a + b) / 2.0
            pc = pfail(c)
            if pc < epsilon:
                b, pb = c, pc
            else:
                a, pa = c, pc
        return (a + b) / 2

    print(go())

except Exception as e:
    print(str(e))
