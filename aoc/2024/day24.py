import re
from itertools import product
from random import random

#input = open("day24_input.txt").readlines()

wires, gates = open("day24_input.txt").read().split("\n\n")

wires = [s.strip().split(":") for s in wires.split("\n")]
for w in wires:
    w[0] = w[0].strip()
    w[1] = int(w[1])
wires = {a:b for a, b in wires}
n = int(max(x for x in wires if x.startswith("x"))[1:]) + 1

def wireName(prefix, idx):
    leading_zero = "0" if idx < 10 else ""
    return prefix + leading_zero + str(idx)

gates = [s.strip().split() for s in gates.split("\n")]
if not gates[-1]:
    gates = gates[:-1]

def saveInput():
    global original
    original = [{a:b for a, b in wires.items()}, gates[:]]

saveInput()


def loop(wires, gates, involved = None):
    ret = False
    for idx in range(len(gates)):
        op1, typ, op2, _, dest = gates[idx]
        if op1 in wires and op2 in wires and dest not in wires: 
            ret = True
            if involved != None: 
                involved[dest] = involved.get(op1, ()) + involved.get(op2, ()) + (idx,)
            match typ: 
                case "AND":
                    wires[dest] = 1 if wires[op1] and wires[op2] else 0
                case "OR":
                    wires[dest] = 1 if wires[op1] or wires[op2] else 0
                case "XOR":
                    wires[dest] = 1 if wires[op1] ^ wires[op2] else 0
    return ret

def zInt(wires):
    ret = ""
    for z in sorted([key for key in wires.keys() if key.startswith("z")]):
        ret = str(wires[z]) + ret 
    return int(ret, 2)

def problim():
    while loop(wires, gates):
        pass
    return zInt(wires)

print(problim())



def desiredZ(wires, n):
    ret = {}
    ret["z00"] = wires["x00"] ^ wires["y00"]
    carry = 1 if wires["x00"] and wires["y00"] else 0
    n = int(max(w for w in wires if w.startswith("x"))[1:]) + 1

    for idx in range(1, n + 1):
        s = wires.get(wireName("x", idx), 0) + wires.get(wireName("y", idx), 0) + carry
        carry = s // 2
        ret[wireName("z", idx)] = s % 2
    return ret



def makeTestCase(bit, n):
    ret = {}
    for i in range(n):
        prefix = "0" if i < 10 else ""
        ret["x" + prefix + str(i)] = 1 if i == bit else 0
        #ret["y" + prefix + str(i)] = 1 if i == bit else 0
        ret["y" + prefix + str(i)] = 0
    return ret


def makeRandomCase(n):
    ret = {}
    for i in range(n):
        prefix = "0" if i < 10 else ""
        ret["x" + prefix + str(i)] = 1 if random() > 0.5 else 0
        ret["y" + prefix + str(i)] = 1 if random() > 0.5 else 0
    return ret


def testRandom(n = n):
    for _ in range(30): 
        wires = makeRandomCase(n)
        des = zInt(desiredZ(wires, n))
        while loop(wires, gates):
            pass
        actual = zInt(wires)
        if des != actual:
            return False
    return True

def swapGates(a, b, gates):
    gates[a][4], gates[b][4] = gates[b][4], gates[a][4]

def buildSwapOptions():
    global gates
    swap_options = []

    for bit in range(n):
        wires = makeTestCase(bit, n)

        des = desiredZ(wires, n)
        inv = {}
        while loop(wires, gates, inv):
            pass

        if zInt(des) != zInt(wires):
            suspect = set()
            for idx in range(n + 1):
                z = wireName("z", idx)
                if z not in des or z not in wires: 
                    return des, wires
                if des[z] != wires[z]:
                    suspect |= set(inv[z])

            swap = []
            for a in suspect:
                for b in suspect:
                    if a != b:
                        swapGates(a, b, gates)
                        test = makeTestCase(bit, n)
                        des = zInt(desiredZ(test, n))
                        while loop(test, gates):
                            pass
                        if (len([z for z in test if z.startswith("z")]) == n + 1 and des == zInt(test)):
                            print("swappable", gates[a], gates[b], a, b)
                            swap.append([a, b])
                        swapGates(a, b, gates)
            if swap:
                swap_options.append(swap)

    return swap_options


    # return ret


def attemptSwap(v):
    for x in product(*v):
        for a, b in x: 
            swapGates(a, b, gates)
        if testRandom(n):
            print ("WIN", ",".join(sorted([gates[i][4] for i in x[0]+x[1]+x[2]+x[3]])))
        for a, b in x: 
            swapGates(a, b, gates)
    
attemptSwap(buildSwapOptions())
