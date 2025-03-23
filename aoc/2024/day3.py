lines = [s.strip() for s in open("day3_input.txt").readlines()]
input_text = "".join(lines)
import regex as re

def mul(v):
    return v[0] * v[1]


def doLine(s):
    v = re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)", s)

    return sum([mul([int(x) for x in re.findall(r"[0-9]+", s)]) for s in v])


def doLines():
    print(sum(doLine(s) for s in lines))

def doLine2(s, pat_vet, pat_extract):
    v = pat_vet.findall(s)
    return sum([mul([int(x) for x in pat_extract.findall(s)]) for s in v])

def doLines2():
    pat_vet = re.compile(r"mul\([0-9]{1,3},[0-9]{1,3}\)")
    pat_extract = re.compile(r"[0-9]+")
    print(sum((doLine2(s, pat_vet, pat_extract)) for s in lines))


def doLine3(s, pat_vet, pat_extract): 
    v = pat_vet.findall(s)
    sum = 0
    okay = True
    for word in v:
        if word == "do()":
            okay = True
        elif word == "don't()":
            okay = False
        elif okay:
            nums = pat_extract.findall(word)
            sum += int(nums[0]) * int(nums[1])
    return sum

def doLines3():
    pat_vet = re.compile(r"mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don't\(\)")
    pat_extract = re.compile(r"[0-9]+")
    print(doLine3(input_text, pat_vet, pat_extract))    
