#!/usr/bin/env python3


k = 0


def PermIter(elements):
    ele = set(elements)
    perm = []

    def PermGo():
        if ele:
            for i in sorted(ele):
                perm.append(i)
                ele.remove(i)
                yield from PermGo()
                ele.add(i)
                perm.pop()
        else:
            yield perm[:]

    return PermGo()


def nth(iterable, n):
    ret = None
    for i in range(n):
        ret = next(iterable)
    return ret


print("".join(nth(PermIter("0123456789"), 1000000)))
