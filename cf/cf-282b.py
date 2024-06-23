n = int(input())

delta = 0
v = []
for _ in range(n):
    x = int(input().split(" ")[0])
    if abs(delta + x) <= 500:
        v.append("A")
        delta += x
    elif abs(delta - (1000 - x)) <= 500:
        v.append("G")
        delta -= (1000 - x)

print("".join(v))
