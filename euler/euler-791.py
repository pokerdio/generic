import random as rnd


def foo():
    a, b, c, d = (rnd.randint(1, 1000) for _ in range(4))
    print(a, b, c, d)
    m = (a + b + c + d) * 0.5
    v = 0.25 * ((m - a)**2 + (m-b)**2 + (m-c)**2 + (m-d)**2)
    v2 = 0.25*0.25 * (a * a + b * b + c * c + d * d)

    return v - v2


def bar(a, b, c, d):
    return a * a + b * b + c * c + d * d - 2 * (a + b + c + d)


def goo(a, b, c, d):
    m = (a + b + c + d) * 0.25
    v = 0.25 * ((m - a)**2 + (m-b)**2 + (m-c)**2 + (m-d)**2)
    v2 = 0.25 * 0.25 * (a * a + b * b + c * c + d * d)

    print(v, v2)
