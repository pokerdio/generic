n = int(input())
v = [int(x) for x in input().split(" ")]

best = sum(v)


for i in range(3, n + 1):  # we try to keep i-gons
    if n % i == 0:
        delta = n // i  # distance between two statues of the same i-gon
        v2 = [0] * delta  # that distance is also the number of possible i-gons
        for j in range(n):
            v2[j % delta] += v[j]
        best = max(best, max(v2))
print(best)
