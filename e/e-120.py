def foo(a):
    rmax = 0
    s = 2
    m = 0
    sm = set()
    a2 = a * a

    while True:
        if s % a2 > rmax:
            rmax = s % a2

        if (s, m) in sm:
            return rmax
        sm.add((s, m))
        s, m = (a * s + m) % a2, (a * m + s) % a2


print(sum(foo(i) for i in range(3, 1001)))
