import sys

input = sys.stdin.readline
#f = open("a.txt", "r")
#input = f.readline


def ints():
    return [int(c) for c in input().split()]


def go():
    n = int(input())
    b = ints()
    c = ints()

    d = [x + y for x, y in zip(b, c)]
    dsum = sum(d)

    if dsum % (2*n):
        print(-1)
        return
    asum = dsum // (2 * n)

    a = [(x - asum) // n for x in d]

    two = 1
    abits = []
    twos = [2 ** x for x in range(30)]
    for two in twos:
        bit_count = 0
        for x in a:
            bit_count += ((x & two) > 0)
        abits.append(bit_count)

    for i in range(n):
        aa, bb, cc = a[i], b[i], c[i]
        bbb, ccc = 0, 0
        for x, two in enumerate(twos):
            if aa & two:
                bbb += abits[x] * two
                ccc += n * two
            else:
                ccc += abits[x] * two
        if bbb != bb or ccc != cc:
            print(-1)
            return
    print(" ".join(str(x) for x in a))


go()
