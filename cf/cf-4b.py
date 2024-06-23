def readtwo():
    return [int(x) for x in input().split()]


d, sumTime = readtwo()

v = [readtwo() for _ in range(d)]

mintotal, maxtotal = [sum(x) for x in zip(*v)]


if sumTime < mintotal or sumTime > maxtotal:
    print("NO")
else:
    print("YES")
    ret = []
    n = sumTime - mintotal
    for x, pair in enumerate(v):
        a, b = pair
        extra_study = min(n, b - a)
        n -= extra_study
        ret.append(a + extra_study)
    print(" ".join(str(x) for x in ret))
