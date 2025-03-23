import re

def getPozInts(s):
    return [int(w) for w in re.findall("[0-9]+", s)]

program = getPozInts(open("day17_input.txt").read())
regA, regB, regC = program[:3]
program = program[3:]

opname = {0:"adv", 1: "bxl", 2: "bst", 3: "jnz", 4:"bxc", 5:"out", 6:"bdv", 7:"cdv"}


def comboValue(val, regA, regB, regC):
    if val >= 0 and val <= 3:
            return val
    if val == 4:
        return regA
    if val == 5:
        return regB
    if val == 6:
        return regC
    assert(False)

def RunUnsafe(regA, regB, regC, program, ret, self_match = False):
    ir = 0  # instruction register

    while ir >= 0 and ir < len(program) - 1:
        #print(ir, "before", opname[program[ir]], f"({program[ir]})", program[ir + 1], "out", ret, "regs", regA, regB, regC)
        if program[ir] == 0: #adv  division
            regA //= 2 ** comboValue(program[ir + 1], regA, regB, regC)
            ir += 2
        elif program[ir] == 1: #bxl  bitwise xor
            regB ^= program[ir + 1]
            ir += 2
        elif program[ir] == 2: #bst
            regB = comboValue(program[ir + 1], regA, regB, regC) % 8
            ir += 2
        elif program[ir] == 3:  #jnz  jump if not zero
            if regA:
                ir = program[ir + 1]
            else:
                ir += 2
        elif program[ir] == 4: # bxc   bitwise xor of b&c
            regB ^= regC
            ir += 2 # ignores operand for "legacy reasons"
        elif program[ir] == 5: #out
            ret.append(comboValue(program[ir + 1], regA, regB, regC) % 8)
            if self_match and out[-1] != program[len(out)]:
                assert(False)
            ir += 2
        elif program[ir] == 6: #bdv  division
            regB = regA // 2 ** comboValue(program[ir + 1], regA, regB, regC)
            ir += 2
        elif program[ir] == 7: #cdv  division
            regC = regA // 2 ** comboValue(program[ir + 1], regA, regB, regC)
            ir += 2
        #print(ir, "after", "out", ret, "regs", regA, regB, regC)
    return ret

def Run(regA=regA, regB=regB, regC=regC, program=program):
    ret = []
    try:
        RunUnsafe(regA, regB, regC, program, ret)
    except:
        pass
    return ret

print(",".join(str(x) for x in Run()))

def strCombo(val):
    if val < 4:
        return str(val)
    if val == 4:
        return "regA"
    if val == 5:
        return "regB"
    if val == 6:
        return "regC"

def printProg(program):
    global opname
    for i in range(0, len(program), 2):
        if program[i] in (0, 2, 5, 6, 7):
            print(opname[program[i]], strCombo(program[i + 1]))
        elif program[i] == 4:
            print(opname[program[i]], "_")
        else:
            print(opname[program[i]], program[i + 1])


def abovepow(val):
    pow2 = 1
    for i in range(1000):
        if pow2 > val: 
            return i, 2 ** i
        pow2 *= 2

def prog_compat(source, new):
    return len(new) <= len(source) and source[:len(new)] == new

def advance(a, bits, demand):
    global regA, regB, regC, program
    above_a = 2 ** bits
    
    keep = set()

    for i in range(4096):
        new_a = a + above_a * i
        v = Run(new_a)
        if v[:demand] == program[:demand]:
            if demand >= len(program) and v == program:
                return new_a
            keep.add(a + above_a * (i & 7))

    for new_a in sorted(list(keep)):
        ret = advance(new_a, bits + 3, demand + 1)
        if ret:
            return ret


# bst regA    regB = regA % 8
# bxl 5       regB ^= 5                          0->5 1->4 2->7 3->6 4->1 5->0 6->3 7->2
# cdv regB    regC = regA div (2 ** regB)
# bxl 6       regB ^= 6
# bxc _       regB ^= regC
# out regB    out regB
# adv 3       regA = regA div 8
# jnz 0       if regA != 0 goto 0
