
def sevens_factorial(n):
    s, i = 0, 7

    while n >= i:
        s += n // i
        i *= 7
    return s


def sevens_number(n):
    s = 0
    while (n % 7 == 0):
        n //= 7
        s += 1
        if (n == 0):
            break
    return s


def goline(n):
    num_sevens, b = 0, 0
    s = 0
    c = 1
    for i in range(1, n):
        k = sevens_number(i)
        j = sevens_number(n + 1 - i)
        num_sevens += j - k

        c *= n + 1 - i
        c //= i

        backup_sevens = sevens_number(c)
#        print("multiply by %d(%d) divide by %d(%d); sevens %d; c = %d; backup sevens %d" %
#              (n + 1 - i, j, i, k, num_sevens, c, backup_sevens))

        assert(backup_sevens == num_sevens)
        assert(num_sevens >= 0)
        if (num_sevens > 0):
            s += 1

    return s


def gotest(n):
    """slow, brute force solver, used for testing"""
    s = 0
    for i in range(1, n):
        s += goline(i)
    return s


from PIL import Image


def putpixel(pixels, x, y, size, color):
    size = max(size, 1)
    fillsize = size if size < 4 else size - 1

    x *= size
    y *= size
    for dx in range(fillsize):
        for dy in range(fillsize):
            pixels[x + dx, y + dy] = color


def gopic(pixel_size, n):
    """displays seven divisibility in Pascal's triangle
    different colors for powers of 7"""
    img = Image.new('RGB', (n * pixel_size + 1, n * pixel_size + 1), 0x333333)
    pixels = img.load()

    colors = [0, 0xff0000, 0x00ff00, 0x0000ff, 0xff00ff, 0xffff00, 0x00ffff]

    for i in range(1, n):
        k = 0

        putpixel(pixels, 0, i, pixel_size, 0)
        putpixel(pixels, i, i, pixel_size, 0)

    #    print("i ", i)
        for j in range(1, i + 1):
            #        print("multiply by", i + 1 - j, "divide by", j)
            k += sevens_number(i + 1 - j)
            k -= sevens_number(j)
            putpixel(pixels, j, i, pixel_size, colors[k])

    img.show()


#gopic(4, 240)


def go2(n):
    #print("go2", n)
    sevens = 1

    if n <= 7:
        return 0

    while sevens * 7 < n:
        sevens *= 7

    k = n // sevens
    #print("k=", k)

    s = k * (k - 1) // 2 * (sevens - 1) * sevens // 2

    #print("stage 1", s)

    s += k * (k + 1) // 2 * go2(sevens)
    #print("stage 2", s)
    q = n % sevens

    s += k * (sevens - 1 + sevens - q) * q // 2
    #print("stage 3", s)
    s += (k + 1) * go2(q)
    #print("stage 4", s)
    return s


def go(n):
    """solves it right"""

    return n * (n + 1) // 2 - go2(n)


def test(n):
    """test solver and slow solver"""
    for i in range(1, n + 1):
        a, b = gotest(i), go2(i)
        print(i, a, b)
        if a != b:
            break
    return True

# test(500)
#gopic(8, 120)


print(go(10**9))
