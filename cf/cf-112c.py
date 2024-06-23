n, x, y = (int(c) for c in input().split())
over = y - n + 1
if over < 1 or (over**2+n-1) < x:
    print(-1)
else:
    print(over)
    print("1\n" * (n - 1))
