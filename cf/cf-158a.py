n, k = [int(x) for x in input().split(" ")]
v = [int(x) for x in input().split(" ")]


print(len([x for x in v if x >= max(0.5, v[k - 1])]))
