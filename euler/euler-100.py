import math

# m total balls, n blue balls
# probability is n/m * (n-1)/(m-1) and has to be 1/2

# n*n-n == (m*m-m)/2

# n*n-n-a == 0
# delta = 1 + 4 * a
# positive solution is: 1 + sqrt(delta)/ 2

# solve above in n as a float for m is 10**12 to get a starter n
# loop n until the delta is a perfect square for solution


def solve(a):
    goodroot, root = sq(4 * a + 1)
    assert(goodroot)
    return (root + 1) // 2


bign = 10**12


def go2():
    m = 1
    a = (m * m - m) // 2
    delta = 1 + 4 * a
    rootdelta = sq(delta)[1] - 5
    rootdeltasq = rootdelta ** 2

    m4 = 4 * m
    for _ in range(10 ** 6):
        while rootdeltasq < delta:
            rootdelta += 1
            rootdeltasq = rootdelta ** 2

        # m = m4 // 4
        # print(m, delta, 1 + 2 * (m ** 2 - m), rootdelta, rootdeltasq, rootdeltasq - delta)

        if rootdeltasq == delta:
            n = (1 + rootdelta) // 2
            print(n, m4 // 4)

        m4, delta = m4 + 4, delta + m4


def foobar():
    n0, n1 = 1, 3

    bign = 10 ** 12

    for _ in range(100):
        n = 6 * n1 - n0 - 2
        m = solve(2 * n * n - 2 * n)

        print(n, m, m * (m - 1) / n / (n - 1))
        if m > bign:
            print("SUCCESS")
            return

        n1, n0 = n, n1


def sq(x):
    if x == 0:
        return True
    s = str(x)
    i = int(s[:(len(s) + 1) // 2])
    while abs(i - x // i) > 1:
        i = (i + x // i) // 2
    return i * i == x, i
