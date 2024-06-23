n, k = [int(c) for c in input().split(" ")]
a = sorted([int(c) for c in input().split(" ")])


if k > n:
    print("-1")
elif k == n:
    print("0 0")
elif k == 0:
    print(f"{10**9+1} " * 2)
elif a[-k] > a[-k-1]:
    print(f"{a[-k]} " * 2)
else:
    print(-1)
