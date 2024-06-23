

def digiroot(n):
    if n < 10:
        return n
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return digiroot(s)


dr = [0] + list(range(1, 10)) * 111111
dr2 = [0] + [i % 9 + 1 for i in range(999999)]
assert(dr == dr2)
max_dr_sum = dr.copy()


def go(prod, dr_sum, max_factor):
    for i in range(2, max_factor + 1):
        newprod = i * prod
        if newprod < 1000000:
            new_dr_sum = dr_sum + dr[i]
            max_dr_sum[newprod] = max(new_dr_sum, max_dr_sum[newprod])
            go(newprod, new_dr_sum, i)
        else:
            break


go(1, 0, 500000)


print(sum(max_dr_sum[2:]))
