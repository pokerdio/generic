def step(v, sum, ten):
    v2 = {}
    sum2 = {}
    for i, i2 in ((j, j * j) for j in range(10)):
        for s, k in v.items():
            v2[s + i2] = (v2.get(s + i2, 0) + k)
            sum2[s + i2] = sum2.get(s + i2, 0) + sum.get(s, 0) + (k * ten * i)
    return v2, sum2


def go(n=20):
    v = {i * i: 1 for i in range(10)}
    s = {i * i: i for i in range(10)}
    ten = 10

    for i in range(n - 1):
        v, s = step(v, s, ten)
        ten = (10 * ten)

    ret = 0
    for i in (j * j for j in range(int(math.sqrt(81 * n)) + 1)):
        if i in s:
            ret += s[i]
    return ret


#print(go() % 10**9)
print(go())
