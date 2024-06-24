from itertools import combinations as comb


k = "0123456789"


def sixtynine(twodigitset):
    return set("".join(sorted(c if c != "9" else "6" for c in s)) for s in twodigitset)


sq = set(["".join(sorted("%.2d" % (x * x))) for x in range(1, 10)])
sq = sixtynine(sq)


count = 0
for a in comb(k, 6):
    for b in comb(k, 6):
        s = {"".join(sorted(ca + cb)) for ca in a for cb in b}
        s = sixtynine(s)
        if s & sq == sq:
            count += 1

print(count // 2)
