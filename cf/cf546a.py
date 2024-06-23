k, n, w = (int(c) for c in input().split())
print(max(k * w * (w + 1) // 2 - n, 0))
