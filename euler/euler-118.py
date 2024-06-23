import primez
import itertools as it


def four_digit_comboz():
    zero = {}
    for p in primez.iterate_primez(10000):
        if len(set(str(p))) == len(str(p)) and ("0" not in str(p)):
            signature = "".join(sorted(str(p)))
            zero[signature] = zero.get(signature, set())
            zero[signature].add((p,))
    ret = zero.copy()
    while True:
        ret2 = {}
        for s1, comboz1 in ret.items():
            for s2, comboz2 in zero.items():
                if len(set(s1 + s2)) == len(s1) + len(s2):
                    s12 = "".join(sorted(s1 + s2))
                    v = ret2.get(s12, set())
                    for c1 in comboz1:
                        for c2 in comboz2:
                            v.add(tuple(sorted(c1 + c2)))
                    ret2[s12] = v
        k = False
        for s, comboz in ret2.items():
            if s in ret:
                before = len(ret[s])
                ret[s].update(comboz)
                if len(ret[s]) > before:
                    k = True
            else:
                ret[s] = comboz
                k = True
        if not k:
            print("ok boomer")
            break

    return ret


def prime_count_anagram(digit_lst):
    ret = 0

    if len(digit_lst) <= 6:
        test = primez.isprime
    else:
        test = primez.isprime_slow

    for combo in it.permutations(digit_lst):
        x = 0
        for i in range(len(combo)):
            x += combo[i] * 10 ** i
        if test(x):
            ret += 1

    return ret


def five_eight_comboz_count(fours_dick):
    ret = 0
    for s, comboz in fours_dick.items():
        if len(s) <= 4 and (sum(int(x) for x in s) % 3 > 0):
            anti_s = sorted([int(c) for c in set("123456789") - set(s)])
            pca = prime_count_anagram(anti_s)
            ret += len(comboz) * pca
            print(s, anti_s, len(comboz), pca)
    return ret

# no  prime number has all and only and just one of each of
# the nonzero digits cuz they adds to a 3 divizible number


def go():
    fours = four_digit_comboz()
    fives = five_eight_comboz_count(fours)
    return len(fours["123456789"]) + fives
