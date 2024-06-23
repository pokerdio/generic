from primez import iterate_primez


def foo(n):
    d = set()
    for p1 in iterate_primez(int(n ** 0.25 + 1)):
        # print(p1)
        p1_quad = p1 ** 4
        n1 = n - p1_quad
        if n1 <= 0:
            break
        for p2 in iterate_primez(int(n1 ** 0.3333334 + 1)):
            #print("    ", p2)
            p2_cube = p2 ** 3
            n2 = n1 - p2_cube
            if n2 <= 0:
                break
            for p3 in iterate_primez(int(n2 ** 0.5 + 1)):
                #print("        ", p3)
                x = p3 ** 2 + p1_quad + p2_cube
                if x < n:
                    d.add(x)
                    #print("            =>", x)
    return len(d)
