test_count = int(input())

for _ in range(test_count):
    n = int(input())
    a = [int(c) for c in input().split()]
    query_count = int(input())

    p, r = 1, 0
    for i in range(30):
        print("? %d %d" % (p - r, 3 * p - r))
        g = int(input())
        assert(g % p == 0)
        g //= p

        if g % 2 == 0:
            r = r + p
        p = p * 2
    print("! %d" % r)
