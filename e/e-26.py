#!/usr/bin/env python3

#


def div1(n):
    rest = 10

    restv = [10]

    s = ""
    while True:
        s += str(rest // n)
        rest = (rest % n) * 10

        if rest == 0:
            return s, ""

        if rest in restv:
            return s[:restv.index(rest)], s[restv.index(rest):]

        restv.append(rest)


def go(n):
    maxi, maxs = 0, ""
    for i in range(2, n + 1):
        s, rep = div1(i)
#        print(i, s, rep)
        if len(rep) > len(maxs):
            maxi = i
            maxs = rep

    print("1/%d = 0.%s(%s)" % (maxi, *div1(maxi)))
    return maxi
