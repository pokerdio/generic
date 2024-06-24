def number_curve(n):
    """1 increasing 0 bouncy -1 decreasing
    all same digit makes -1 number"""
    s = str(n)
    up = "".join(sorted(s))
    if s == up[::-1]:
        return -1

    if s == up:
        return 1
    return 0


def bump_increasing(n):
    """generates the next bouncy number after an increasing number"""
    n = n + (10 - n % 10)
    if number_curve(n) == -1:
        return bump_decreasing(n)
    # since the last digit of n is now zero it cannot be increasing
    return n


def bump_decreasing(n):
    """generates the next bouncy after a decreasing (or flat) number"""
    last = n % 10
    second = (n % 100) // 10

    n += (second - last + 1)
    curve = number_curve(n)
    if curve == -1:
        return bump_decreasing(n)
    if curve == 1:
        return bump_increasing(n)
    return n


def bump(n):
    curve = number_curve(n)

    if curve == -1:
        return bump_decreasing(n)
    if curve == 1:
        return bump_increasing(n)

    return bump_bouncy(n)


def bouncy_break(n):
    s = str(n)
    ndigits = len(s)
    clast = s[0]
    klast = -1  # last place digits differ on the first up or down leg

    k = 1
    direction = 0
    for c in s[1:]:
        if direction == 1:
            if c < clast:
                break
            if c > clast:
                klast = k
        elif direction == -1:
            if c > clast:
                break
            if c < clast:
                klast = k
        else:
            if c > clast:
                direction = 1
                klast = k
            if c < clast:
                direction = -1
                klast = k

        clast = c
        k += 1

    return klast, direction, s


def bump_bouncy(n):
    k, d, s = bouncy_break(n)
    ls = len(s)

    if d == 1:
        return int(s[:k] + s[k] * (ls - k))
    if d == -1:
        return int(s[:k] + chr(ord(s[k]) + 1) + "0" * (ls - k - 1))


def nfrequency(a, b):
    """finds the first number for which the
    bouncy frequency is above a/b """
    assert(0 < a < b)

    bouncy = 0
    x = 100
    while True:
        y = bump(x)
        x = bump(y)

        xtra_bouncy = x - y
        if (bouncy + xtra_bouncy) * b >= a * (x - 1):
            for j in range(y, x):  # this wastes a huge amount of time; whatevs
                if (bouncy + j + 1 - y) * b >= a * j:
                    return j
            print("fuck")
            return

        bouncy += xtra_bouncy


print(nfrequency(99, 100))


def count_mono(n):
    if n <= 100:
        return n
    mono = 100
    x = 101
    while True:
        y = bump(x)
        x = bump(y)

        if x >= n:
            return mono + n - y
        mono += (x - y)
