v = [[int(c) for c in list(line.strip())] for line in open("day10_input.txt").readlines()]
vis = [[False for _ in range(len(v[0]))] for _ in range(len(v))]



from itertools import chain
from collections import Counter 

def onMap(x, y):
    return x >= 0 and y >= 0 and x < len(v[0]) and y < len(v)

def neigh(x, y):
    for dx, dy in ((0, 1), (0, -1), (-1, 0), (1, 0)):
        if onMap(x + dx, y + dy):
            yield (x + dx, y + dy)

def hike(startx, starty):
    open = {(startx, starty):1}
    for height in range(1, 10):
        new_open = {}
        for xy, trail_count in open.items():
            for xy1 in neigh(xy[0], xy[1]):
                if v[xy1[1]][xy1[0]] == height:
                    new_open[xy1] = new_open.get(xy1, 0) + trail_count
        open = new_open
    return len(open), sum(open.values())


def problim():
    ret_peaks = 0
    ret_trails = 0
    for i in range(len(v)):
        for j in range(len(v[0])):
            if 0 == v[i][j]:
                peaks, trails = hike(j, i)
                ret_peaks += peaks
                ret_trails += trails
    return ret_peaks, ret_trails
