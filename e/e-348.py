def pallies(n):
    pat = "%%0%dd" % n
    for i in range(1, 10 ** n):
        if i % 10:
            s = pat % i
            yield int(s[::-1] + s)
            for i in range(10):
                yield int(s[::-1] + str(i) + s)


def go(ndigitz):
    n = int(3.4 * 10 ** ndigitz)
    n2 = n * n
    s2 = set(x * x for x in range(1, n))
    v3 = []
    for i in range(1, n):
        i3 = i ** 3
        if i3 > n2:
            break
        v3.append(i3)

    for digitz in range(1, ndigitz + 1):
        for p in pallies(digitz):
            k = 0
            for i3 in v3:
                if i3 > p:
                    break
                if p - i3 in s2:
                    k += 1
                    if k > 4:
                        break
            if k == 4:
                yield p


print(sum(go(4)))  # turns out there's exactly five in here
