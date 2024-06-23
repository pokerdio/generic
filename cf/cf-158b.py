from collections import Counter

n = int(input())
v = [int(x) for x in input().split(" ")]

#n = 5
#v = [1, 2, 4, 3, 3]

v = Counter(v)

s4 = v[4]

s3 = min(v[3], v[1])
v[3] -= s3
v[1] -= s3
s3 += v[3]

s2 = v[2] // 2
v[2] -= s2 * 2


s1 = (v[2] * 2 + v[1] + 3) // 4

print(s1 + s2 + s3 + s4)
