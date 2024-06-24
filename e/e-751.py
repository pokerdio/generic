def boo(t):
    t = float(t)
    s = "2."
    for i in range(25):
        t = floor(t) * (t - floor(t) + 1.0)
        s += str(int(floor(t)))
    return s


def foo(f, n=100):
    s = "2.2"
    for _ in range(n):
        s2 = f(s)
        if s2 == s:
            return s
        s = s2
    return "soorrry"


print(foo(boo)[:26])
