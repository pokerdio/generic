t = int(input())

mod = 998244353

for _ in range(t):
    n, k = (int(c) for c in input().split())
    v = list(int(c) for c in input().split())

    ret = 1

    for i in range(n - k, n):
        if v[i] > 0:
            ret = 0

    for i in range(n):
        if i < k:
            ret = ret * (i + 1) % mod
        else:
            val = v[i - k]

            if val == -1:
                ret = ret * (i + 1) % mod
            elif val == 0:
                ret = ret * (k + 1) % mod
            elif val > i:
                ret = 0
    print(ret)
