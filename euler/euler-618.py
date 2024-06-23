import primez


def fibo(n, data=[1, 1]):
    while n >= len(data):
        data.append(data[-1] + data[-2])
    return data[n - 1]


def go(vn):
    n = max(vn)
    v = [[0], [0], [2]]  # list of sums for i made up of primez not greater than jth prime
    vp = list(primez.iterate_primez(n + 1))
    for i in range(3, n + 1):
        if i % 100 == 0:
            print(i)
        v0 = []
        for j in range(n):
            if j >= len(vp):
                break
            p = vp[j]
            if p > i:
                break

            new = (i == p) and p
            if v0:
                new += v0[-1]

            v1 = v[-p]
            if j < len(v1):
                new += v1[j] * p
            else:
                new += v1[-1] * p
            new %= 1000000000
            v0.append(new)
        v.append(v0)
    return sum(v[i][-1] for i in vn) % 1000000000


def solve():
    return go(list(fibo(i) for i in range(2, 25)))


# 634212216
