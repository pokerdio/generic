def bounce(x0, y0, xc, yc):
    pass


bar = 666


def foo():
    global bar
    i = 666
    print(list(globals().keys()))

    if "i" in locals():
        print("no okay")


def f(a, b, /):
    print(a, b)
