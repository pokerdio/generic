t = int(input())


for _ in range(t):
    n = int(input())
    v = list(int(c) for c in input().split())
    has_zero = 0 in v
    zero_count = v.count(0)
    has_equal = len(set(v)) < n
    if has_zero:
        print(n - zero_count)
    else:
        if has_equal:
            print(n)
        else:
            print(n + 1)
