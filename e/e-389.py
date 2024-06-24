#from builtins import sum


def gen_outcomes(ndice, nside):
    v = [1]

    for _ in range(ndice):
        v2 = [0] * (len(v) + nside)
        for dice_roll in range(1, nside + 1):
            for i in range(len(v)):
                v2[i + dice_roll] += v[i]

        v = v2
    return v


def stack_outcomes(vndice, nside):
    ndice = len(vndice) - 1
    ret = [0] * (ndice * nside + 1)

    v = [1]
    for die in range(1, ndice + 1):
        print("%d / %d" % (die, ndice))
        v2 = [0] * (len(v) + nside)
        for dice_roll in range(1, nside + 1):
            for i in range(len(v)):
                v2[i + dice_roll] += v[i]
        v = v2
        for i in range(len(v)):
            ret[i] += vndice[die] * v[i]
    return ret


def stack_outcomes2(v_p, nside):
    n = len(v_p) - 1
    ret = [0] * (n * nside + 1)

    v = [1]
    for die in range(1, n + 1):
        print("%d / %d" % (die, n))
        v2 = [0] * (len(v) + nside)
        for dice_roll in range(1, nside + 1):
            for i in range(len(v)):
                v2[i + dice_roll] += v[i] / nside
        v = v2
        for i in range(len(v)):
            ret[i] += v_p[die] * v[i]
    return ret


def test_46():
    ret = [0] * 25
    for i in range(1, 5):
        v = gen_outcomes(i, 6)
        for j in range(len(v)):
            ret[j] += v[j]
    return ret


def var_avg(ndice, nface):
    avg = (nface + 1) / 2
    var = ndice * sum((x - avg) ** 2 for x in range(1, nface + 1)) / nface
    return ndice * avg, var


def combine_var_avg(n1, avg1, var1, n2, avg2, var2):
    combined_avg = (n1 * avg1 + n2 * avg2) / (n1 + n2)
    d1 = avg1 - combined_avg
    d2 = avg2 - combined_avg
    combined_var = (n1 * var1 + n2 * var2 + n1 * d1 ** 2 + n2 * d2 ** 2) / (n1 + n2)
    return n1 + n2, combined_avg, combined_var


def go():
    v6 = stack_outcomes(gen_outcomes(1, 4), 6)
    v8 = stack_outcomes(v6, 8)
    v12 = stack_outcomes(v8, 12)

    #v20 = stack_outcomes(v12, 20)
    n, avg, var = 0, 0, 0

    for i in sorted(range(1, len(v12)), key=lambda x: v12[x]):
        #    for i in range(len(v12)-1, 0, -1):
        n, avg, var = combine_var_avg(n, avg, var, v12[i], *var_avg(i, 20))
        print(i, len(str(v12[i])), var)
    return avg, var


def go2():
    v6 = stack_outcomes(gen_outcomes(1, 4), 6)
    v8 = stack_outcomes(v6, 8)
    v12 = stack_outcomes(v8, 12)

    v20 = stack_outcomes(v12, 20)
    s20 = sum(v20)
    for i in range(len(v20)):
        v20[i] /= s20

    avg = sum(i * v20[i] for i in range(1, len(v20)))
    var = sum((i - avg) ** 2 * v20[i] for i in range(1, len(v20)))
    print(avg, var, len(v20))

    return var


def go3():
    v6 = stack_outcomes2([0, 0.25, 0.25, 0.25, 0.25], 6)
    v8 = stack_outcomes2(v6, 8)
    v12 = stack_outcomes2(v8, 12)
    v20 = stack_outcomes2(v12, 20)

    # v7 = stack_outcomes2([0, 0.2, 0.2, 0.2, 0.2, 0.2], 7)
    # v20 = stack_outcomes2(v7, 9)
    s20 = sum(v20)

    for i in range(len(v20)):
        v20[i] /= s20

    print(len(str(s20)), type(s20), sum(v20))

    avg = sum(i * v20[i] for i in range(1, len(v20)))
    var = sum(((i - avg)**2) * v20[i] for i in range(1, len(v20)))
    print(avg, var, len(v20))

    return var


print(go3())
