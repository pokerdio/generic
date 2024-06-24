def upcount(ndigitz):
    up = {x: 1 for x in range(0, 10)}

    s = 9
    for i in range(ndigitz - 1):
        up2 = {}
        for k in range(1, 10):
            up2[k] = sum((up[x] for x in range(k, 10)))

        up = up2
        s += sum((up[x] for x in range(1, 10)))
    return s


def downcount(ndigitz):
    down = {x: 1 for x in range(0, 10)}
    s = 9
    for i in range(ndigitz - 1):
        down2 = {}
        for k in range(1, 10):
            down2[k] = 1 + sum((down[x] for x in range(1, k + 1)))

        down = down2
        s += sum((down[x] for x in range(1, 10)))
    return s


def flatcount(ndigitz):
    return 9 * ndigitz


def count(n):
    return upcount(n) + downcount(n) - flatcount(n)
