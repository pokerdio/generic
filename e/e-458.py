
import matrix
import pprint


def go(n):
    pp = pprint.PrettyPrinter()

    m = [[1, 1, 1, 1, 1, 1],
         [6, 1, 1, 1, 1, 1],
         [0, 5, 1, 1, 1, 1],
         [0, 0, 4, 1, 1, 1],
         [0, 0, 0, 3, 1, 1],
         [0, 0, 0, 0, 2, 1]]

    m = matrix.pow(m, n - 1, 10**9)

    v = matrix.mul(m, [7, 0, 0, 0, 0, 0])

    pp.pprint(v)

    return sum(v) % 10**9
