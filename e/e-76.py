#!/usr/bin/env python3



v = {(1, 1): 1}
n = 10

for value in range(2, n):
    for max_sub in range(1, value + 1):
        # get the number of ways to break up value in a sum of items no bigger than max_sub

        #        print("counting for ", value, max_sub)
        count = 1  # the 1+1+...+1 break
        for k in range(2, max_sub):
            v2, max2 = value - k, min(k, value - k)

#            print("  adding sub sum of", v2, max2)
            count += v[v2, max2]

        if max_sub == value:
            count += 1  # the unbroken one item "sum" #note the problem doesn't want these
        else:
            v2, max2 = value - max_sub, min(value - max_sub, max_sub)
#            print("  adding sub sum of", v2, max2)
            count += v[v2, max2]

        v[(value, max_sub)] = count
