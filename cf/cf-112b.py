n2, x, y = (int(c) for c in input().split())
n = n2//2

if x >= n and x <= n+1 and y >= n and y <= n + 1:
    print("NO")
else:
    print("YES")
