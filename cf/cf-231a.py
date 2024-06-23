n = int(input())
s = 0
for _ in range(n):
    s += sum(int(x) for x in input().split(" ")) >= 2
print(s)
