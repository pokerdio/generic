from turtle import * 
from random import random


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
    
def tree (lv):
    if not lv:
        return;
    branch, angle, length = lv[0];
    lv = lv[1:];
    push();
    rt((branch - 1) * angle * 0.5);
    for i in range (branch):
        push();
        fd(length);
        tree(lv);
        pop();
        lt(angle);
    pop();

def zig (n, length):
    n = max (1, n);
    d = length / (n * 2 + 2);
    fd (d);
    for i in range (n):
        rt (90);
        fd (d);
        lt (90);
        fd (d);
        lt (90);
        fd (d * 2);
        rt (90);
        fd (d);
        rt (90);
        fd (d);
        lt (90);
    fd (d);

def zig_gon(d, n):
    for i in range(n):
        zig(d // 15 + 2, d);
        rt(360/n);
