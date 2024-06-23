_ = int(input())
k1 = tuple(int(c) for c in input().split())[1:]
k2 = tuple(int(c) for c in input().split())[1:]


def step(k1, k2):
    if k1[0] > k2[0]:
        return (*k1[1:], k2[0], k1[0]), k2[1:]
    else:
        return k1[1:], (*k2[1:], k1[0], k2[0])


def go(k1=k1, k2=k2):
    n = 0
    s = set()
    while k1 and k2:
        n += 1
        k1, k2 = step(k1, k2)
        kpair = (k1, k2)
        if kpair in s:
            print("-1")
            return
        s.add((k1, k2))

    print(n, k1 and "1" or "2")


go()
