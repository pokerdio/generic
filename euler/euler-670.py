
import matrix
import pprint


def go(n):
    pp = pprint.PrettyPrinter()
    mod = 10**9 + 4321
#         A  B  C  D  E  F  A, E, F, A, X, X, X
    m = [[3, 2, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0],  # A
         [6, 0, 2, 2, 0, 0, 6, 2, 2, 6, 12, 12, 12],  # B
         [6, 0, 0, 2, 2, 0, 6, 0, 2, 0, 12, 12, 0],  # C
         [6, 0, 2, 0, 0, 2, 6, 2, 0, 0, 12, 12, 0],  # D
         [6, 0, 0, 2, 0, 0, 0, 0, 0, 0, 12, 0, 0],  # E
         [6, 0, 2, 0, 0, 0, 0, 0, 0, 0, 12, 0, 0],  # F
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # A2
         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],  # E2
         [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],  # F2
         [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],  # A3
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # X
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],  # X2
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],  # X3
         ]
    v = [0] * 10 + [1, 0, 0]

    m = matrix.pow(m, n, mod)

    v = matrix.mul(m, v)

#    pp.pprint(v)

    return (v[0] + v[1]) % mod


print(go(10**16))


import primez
