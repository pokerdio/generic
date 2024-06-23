


def go1(m, n):
    """horizontal"""
    s = 0
    for gm in range(1, m + 1):
        for gn in range(1, n  + 1):
            for i in range(1, gm + 1):
                for j in range(1, gn + 1):
#print(gm, gn, i, j, (gm - i + 1) * (gn - j + 1))
                    s += (gm - i + 1) * (gn - j + 1)
    return s

def go2(m, n):
    """diagonal"""
    s = 0

    for gm in range(1, m + 1): #x axis
        for gn in range(1, n + 1):  #grid dimensions 
            half_total = 2 * min(gn, gm)
            for i in range(1, half_total): #x axis
                for j in range(1, half_total + 1 - i): #y axis
#print("trying", i, j, "in", gm, gn)
                    #top is whole coords
                    w = ((i + 1) // 2 + (j + 1) // 2) 
                    h = (i + j + 1) // 2 
                    if w <= gm and h <= gn:
                        delta = (gm - w + 1) * (gn - h + 1)
#print("dot zero", gm, gn, "-", i, j, delta, "---", w, h)
                        s += delta

                    #top is half and half coords (center of a grid square)
                    w = i // 2 + j // 2 + 1
                    h = (i + j) // 2 + 1
                    if w <= gm and h <= gn:
                        delta = (gm - w + 1) * (gn - h + 1)
#print("dot five", gm, gn, i, j, delta)
                        s += delta

    return s


def go(m, n):
    return go1(m, n) + go2(m, n)

# print(go(47,43))
# 846910284
