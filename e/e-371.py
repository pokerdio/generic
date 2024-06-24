# from fractions import Fraction as F

# # notyet = F(1)
# # expectedn = F(0)

# # for i in range(2, 1000):
# #     expectedn += (notyet * (i * i - i)) / 999
# #     notyet *= (1000 - i) / 999

# # en = float((expectedn * 1000) / 999)
# # print("%.9f" % en)
# # print("%.8f" % en)
# print()
# notyet = F(1)

# nxp = 500
# xp = [F(1)] + [F(0)] * (nxp - 1)  # probability of getting to a step with [x] zeros and doubles
# xp500 = [F(0)] * nxp  # probability of getting to a step with [x] zeros and doubles and with a 500

# winxp = F(0)


# F001 = F(1, 1000)
# F999 = F(999, 1000)

# sumbingo = F(0)
# for i in range(0, 500):
#     xp2 = [F(0)] * nxp
#     xp5002 = [F(0)] * nxp
#     bingo = F(0)  # game end on step i
#     for zero in range(nxp):
#         if i >= zero:
#             bingo += (i - zero) * F001 * (xp[zero] + xp500[zero])
#             xp2[zero] += xp[zero] * (999 - i + zero) * F001
#         if zero < nxp - 1:
#             xp2[zero + 1] += xp[zero] * F001
#     s = " - "

#     winxp += bingo * (i + 1)
#     xp = xp2

#     for j in range(10):
#         s += "%.9f " % float(xp[j])
#     sumbingo += bingo
#     print("on turn %d bingo is %.9f sumxp %.9f" % (i, float(bingo), float(sum(xp)) + sumbingo) + s)


# print("final solution %.8f" % float(winxp))
# print("moar digits %.10f" % float(winxp))

def vadd(v,  key, value):
    v[key] = v.get(key, 0) + value


def go(n=470):
    v = {(0, True): 1 / 999, (1, False): 998 / 999}
    s = 0
    for i in range(2, n + 1):
        v2 = {}

        for (k, five), p in v.items():
            #            print("k5p", k, five, p)
            if five:
                s += p * i * (k + 1) / 999  # k options for WiN plus one for 500
                vadd(v2, (k, True), p * k / 999)  # k options for repeats
                vadd(v2, (k + 1, True), p * (998 - k * 2) / 999)  # rest
            else:
                s += p * i * k / 999  # k options for WIn
                vadd(v2, (k, False), p * k / 999)  # k options for repeats
                vadd(v2, (k, True), p * 1 / 999)  # 1 option for 500
                vadd(v2, (k + 1, False), p * (998 - k * 2) / 999)  # remaining options new num
        v = v2
#        print(v)
    return s * 1.001001001001001001001  # this accounts for the 000 plates which never win
# for every car that's not a 000, there's 1/1000 chance for the win to be delayed by one
# or more 000 cars, 1/1000000 for the win to be delayed by two or more, 1/(10**9) 3+ etc.
