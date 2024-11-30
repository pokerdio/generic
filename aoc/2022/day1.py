v = [line.strip() for line in open("day1_input.txt").readlines()]

def split(lst, sep):
    if not callable(sep):
        compare_with = sep
        sep = lambda x: x == compare_with

    ret = []
    current = []
    for item in lst:
        if sep(item) and current:
            ret.append(current)
            current = []
        else:
            current.append(item)
    if current:
        ret.append(current)
    return ret
        
v = [sum(int(x) for x in elf) for elf in split(v, "")]

print("top elf:", max(v))
print("top 3 elf", sum(sorted(v)[-3:])) 
