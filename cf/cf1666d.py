from collections import Counter as C
test_count = int(input())
tests = [input().split() for _ in range(test_count)]
# test_count = 1
# tests = [["DETERMINED", "TRME"],
#          ["DETERMINED", "TERM"],
#          ["PSEUDOPSEUDOHYPOPARATHYROIDISM", "PEPA"],
#          ["DEINSTITUTIONALIZATION", "DONATION"],
#          ["CONTEST", "CODE"],
#          ["SOLUTION", "SOLUTION"]]

for a, b in tests:
    a = "".join(c for c in a if c in b)
    ca, cb = C(a), C(b)
    aa = []
    for c in a:
        if ca[c] <= cb[c]:
            aa.append(c)
        else:
            ca[c] -= 1
    if "".join(aa) == b:
        print("YES")
    else:
        print("NO")


def foo(n):
    for i in range(n):
        if i == 7:
            print("BREAK")
            break
    else:
        print("ELSE")
