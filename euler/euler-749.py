from builtins import sum


def gen_digitz(d, n):
    if d == 9:
        yield (n, )
        return
    yield (n, *((0,) * (9 - d)))
    for i in range(n):
        for s in gen_digitz(d + 1, n - i):
            yield (i, *s)


def go(n):
    count = 0
    for s in gen_digitz(0, n):
        count += 1
        if count % 10000 == 0:
            print(s)
        for k in range(4 * n):
            q = sum(s[i] * (i ** k) for i in range(1, 10))

            qstr2 = str(q - 1)
            s2 = tuple(qstr2.count(c) for c in "0123456789")
            if s2 == s:
                yield q - 1

            qstr3 = str(q + 1)
            s3 = tuple(qstr3.count(c) for c in "0123456789")
            if s3 == s:
                yield q + 1

#            print(q, s, s2, s3)
            if len(qstr3) > n:
                break


# sum(sum(go(n) for n in range(1, 17))) -> 13459471903176422
