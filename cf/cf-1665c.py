from collections import Counter as C

test_count = int(input())


for _ in range(test_count):
    n = int(input())
    v = [int(c) for c in input().split()]
    m = sorted([1] + list(C(v).values()))[::-1]
    for t in range(0, len(m)):
        m[t] = max(0, m[t] - (len(m) - t))

    ret = len(m)
    m = sorted(x for x in m if x > 0)
    while m:
        m = sorted(x - 1 for x in m if x > 1)
        if m:
            m[-1] -= 1
            if not m[-1]:
                del m[-1]
        ret += 1
    print(ret)
