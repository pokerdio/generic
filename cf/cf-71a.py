n = int(input())


def foo(s):
    return len(s) > 10 and (s[0] + str(len(s) - 2) + s[-1]) or s


for _ in range(n):
    print(foo(input()))
