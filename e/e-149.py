from itertools import islice


def maxsum(v):
    s = 0
    maxs = 0
    for i in range(len(v)):
        if v[i] + s > 0:
            s = v[i] + s
        else:
            s = 0
        if maxs < s:
            maxs = s
    return maxs


def f1(k):
    return (100003 - 200003 * k + 300007 * (k ** 3)) % 1000000 - 500000


def r():
    s = [f1(k) for k in range(1, 56)]

    for i in s:
        yield i

    while True:
        i = (s[31] + s[0] + 1000000) % 1000000 - 500000
        yield i
        s[:-1] = s[1:]
        s[-1] = i

        # s.append(i)
        # s.pop(0)


def rn(n):
    return list(islice(r(), n))


n = 2000
n2 = n * n
v = rn(n2)


# n = 4
# n2 = n * n
# v = [-2, 5, 3, 2, 9, -6, 5, 1, 3, 2, 7, 3, -1, 8, -4, 8]


horiz = [maxsum(v[i:i + n]) for i in range(0, n2, 2000)]
vert = [maxsum(v[i: n2: n]) for i in range(2000)]

diag1a = [maxsum(v[i:n * i + 1: n - 1]) for i in range(n)]
diag1b = [maxsum(v[i * n + n - 1:n2 - n + i + 1: n - 1]) for i in range(n)]


diag2a = [maxsum(v[i:n2:n + 1]) for i in range(n)]
diag2b = [maxsum(v[n * i:n2 - i:n + 1]) for i in range(1, n)]


print(max(horiz + vert + diag1a + diag1b + diag2a + diag2b))
