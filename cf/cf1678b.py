import sys
t = int(input())


for _ in range(t):
    n = int(input())
    s = sys.stdin.readline()
    lastc = s[0]
    count = 1
    ret = 0
    for c in s[1:]:
        if c == lastc:
            count += 1
        else:
            if count % 2 == 0:
                count = 1
                lastc = c
            else:
                ret += 1
                count += 1
    print(ret)
