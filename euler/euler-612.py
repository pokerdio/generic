# dp grouping numbers by the set of digitz in their representation
# fail for encoding sets as sorted numbers (762 for {2,6,7}) and not bitmasks

def _go(n):
    ret = 0
    for i in range(1, n - 1):
        si = set(str(i))
        for j in range(i + 1, n):
            sj = set(str(j))
            if si & sj:
                ret += 1
    return ret


def _buckitz(n):
    num = {}
    for i in range(1, n):
        code = int("".join(sorted((c for c in set(str(i))), reverse=True)))
        num[code] = num.get(code, 0) + 1
    return num


def gen_transitions():
    s = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    d = {}
    for _ in range(10):
        o = s
        s = set()
        for code in o:
            code_set = set(int(c) for c in str(code))
            for x in range(10):
                xcode = int("".join(sorted((str(i) for i in (code_set | {x})), reverse=True)))
                d[(code, x)] = xcode
                if xcode not in o:
                    s.add(xcode)
    return d


def go(n):
    trans = gen_transitions()
    num = {x: 1 for x in range(1, 10)}

    num2 = num.copy()
    for _ in range(n - 1):
        num3 = {}
        for code, count in num2.items():
            for digit in range(10):
                new_code = trans[code, digit]
                num3[new_code] = (num3.get(new_code, 0) + count) % 1000267129
                num[new_code] = (num.get(new_code, 0) + count) % 1000267129
        num2 = num3

    ret = 0
    for code, count in num.items():
        for code2, count2 in num.items():
            if code == code2:
                ret += count * (count - 1) // 2
            elif (code > code2) and (set(str(code)) & set(str(code2))):
                #                print(f"{code}({count}) {code2}({count2}) +++{count*count2}")
                ret += count * count2
    return ret % 1000267129
