ntest = int(input())

def dist(x1,y1,x2,y2):
    return abs (x1 - x2) + abs(y1 - y2)


for _ in range(ntest):
    w, h, sx, sy, d = (int(x) for x in input().split())
    ok1, ok2 = True, True


# ok1 is the path that goes from 1,1 all the way right to n,1 then down to n,m
# ok2 is the path that goes from 1,1 all the way down to 1,m then right to n,m
# we check the two paths square by square for laser proximity 

# if one path is good we print its length (it is always m+n-2)

    for x in range(1, w + 1):
        if dist(x, 1, sx, sy) <= d:
            ok1 = False
        if dist(x, h, sx, sy) <= d:
            ok2 = False

    for y in range(1, h + 1):
        if dist(w, y, sx, sy) <= d:
            ok1 = False
        if dist(1, y, sx, sy) <= d:
            ok2 = False

    if ok1 or ok2:
        print (w + h - 2)
    else:
        print (-1)


