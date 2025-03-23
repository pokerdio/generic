v = [[int(s) for s in line.strip().split()] for line in open("day1_input.txt").readlines()]
v2 = list(zip(*v))
a = sorted(v2[0])
b = sorted(v2[1])


print(sum(abs(a[i] - b[i]) for i in range(len(a))))


from collections import Counter

c = Counter(b)

print(sum(x * c[x] for x in a))
