def between(x, a, b):
    a, b = (min(a, b), max(a, b))
    return (x >= a and x <= b)


def foo(a, b, f, want, k=10):
    fa = f(a)
    fb = f(b)
    for _ in range(k):
        mid = (a + b) / 2.0
        fmid = f(mid)

        if between(want, fa, fmid):
            b = mid
            fb = fmid
        elif between(want, fmid, fb):
            a = mid
            fa = fmid
        else:
            print("error")
            return mid, fmid

    return mid, fmid


def f(r):
    s = 0.0
    for k in range(1, 5001):
        s += (900.0 - 3 * k) * r ** (k - 1)
    return s


print("%.12f" % foo(1.0005, 1.005, f, -6 * 10**11, 60)[0])
