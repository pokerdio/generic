def go(n):
    ret = set()
    for i in range(2, n):
        if i % 10000 == 0:
            print(i)
        for j in range(2, i + 1):
            nn = i * j * (i - 1) * (j - 1)
            if nn > n:
                break
            ret.add(nn)
        if i > 2 and j == 2:
            break
    return ret

# print(len(go(10**14)))  # memory intensive beware
# 75737353


def foo(n):
    for i in range(1, n):
        delta = 141 + i * i - 14 * i
        d2 = int(sqrt(delta))
        if d2 * d2 == delta:
            print(delta, d2, d2 * d2, i)
