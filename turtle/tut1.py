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

cfg = {"brick_x": 100, "brick_y": 30, "n_horiz": 14, 
       "n_vert": 7, 
       "odd":False,
       "y_mul": 1.15};

def flip_color():
    r = random();
    if r < 0.33:
        fillcolor((0.5, 0.25, 0.13));
    elif r < 0.66:
        fillcolor((0.65, 0.3, 0.23));
    else:
        fillcolor((0.8, 0.4, 0.3));

def flip_color2():
    r = random();
    if r < 0.33:
        fillcolor((1.0, 0.5, 0.5));
    elif r < 0.66:
        fillcolor((0.5, 0.5, 1.0));
    else:
        fillcolor((0.5, 1.0, 0.5));


def brick():

#    cfg["odd"] = not cfg["odd"];
    flip_color2();

    begin_fill();
    pd();
    fd(cfg["brick_x"]);
    right(90);
    fd(cfg["brick_y"]);
    right(90);
    fd(cfg["brick_x"]);
    right(90);
    fd(cfg["brick_y"]);
    right(90);
    pu();
    fd(cfg["brick_x"]);
    end_fill();

def bricks(n):
    for i in range(n):
        brick();

def two_rows():
    bricks(cfg["n_horiz"])
    pu();
    left(90);
    cfg["brick_y"] *= cfg["y_mul"];
    fd(cfg["brick_y"]);
    left(90);
    fd(cfg["brick_x"] * (cfg["n_horiz"] - 0.5))
    left(180);
    bricks(cfg["n_horiz"] - 1)
    cfg["brick_y"] *= cfg["y_mul"];
    pu();
    left(90);
    fd(cfg["brick_y"]);
    left(90);
    fd(cfg["brick_x"] * (cfg["n_horiz"] - 1.5))
    left(180);
    cfg["n_horiz"] -= 2;


def go():
    reset()
    pu();
    goto(-600, -500);
    pd();
    shape("turtle")
    speed(10)
    width(5)

    turtlesize(5.0, 5.0, 3.0)
    for _ in range(cfg["n_vert"]):
        two_rows()




