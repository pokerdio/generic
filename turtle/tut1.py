from turtle import * 
from random import random
from math import sin

def make_push_pop():
    pos_stack = [];
    rot_stack = [];
    def push():
        pos_stack.append(pos())
        rot_stack.append(heading())
    def pop():
        if pos_stack:
            setpos(pos_stack.pop())
            setheading(rot_stack.pop())
    return push, pop

push, pop = make_push_pop()
    

def zig_gon(d, n):
    for i in range(n):
        zig(d // 15 + 2, d);
        rt(360/n);

def go():
    reset()
    shape("turtle")
    speed(2)
    width(5)
    turtlesize(5.0, 5.0, 3.0)
    a = 10
    d = 80
    dd = d * sin(a * 6.28 / 360)
    pu()
    goto(0, 500)
    for i in range(36):
        pd()
        fd(d)
        left(90-a)
        fd(d)
        left(90+a)
        fd(d+2*dd)
        left(90+a)
        fd(d)
        left(90-a)
        pu()
        fd(d)
        right(a)
    pu()
    fd(600)


