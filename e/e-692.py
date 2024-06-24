def foo(n):
    if n == 1:
        return 1
    if n == 2:
        return 3
    if n == 3:
        return 6

    s = 6
    i = 3
    k = 1

    while True:
        if i + k >= n:
            return s + (n - i) * (n - i + 1) // 2
        s += k * (k + 1) // 2
        i += k

        i += 1
        s += i
        if i == n:
            return s
        k = i // 2


# 4 1
# 5 5
# 6 1
# H(7) == 2
# H(8) == 8
# H(9) == 1
# H(10) == 2
# H(11) == 3
# H(12) == 12
# H(13) == 1
# 14 2
# 15 3
# 16 4
# 17 5
# 18


def genh(n):
    h = list(range(1, 4)) + [0] * (n - 3)  # index is n-1 h[3] is H[4] from problem text

    if n < 4:
        return h[:n]
    for i in range(4, n + 1):
        h[i - 1] = i

        for j in range(1, i):
            if (h[i - j - 1] > j * 2):
                h[i - 1] = j
                break
    return h


def ph(n):
    return " ".join(str(i) for i in genh(n))


def foo(n):
    f1, f2 = 3, 5
    v = genh(n)
    s = "  +"
    ss = 0
    for i in range(len(v)):
        if v[i] == f1:
            print("%.5d %.5d" % (i + 1, f1), s[:-1], "=", ss)
            f1, f2 = f2, f1 + f2
            s = "  +"
            ss = 0
        else:
            s += str(v[i]) + "+"
            ss += f1


demanded_n = 23416728348467685


def bar(n):
    s0 = 3
    s1 = 7

    f0 = 3
    f1 = 5

    for _ in range(n):
        ff0, ff1 = f1, f0 + f1
        ss0, ss1 = s1, s0 + s1 + f1
        yield ff1, ss1 + ff1
        s0, s1, f0, f1 = ss0, ss1, ff0, ff1


def go(n):
    def goret(n=n, v=[]):
        if n < 10:
            return sum(genh(n))
        if not v:
            gen = bar(10000)
            v = [next(gen)]
            while v[-1][0] < n:
                v.append(next(gen))

        if v[-1][0] == n:
            return v[-1][1]
        else:
            return v[-2][1] + goret(n - v[-2][0])
    return goret


def testgo():
    n = 50000
    v = genh(n)
    s = [v[0]]
    for i in range(1, n):
        if go(i)() != s[-1]:
            print("ERROR", i, go(i)(), s[-1])
            return
        s.append(s[-1] + v[i])
    print("ALRIGHT.OKAY.YOU.WIN")


def psum(n):
    v = genh(n)
    s = 0
    for i in range(n):
        s += v[i]
        print(i + 1, s)


testgo()
print(go(demanded_n)())


def fibo(n):
    f1, f2 = 3, 5
    while f2 < n:
        f1, f2 = f2, f1 + f2
    return f2
