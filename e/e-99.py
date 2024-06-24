pairs = set()
for s in open("p099_base_exp.txt").readlines():
    pairs.add(tuple(int(w) for w in s.split(",")))


print(max(pairs, key=lambda x: x[0] ** x[1]))
