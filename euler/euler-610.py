def below_m():
    hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    units = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    ret = {}
    for i in range(0, 1000):
        u = i % 10
        t = (i // 10) % 10
        h = (i // 100) % 10
        ret[hundreds[h] + tens[t] + units[u] + "#"] = i
    return ret


def char_weight(c):
    return 1 if c == "#" else 7


def solve(s="", d=below_m()):
    """get the ev for the numbers lower than 1000 - note none of them starts with M"""
    total = 0
    total_weight = 0

    v = [q for q in d if q.startswith(s)]
    if not v:
        return None
    if len(v) == 1:
        return d[v[0]]

    for c in "IVXLCDM#":
        ev = solve(s + c)
        if ev != None:
            w = char_weight(c)
            total_weight += w
            total += w * ev
    return total / total_weight


def m_m():
    """adjust the ev for the case the number starts with a M"""
    m = 7 / 50  # odds of starting with a m
    notm_ev = solve()  # ev for starting with not m

    # ret = (ret + 1000) * m + notm_ev * (1.0 - m)  # our answer appears on both sides because M can repeat
    # ret(1-m) = 1000*m + notm_ev * (1.0 - m)

    return (1000 * m) / (1.0 - m) + notm_ev


def m_m():
    return 7000.0 / 43.0 + solve()
