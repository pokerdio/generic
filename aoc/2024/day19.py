pat, design = open("day19_input.txt").read().split("\n\n")
pat = pat.split(", ")
design = design.split("\n")
if not design[-1]:
    design.pop()


def solveDesign(des):
    n = len(des)
    ok = [False] * (n + 1)
    ok[0] = True

    combo = [0] * (n + 1) # count of combinations for part two
    combo[0] = 1
    for idx in range(n): 
        if ok[idx]:
            s = des[idx:]
            for p in pat: 
                m = len(p) + idx 
                if m <= n and s.startswith(p):
                    ok[m] = True
                    combo[m] += combo[idx]
    return ok[n], combo[n]


def problim():
    return sum(solveDesign(des)[0] for des in design), \
        sum(solveDesign(des)[1] for des in design)

print(problim())
