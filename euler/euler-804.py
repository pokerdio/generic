from math import sqrt


def bar(n):
    """counts pairs with y such that 41yy>n"""
    y0 = int(sqrt(n // 41)) 
    x1 = 1
    x2 = y0
    ret = 0
    for y in range(y0 + 1, y0 * 2):
        y41 = y * y * 41
        while x1 > 1 and (x1 * x1 - x1 * y + y41 <= n):
            x1 -= 1
        while x1 < y and (x1 * x1 - x1 * y + y41 > n):
            x1 += 1

        while x2 < y and (x2 * x2 - x2 * y + y41 <= n):
            x2 += 1
        while x2 > 1 and (x2 * x2 - x2 * y + y41 > n):
            x2 -= 1


        if x1 > x2:
            return ret
        
        ret += (x2 - x1 + 1) * 2
    return ret


def foo(n):
    """sums pairs with y such that 41yy<=n"""
    y = int(sqrt(n // 41)) 
    x1 = 0
    x2 = 0

    # for y=0, x goes from -sqrt(n) to +sqrt(n) without zero
    ret = 2 * (int(sqrt (n))) 
    while y > 0:
        y41 = 41 * y * y

        while x1 * x1 - x1 * y + y41 <= n:
            x1 += 1
        while x1 * x1 - x1 * y + y41 > n:
            x1 -= 1

        while x2 * x2 + x2 * y + y41 <= n:
            x2 += 1
        while x2 * x2 + x2 * y + y41 > n:
            x2 -= 1


        delta = 2 # (0,y) (0,-y) are always solutions for y>0

        if (x1 > 0):
            delta += 2 * x1 # xes with opposite sign to y
        if (x2 > 0):
            delta += 2 * x2 # xes with same sign as y

        ret += delta

        y -= 1
    return ret


print(foo(10**16) + bar(10**16))

