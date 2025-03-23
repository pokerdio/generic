import re

def convert_line(s):
    return [int(word) for word in re.split("[-,]", s)]

def inside(a, b, c, d):
    return (a <= c and b >= d) or (a >= c and b <= d)

lines = [convert_line(s.strip()) for s in open("day4_input.txt").readlines()]


print(sum(inside(*v) for v in lines))

def intersect(a, b, c, d):
    return not (a > d or b < c)


print(sum(intersect(*v) for v in lines))
