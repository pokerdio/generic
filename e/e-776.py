from builtins import sum


def _go100(ndigitz, maxdigit=10):
    app = [0] * (9 * ndigitz + 1)
    multi = [0] * len(app)
    for i in range(1, 10 ** (ndigitz - 1) * maxdigit):
        s = sum(int(d) for d in str(i))
        app[s] += 1
        multi[s] += i
    return app, multi


def _go(n):
    ndigitz = len(str(n))
    app = [0] * (9 * ndigitz + 1)
    multi = [0] * len(app)
    for i in range(1, n + 1):
        s = sum(int(d) for d in str(i))
        app[s] += 1
        multi[s] += i
    return app, multi


def go100(ndigitz, maxdigit=10):
    if ndigitz == 1:
        return [0] + [1] * 9, list(range(10))
    app, multi = go100(ndigitz - 1)  # appearences of denominator x and total multiplier

    app2, multi2 = app.copy(), multi.copy()
    app2.extend([0, 0, 0, 0, 0, 0, 0, 0, 0])
    multi2.extend([0, 0, 0, 0, 0, 0, 0, 0, 0])

    ten = 10 ** (ndigitz - 1)
    for first_digit in range(1, maxdigit):
        for denominator in range(1, len(app)):
            app2[denominator + first_digit] += (app[denominator])
            multi2[denominator + first_digit] += first_digit * app[denominator] * ten + multi[denominator]

        app2[first_digit] += 1
        multi2[first_digit] += first_digit * ten
    return app2, multi2


def go(n):
    if n < 11:
        return _go(n)

    s = str(n)
    a = int(s[0])
    b = int(s[1:])

    a0, m0 = go100(len(s), a)
    a1, m1 = go(b)

    a0.extend([0, 0, 0, 0, 0, 0, 0, 0, 0])
    m0.extend([0, 0, 0, 0, 0, 0, 0, 0, 0])

    ten = 10 ** (len(s) - 1)
    a0[a] += 1
    m0[a] += a * ten

    for i in range(1, len(m1)):
        a0[i + a] += a1[i]
        m0[i + a] += m1[i] + a1[i] * ten * a

    return a0, m0


def stripzeros(v):
    while v and not v[-1]:
        v.pop()
    return v


def myeq(p1, p2):
    p1, p2 = ([stripzeros(x) for x in p] for p in (p1, p2))
    return p1 == p2


def gogo(n):
    a, m = go(n)

    ret = 0.0
    for i in range(1, len(m)):
        ret += m[i] / i
    return ret


# for i in range(2, 20000):
#     if not myeq(go(i), _go(i)):
#         print(i)
#         break


print(gogo(1234567890123456789))
