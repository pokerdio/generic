

def F(n, m):
    """if m lower than halfish split in m-1 equalish groups, and 
    test the complete subgraph for all groups - box principle says one has 2+ good
    fuses - murphy law says last tested group has 2 and last conenction tested has 
    the good ones -- apparently this is called turan's theorem"""
    if m > (n + 1) // 2:
        return n - m + 1

    if m == 2:
        return n * (n - 1) // 2

    smol = n // (m - 1)
    big = smol + 1
    nbig = n - smol * (m - 1)
    nsmol = (n - (nbig * big)) // smol

#    print(smol, nsmol, big, nbig)
    return (smol * (smol - 1) * nsmol + big * (big - 1) * nbig) // 2


def L(n):
    return sum(F(n, m) for m in range(2, n + 1))
