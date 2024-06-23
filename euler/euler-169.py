import re
import sys

print(sys.getrecursionlimit())


def go(s):
    s = re.sub("^1*", "", s)
    if len(s) <= 1:
        return 1

    zeroz, rest = re.match("(^0+)(.*)", s).groups()
    return go(rest) + len(zeroz) * go("0" + rest[1:])


def tobinary(n):
    return "".join(list(reversed("{0:b}".format(n))))


print(go(tobinary(10**25)))
