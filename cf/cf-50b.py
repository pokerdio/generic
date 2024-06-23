s = input()


d = {}
for c in s:
    d[c] = d.get(c, 0) + 1

print(sum(x * x for x in d.values()))
