from primez import init_primes, ba, iterate_primez


def bigprimez(n):
    n2 = int(sqrt(n)) + 1
    v = ba(n2)
    pv = list(iterate_primez(n2))

    n0 = n2
    pv2 = []

    percent = 0
    while n0 < n:
        if 100 * n0 // n > percent:
            percent = 100 * n0 // n
            print(percent, "%")
        v[:] = True
        for p in pv:
            p1 = (p - (n0 % p)) % p
            v[p1::p] = False
        for i in range(n2):
            if v[i]:
                pv2.append(i + n0)
        n0 += n2
    while pv2[-1] > n:
        pv2.pop()
    return pv + pv2


#vbil = bigprimez(10**8 + 10000)


def go(n, v=vbil):
    prime = [[0, 1, 0], [1, 1, 0]]      # two has 2->1 three has 3,2 and 3,2,1
    interval = [[0, 0, 0], [0, 1, 1]]  # two: nothing; 3's interval has 421 and 42

    total = [1, 3, 1]  # total for 2,3,4

    pi = 0
    for i in range(2, len(v)):
        p = v[i]

        if p > n:
            break

        iprime = (v[pi] == i + 1)

        if v[pi + 1] == i + 1:
            pi += 1
            iprime = True

        #print("cycle ", i, p, pi, iprime)

        if iprime:
            newprime = prime[pi].copy()
            newprime[0] += 1
            newinterval = [0] + prime[pi]
            newinterval[1] += 1

            #print("taking from prime ", pi, v[pi], newprime, newinterval)
        else:
            newprime = interval[pi].copy()
            newprime[1] += 1
            newinterval = [0] + interval[pi]
            newinterval[2] += 1
            #print("taking from interval ", pi, v[pi], newprime, newinterval)
        # save
        if p <= len(v) + 10:
            prime.append(newprime)
            interval.append(newinterval)
        # totalize

        while len(total) < max(len(newprime), len(newinterval)):
            total.append(0)
        for j in range(len(newprime)):
            total[j] += newprime[j]

        interval_start = v[i] + 1  # inclusive
        interval_end = v[i + 1]  # exclusive
        if interval_end > n:
            interval_end = n + 1
        interval_size = interval_end - interval_start
        #print("interval size:", interval_size)
        for j in range(len(newinterval)):
            total[j] = total[j] + newinterval[j] * interval_size

    ret = 1
    for x in total:
        if x > 0:
            ret = ret * x % 1000000007
    return ret  # , total


# 0: 32 53 532
# 1: 321 53 73 732 42
