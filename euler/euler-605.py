from fractions import Fraction as F


class F2:
    def simp(self):
        while self.twos > 0 and self.nm % 2 == 0:
            self.twos -= 1
            self.nm //= 2

    def __init__(self, numerator, twos):
        self.nm = numerator
        self.twos = twos
        self.simp()

    def __neg__(self):
        return F2(-self.nm, self.twos)

    def __add__(self, val):
        a, b = self, val
        if a.twos < b.twos:
            a, b = b, a
        if a.twos == b.twos:
            return F2(a.nm + b.nm, a.twos)  # the constructor it simps
        else:
            return F2(a.nm + b.nm * (2 ** (a.twos - b.twos)), a.twos)

    def __repr__(self):
        if self.twos == 0:
            return str(self.nm)
        elif self.twos == 1:
            return "%d/2" % self.nm
        return "%d/2**%d" % (self.nm, self.twos)

    def __mul__(self, val):
        return F2(self.nm * val.nm, self.twos + val.twos)


def pow_matrix(matrix, n):
    v = []
    while n > 0:
        print("pow", n)
        if n % 2 == 0:
            n //= 2
            matrix = mul33(matrix, matrix)
        else:
            v.append(matrix)
            n -= 1
    ret = v[0]
    for i in range(1, len(v)):
        print("pow2 %d/%d" % (i, len(v)))
        ret = mul33(ret, v[i])
    print("kapow over")
    return ret


def mul33(m1, m2):
    zero = F2(0, 0)
    v = [[zero, zero, zero], [zero, zero, zero], [zero, zero, zero]]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                v[i][j] = v[i][j] + m1[i][k] * m2[k][j]
    return v


def det22(a, b, c, d):
    return a * d + (-b * c)


def minus33(m1, m2):
    print("enter minus")
    v = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(3):
        for j in range(3):
            v[i][j] = m1[i][j] + (-m2[i][j])
    print("exit minus33")
    return v


def inv33(m):
    a11, a12, a13 = m[0]
    a21, a22, a23 = m[1]
    a31, a32, a33 = m[2]
    print("inv33 start")
    det = (a11 * a22 * a33 + a31 * a12 * a23 + a13 * a21 * a32) + \
        (-(a31 * a22 * a13 + a21 * a12 * a33 + a11 * a32 * a23))

    print("inv33 mid")

    ret = [[det22(a22, a23, a32, a33),
            det22(a13, a12, a33, a32),
            det22(a12, a13, a22, a23)],
           [det22(a23, a21, a33, a31),
            det22(a11, a13, a31, a33),
            det22(a13, a11, a23, a21)],
           [det22(a21, a22, a31, a32),
            det22(a12, a11, a32, a31),
            det22(a11, a12, a21, a22)]], det
    print("inv33 exit")
    return ret


def go(n, m):
    half = F(1, 2)
    zero = F(0, 1)
    one = F(1, 1)
    a = [[half, zero, zero], [half, half, zero], [zero, half, zero]]
    i = [[one, zero, zero], [zero, one, zero], [zero, zero, one]]

    ret = 0
    for i in range(10):
        b = pow_matrix(a, m + n * i)
        print(b[-1][0], ret)
        ret += b[-1][0]
    return ret


def go2(n, m):
    half = F2(1, 1)
    zero = F2(0, 0)
    one = F2(1, 0)
    a = [[half, zero, zero], [half, half, zero], [zero, half, zero]]
    i = [[one, zero, zero], [zero, one, zero], [zero, zero, one]]

    b = pow_matrix(a, m)
    p = pow_matrix(a, n)

    astar, det = inv33(minus33(i, p))
    x = mul33(b, astar)[-1][0]

    return encode_fr_faith(x, det)


def encode_fr(x, det):
    twos = abs(x.twos - det.twos)

    f = F(x.nm, det.nm)
    return (f.numerator % 10**8) * (f.denominator % 10 ** 8) * ((2 ** twos) % 10 ** 8) % 10 ** 8


def encode_fr_faith(x, det):
    """assume they're coprime"""
    twos = abs(x.twos - det.twos)

    return (x.nm % 10**8) * (det.nm % 10 ** 8) * ((2 ** twos) % 10 ** 8) % 10 ** 8


# print(encode_fr(go2(10**8+7, 10**4+7)))
print(go2(10**8+7, 10**4+7))


# 59992576 correct
