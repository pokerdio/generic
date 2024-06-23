def N(m):
    k = 0
    for t in range(100):
        if 4 ** t - 2 ** t < m:
            k += 1
        else:
            return k


def foo(frange):
    for i in frange:
        i = float(i)
        print("f(%.3f) = %.3f" % (i, 4 ** i - 2 ** i))


def bar(k):
    return (1 + math.sqrt(1 + 4 * k)) / 2.0


def boo(n):
    count = 0
    perfect_count = 0

    two = 1
    for i in range(3, n, 2):
        count += 1

        k = (i * i - 1) // 4
        two_t = (1 + i) // 2

        while two_t > two:
            two *= 2
        if two_t == two:
            perfect_count += 1
        if perfect_count and (count / perfect_count > 12345):
            print(k, two_t, count, perfect_count)
            print("!!!!")
            return


boo(2000000)
# 44043947822 209867 209866 17
#!!!!


# first number is right
