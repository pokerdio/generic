

def roman_to_num(s, v=[("M", 1000), ("CM", 900), ("D", 500), ("CD", 400),
                       ("C", 100), ("XC", 90), ("L", 50), ("XL", 40),
                       ("X", 10), ("IX", 9), ("V", 5), ("IV", 4), ("I", 1)]):
    s = s.upper().strip()

    ret = 0
    for prefix, value in v:
        while s.startswith(prefix):
            ret += value
            s = s[len(prefix):]

    return ret


def num_to_roman(n, v=[("M", 1000), ("CM", 900), ("D", 500), ("CD", 400),
                       ("C", 100), ("XC", 90), ("L", 50), ("XL", 40),
                       ("X", 10), ("IX", 9), ("V", 5), ("IV", 4), ("I", 1)]):
    ret = ""

    for s, value in v:
        while value <= n:
            ret += s
            n -= value
    return ret


def go():
    total = 0
    for s in open("p089_roman.txt", "r").readlines():
        s = s.strip()
        total += len(s) - len(num_to_roman(roman_to_num(s)))
    return total
