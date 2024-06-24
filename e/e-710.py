import primez


def go(n):
    two = [0]
    non_two = [1]
    for i in range(1, n + 1):
        two.append(0)
        non_two.append(0)

        for j in range(1, i + 1):
            if j == 2:
                two[i] += two[i - 2] + non_two[i - 2]
            else:
                two[i] += two[i - j]
                non_two[i] += non_two[i - j]
            two[i] %= 1000000
            non_two[i] %= 1000000

#    print(two)
#    print(non_two)

    for i in range(1, 2 * n + 1):
        total = 0
        if i % 2 == 0:
            total += two[i // 2]

        for center in range(i % 2 and 1 or 2, i + 1, 2):
            remain = (i - center) // 2
            total += two[remain]
            if center == 2:
                total += non_two[remain]
            total %= 1000000

        print(i, total)  # , primez.decompose(total))


def go2(n):
    two = [0]
    non_two = [1]
    for i in range(1, n + 1):
        two.append(0)
        non_two.append(0)

        for j in range(1, i + 1):
            if j == 2:
                two[i] += two[i - 2] + non_two[i - 2]
            else:
                two[i] += two[i - j]
                non_two[i] += non_two[i - j]
            two[i] %= 1000000
            non_two[i] %= 1000000

        if i < 42:
            continue

        i = i * 2
        total = 0
        if i % 2 == 0:
            total += two[i // 2]

        for center in range(i % 2 and 1 or 2, i + 1, 2):
            remain = (i - center) // 2
            total += two[remain]
            if center == 2:
                total += non_two[remain]
            total %= 1000000
        if total % 1000 == 0:
            print(i, total)  # , primez.decompose(total))
            if total == 0:
                return

        i = i + 1
        total = 0
        if i % 2 == 0:
            total += two[i // 2]

        for center in range(i % 2 and 1 or 2, i + 1, 2):
            remain = (i - center) // 2
            total += two[remain]
            if center == 2:
                total += non_two[remain]
            total %= 1000000
        if total % 1000 == 0:
            print(i, total)  # , primez.decompose(total))
            if total == 0:
                return


def go3(n, mod=1000000):
    two = [0, 0]
    non_two = [1, 1]
    two_sum = [0, 0]
    non_two_sum = [1, 2]

    for i in range(2, n + 1):
        two.append((two_sum[-1] + non_two[-2]) % mod)
        non_two.append((non_two_sum[-1] - non_two[i - 2]) % mod)
        two_sum.append((two_sum[-1] + two[-1]) % mod)
        non_two_sum.append((non_two_sum[-1] + non_two[-1]) % mod)

        if i < 2:
            continue

        #i * 2
        total = (two_sum[i] + non_two[i - 1]) % mod
        if total % 1000 == 0:
            print(i * 2, total)  # , primez.decompose(total))
            if total == 0:
                return
        #i * 2 + 1
        total = two_sum[i]

        if total == 0:
            print(i * 2 + 1, total)  # , primez.decompose(total))
            return
