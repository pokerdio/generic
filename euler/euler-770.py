# g(give, take) = min((1 + x) * g(give-1, take), (1-x) * g(give, take - 1))

# (1+x) * a = (1-x) * b

# x(a+b) = b - a

# x = (b - a) / (a + b)
from math import log, exp


def do_layer(n, v):
    """a point in v is the ev of a game starting from a
    (index,n-1-index) pair meaning (gives,takes)"""
    v2 = [1.0]
    for gives in range(1, n):
        takes = n - gives

        a = v[gives - 1]
        b = v[gives]
        x = (b - a) / (a + b)
        v2.append((1 + x) * a)
    v2.append(2.0 * v[n-1])

    return v2


def do_layer2(v):
    """a point in v is the logarithmic ev of a game starting from a
    (index,n-1-index) pair meaning (gives,takes)"""
    n = len(v)
    if n % 100 == 0:
        print(n)

    v2 = [0.0]
    for gives in range(1, n):
        a = v[gives - 1]
        b = v[gives]

        #x = log(exp(b) - exp(a)) - log(exp(a) + exp(b))
        #x = log(exp(a)(exp(b-a) - 1)) - log(exp(a)(1+exp(b-a)))
        if b-a < 15:
            eba = exp(b-a)
            x = log(eba-1) - log(1+eba)
            if x < 15:
                x = log(1 + exp(x))
        else:
            x = 0
        v2.append(x + a)
    v2.append(log(2.0) + v[-1])

    return v2


def do_layer3(v):
    """a point in v is the ev of a game starting from a
    (index,n-1-index) pair meaning (gives,takes)"""
    n = len(v)
    if n % 100 == 0:
        print(n)

    v2 = [0.0]
    for gives in range(1, n):
        a = v[gives - 1]
        b = v[gives]

        #x = log(exp(b) - exp(a)) - log(exp(a) + exp(b))
        #x = log(exp(a)(exp(b-a) - 1)) - log(exp(a)(1+exp(b-a)))
        if b-a < 15:
            eba = exp(b-a)
            x = log(eba-1) - log(1+eba)
        else:
            x = 0
        v2.append(x + a)
    v2.append(log(2.0) + v[-1])

    return v2


def go(n):
    global midv
    v = [0.0]
    last = 0.0
    for i in range(2 * n):
        v = do_layer2(v)
        if i == n:
            midv = v
        if i >= n:
            v = v[1:-1]
        if i % 2 == 1:
            value = exp(v[len(v)//2])
            if last:
                print(i, value, value - last, value / last, 1 / (value - last))
            else:
                print(i, value)
            last = exp(v[len(v)//2])
        if i % 2 == 1 and exp(v[len(v) // 2]) > 1.7:
            print((i + 1) // 2)
            return
    print(v)
    return exp(v[0])


# print(go(100000))

# [0, 3]: 1.0 [1, 2]: g[2, 1]: g[3, 0]: 4.0
# [0, 2]: 1.0 [1, 1]: g[2, 0]: 4.0
# [0, 1]: 1.0 [1, 0]: 2.0
# [0, 0]: 1.0

# 2      2
# ----- -----
# 1   1  1   1
# - + - - + -
# a   b  c   b


# 2ab/a+b
# 2ac/a+c


# 2ab(a+c)+2ac(a+b) / (a+b)*(a+c)
# 2a*a(b+c)+4abc /
