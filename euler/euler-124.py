from primez import iterate_primez


def make_rad(n):
    a = [0] + [1] * (n - 1)
    for i in iterate_primez(n):
        a[i:n:i] = (a[j] * i for j in range(i, n, i))
    return a


def make_E(n):
    v = list(zip(make_rad(n + 1)[1:], range(1, n + 1)))
    return [x[1] for x in sorted(v)]


print(make_E(100000)[9999])
