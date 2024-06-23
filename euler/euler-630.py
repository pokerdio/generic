from fractions import Fraction as Fr


def tpairs():
    s = 290797
    for _ in range(5000):
        s = s ** 2 % 50515093
        t1 = s % 2000 - 1000

        s = s ** 2 % 50515093
        t2 = s % 2000 - 1000
        yield (t1, t2)


def slant(xy0, xy1):
    if xy0[0] == xy1[0]:
        return 9999999999.999  # doesn't need to be
    f = Fr((xy0[1] - xy1[1]), (xy0[0] - xy1[0]))
    return (f.numerator, f.denominator)


def para_count(lines):
    n = len(lines)
    if n == 1:
        return 1
    s = set()
    for line in lines:
        x0, y0 = line[0]
        x1, y1 = line[1]
        a, b, c = y0 - y1, x1 - x0, y1 * x0 - y0 * x1

        assert(a * x0 + b * y0 + c == 0)
        assert(a * x1 + b * y1 + c == 0)
        m = max((a, b, c), key=abs)
        s.add((Fr(a, m), Fr(b, m), Fr(c, m)))

    return len(s)


def go(n):
    tp = tpairs()
    p = list(set(next(tp) for _ in range(n)))

    lines = {}
    for i in range(n - 1):
        if i % 10 == 0:
            print("line_0", i)
        for j in range(i + 1, n):
            sl = slant(p[i], p[j])
            if sl not in lines:
                lines[sl] = []
            lines[sl].append((p[i], p[j]))

    para = [0] * 1000
    i = 0
    for sl in lines.values():
        i += 1
        if i % 1000 == 0:
            print("line_2", i)

        k = para_count(sl)
        para[k] = para.get(k, 0) + 1

    ret = 0
    print(para)
    for i in para.keys():
        ret += para[i] * (para[i] - 1) * i * i
        for j in para.keys():
            if i < j:
                ret += para[i] * para[j] * i * j * 2
    return ret
