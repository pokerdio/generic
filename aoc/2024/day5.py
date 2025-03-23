input = [s.strip() for s in open("day5_input.txt").readlines()]

split = input.index("")
rules, orders = [input[:split], input[split+1:]]

rules = [[int(s) for s in r.split("|")] for r in rules]
orders = [[int(s) for s in o.split(",")] for o in orders]


rule_dict = {}

for r in rules:
    rule_dict[tuple(r)] = 1
    rule_dict[(r[1], r[0])] = -1

def bubbleSort(v):
    for i in range(len(v)-1):
        for j in range(i+1, len(v)):
            if rule_dict.get((v[i], v[j]), 0) < 0:
                tmp = v[i]
                v[i] = v[j]
                v[j] = tmp
            
    
def problim():
    ret1 = 0
    ret2 = 0
    for o in orders:
        ok = True
        for i in range(len(o) - 1):
            for j in range(i + 1, len(o)):
                if (rule_dict.get((o[i], o[j]), 0) < 0):
                    ok = False
                    break
            if not ok:
                break
        if ok:
            ret1 += o[len(o) // 2]
        else:
            bubbleSort(o)
            ret2 += o[len(o) // 2]
    return ret1, ret2

print (problim())
