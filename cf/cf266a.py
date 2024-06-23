n = int(input())
col = input()


count = 0
for s in ["RR", "GG", "BB"]:
    while s in col:
        col = col.replace(s, s[1], 1)
        count += 1
print(count)
