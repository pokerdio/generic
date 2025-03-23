from itertools import combinations


v = [s.strip().split("-") for s in open("day23_input.txt").readlines()]

d = {}

for a, b in v:
    d[a] = d.get(a, [])
    d[b] = d.get(b, [])
    d[a].append(b)
    d[b].append(a)

for a in d.keys():
    d[a] = set(d[a])
    
def problim():
    ret = set()
    for a in d.keys():
        if not a.startswith("t"):
            continue
        for b in d[a]:
            for c in d[a]:
                if b == c:
                    continue
                if c in d[b]:
                    triple = tuple(sorted((a, b, c)))
                    if len(set(triple)) == 3: 
                        ret.add(triple)
    
    return ret

print(len(problim()))

def test_lan(lan):
    for a in lan:
        for b in lan:
            if a != b and b not in d[a]:
                return False
    return True

def problim2():
    best = 0
    best_set = None
    for a in d.keys(): # min computer in the connected party
        va = [b for b in d[a] if b > a]

        for alen in range(best, len(va) + 1):
            for subset in combinations(va, alen):
                if test_lan(subset):
                    best = alen + 1
                    best_set = [a, *subset]
    print(",".join(sorted(best_set)))
    return best_set

problim2()
