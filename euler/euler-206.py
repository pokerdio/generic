def five_digitz():
    for i in range(100000):
        if re.match("7.8.9", ("000000%d" % (i * i))[-5:]):
            yield i


def brute_solve():
    fivedee = list(five_digitz())

    for n in range(100000000, 140000000, 100000):
        for plusn in fivedee:
            n2 = n + plusn
            if re.match("1.2.3.4.5.6.7.8.9", str(n2 * n2)):
                print("%d0" % n2)

# 1389019170
