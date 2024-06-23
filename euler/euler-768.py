import turtle
from builtins import sum


def tri(side):
    for i in range(3):
        my_pen.fd(side)
        my_pen.left(120)
        side -= 10


tut = turtle.Screen()
tut.bgcolor("green")
tut.title("Das Gerat")
turtle.speed('fastest')
my_pen = turtle.Turtle()
my_pen.color("orange")
my_pen.speed(0)
tut = turtle.Screen()


def gon_xy(x, a, zerox=0, zeroy=0, side=20):
    retx, rety = zerox + side * cos(a * x), zeroy + side * sin(a * x)
    return retx, rety


def tutdraw(n, k, v, count):
    zerox = -300 + (count % 10) * 50
    zeroy = -300 + (count // 10) * 50

    a = 2 * pi / n
    my_pen.pu()
    my_pen.goto(*gon_xy(0, a, zerox, zeroy))
    my_pen.pd()
    for i in range(n):
        my_pen.goto(*gon_xy(i + 1, a, zerox, zeroy))

    for i in range(n):
        if v[i]:
            my_pen.pu()
            my_pen.goto(zerox, zeroy)
            my_pen.pd()
            my_pen.goto(*gon_xy(i, a, zerox, zeroy))
    tut.onclick(None)


def foo(n=12, k=3):
    count = 0
    twopi = pi * 2
    for i in range(2 ** (n - 1)):
        if i % 10000 == 0:
            print("...", i)

        j = i * 2 + 1
        v = [int(j & 2 ** x > 0) for x in range(n)]

        if sum(v) != k:
            continue
        if abs(sum(cos(twopi * x / n) for x in range(n) if v[x])) > 0.001:
            continue
        if abs(sum(sin(twopi * x / n) for x in range(n) if v[x])) > 0.001:
            continue

        tutdraw(n, k, v, count)
        count += 1


try:
    turtle.tracer(0, 0)
    foo(18, 5)
    turtle.update()
    tut.exitonclick()
except Exception:
    print("fuuuu")
    turtle.bye()
finally:
    print("godddd")
    turtle.bye()
