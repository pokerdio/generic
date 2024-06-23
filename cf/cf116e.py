import sys
n, m = (int(x) for x in input().split())


ret = 1
vert = [0] * m

for row in range(n):
    s = sys.stdin.readline()

    horiz = 0

    desired_vert = -1 if (row % 2 > 0) else 1

    horiz = 0
    x = -1
    while ret > 0:
        x = s.find("1", x + 1)
        if x < 0:
            break
        if vert[x] == 0:
            vert[x] = desired_vert
        else:
            if vert[x] != desired_vert:
                ret = 0
                break

        desired_horiz = -1 if (x % 2 > 0) else 1

        if horiz == 0:
            horiz = desired_horiz
        elif horiz != desired_horiz:
            ret = 0
            break
    x = -1
    while ret > 0:
        x = s.find("4", x + 1)
        if x < 0:
            break
        if vert[x] == 0:
            vert[x] = desired_vert
        else:
            if vert[x] != desired_vert:
                ret = 0
                break

        desired_horiz = -1 if (x % 2 > 0) else 1

        if horiz == 0:
            horiz = -desired_horiz
        elif horiz != -desired_horiz:
            ret = 0
            break
    x = -1
    while ret > 0:
        x = s.find("2", x + 1)
        if x < 0:
            break
        if vert[x] == 0:
            vert[x] = -desired_vert
        else:
            if vert[x] != -desired_vert:
                ret = 0
                break

        desired_horiz = -1 if (x % 2 > 0) else 1

        if horiz == 0:
            horiz = desired_horiz
        elif horiz != desired_horiz:
            ret = 0
            break
    x = -1
    while ret > 0:
        x = s.find("3", x + 1)
        if x < 0:
            break
        if vert[x] == 0:
            vert[x] = -desired_vert
        else:
            if vert[x] != -desired_vert:
                ret = 0
                break
        desired_horiz = -1 if (x % 2 > 0) else 1

        if horiz == 0:
            horiz = -desired_horiz
        elif horiz != -desired_horiz:
            ret = 0
            break

    if horiz == 0:
        ret = (2 * ret % 1000003)

    if ret == 0:
        break


for col in range(m):
    if vert[col] == 0:
        ret = (ret * 2) % 1000003

print(ret % 1000003)
