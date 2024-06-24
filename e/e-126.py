
from itertools import count, islice


def layer(x, y, z, depth):
    """x>=y>=z cuboid; first layer is n=0"""
    s = 2 * y * z  # whole left and right new outside layers
    s += (2 * (y + z) + 4 * depth) * x  # around the original
    s += depth * (4 * (y + z + depth - 1))
    return s


def c(desired_total):
    explore = {(1, 1, 1, 0)}
    closed = set()
    future = set()
    totals = {}
    for n in count(2, step=2):
        if totals:
            print(n, len(closed), max(0, *totals.values()))
        while explore:
            xyzd = explore.pop()
            value = layer(*xyzd)

            if value > n:
                future.add(xyzd)
                continue

            totals[value] = totals.get(value, 0) + 1
            closed.add(xyzd)

            x, y, z, d = xyzd
            for newxyzd in ((x + 1, y, z, d), (x, y + 1, z, d),
                            (x, y, z + 1, d), (x, y, z, d + 1)):
                if (newxyzd[0] >= newxyzd[1]) and \
                        (newxyzd[1] >= newxyzd[2]) and (not newxyzd in closed):
                    explore.add(newxyzd)

        if totals.get(n, 0) == desired_total:
            return n
        explore = future
        future = set()
