
from math import factorial as f


def c(p, n):
    return f(n) // f(p) // f(n - p)


def foo():
    p = [0] * 27
    for peakpos in range(0, 25):
        #        print("peakpos", peakpos)
        for peakchar in range(peakpos + 1, 26):
            gapn = peakchar - peakpos
#            print("--->peakchar", peakchar, "gapn", gapn)
            assert(gapn >= 1)
            for topgap in range(gapn - 1, peakchar):  # id of the peak gap letter
                gapk = c(gapn - 1, topgap)  # combos of gap letters
                above_letters = 25 - peakchar

#                print("------>topgap", topgap, "gapk", gapk, "above_letters", above_letters)
                for rebound_saved in range(gapn):
                    climb_letters = above_letters + rebound_saved
#                    print("--------->rebound_saved", rebound_saved,
#                          "climb letters", climb_letters)

                    for climb_count in range(climb_letters + 1):
                        p[peakpos + 1 + climb_count] += c(climb_count, climb_letters) * gapk
    return p


print(max(foo()))
