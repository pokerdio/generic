n = int(input())

d = {}
for _ in range(n):
    s = input()
    if s in d:
        print(s + str(d[s]))
        d[s] += 1
    else:
        print("OK")
        d[s] = 1
