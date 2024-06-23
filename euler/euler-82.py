#!/usr/bin/env python3

# https://projecteuler.net/problem=82


m = [[int(s) for s in line.split(",")] for line in open("p082_matrix.txt").readlines()]
open_node = {(0, y): m[y][0] for y in range(len(m))}
closed_node = {}


def add_node(x, y, value):
    global open_node, closed_node
    xy = (x, y)
    if xy in closed_node and closed_node[xy] < value:
        return
    if xy in open_node and open_node[xy] < value:
        return
    if xy in closed_node:
        del closed_node[xy]
    open_node[xy] = value


def expand_node(xy):
    x, y = xy
    global m, open_node, closed_node
    closed_node[xy] = open_node[xy]
    del open_node[xy]
    value = closed_node[xy]

    if x < len(m[0]) - 1:
        add_node(x + 1, y, value + m[y][x + 1])
    if y < len(m) - 1:
        add_node(x, y + 1, value + m[y + 1][x])

    if y > 0:
        add_node(x, y - 1, value + m[y - 1][x])


def go():
    global m, open_node, closed_node
    while open_node:
        expand_node(next(iter(open_node)))
    print(min(closed_node[(len(m[0]) - 1, y)] for y in range(len(m))))
