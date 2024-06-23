def gen_faces():
    n = 1
    saved = 2  # how much is saved summed over all cubes of the face
    delta = 2  # how much is saved per cube after adding the face

    yield 2, 2, 1  # saved, delta, count for 1x1
    while True:
        saved += delta * n + 4 * n + 3 * (n - 1) * n
        delta += 4 + 6 * (n - 1)
        yield saved, delta, n * (n + 1)
        n += 1
        saved += delta * n + 4 * n + 3 * (n - 1) * n
        delta += 4 + 6 * (n - 1)
        yield saved, delta, n * n


def goo(n):
    n -= 1
    x, y, z = 1, 1, 1
    yz = 0
    saved, delta = 0, 0

    g = gen_faces()

    while y * z <= n:
        n -= y * z
        if yz != y * z:
            s2, d2, yz2 = next(g)
            yz = y * z
            assert yz == yz2
        saved += y * z * delta + s2
        delta += d2

        x, y, z = sorted((x + 1, y, z))
    if n > 0:
        g = gen_faces()
        s2, d2, yz = next(g)
        while True:
            s3, d3, yz3 = next(g)
            if yz3 <= n:
                s2, d2, yz = s3, d3, yz3
            else:
                break
        n -= yz
        saved += s2 + yz * delta
        delta += d2
    if n > 0:
        saved += delta * n + 4 * n + 3 * (n - 1) * n
    return saved


print(goo(10**16) % 1000000007)
