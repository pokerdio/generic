
def step(n):
    return (1504170715041707 * n) % 4503599627370517


def go():
    small, big = 1504170715041707, 1504170715041707
    s = small

    while True:
        new = (small + big) % 4503599627370517
        if new == 0:
            return s
        if new < small:
            small = new
            s += small
        elif new > big:
            big = new
        else:
            print("error", small, big, new)
            return
