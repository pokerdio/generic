def go(n=976):
    assert(len(set(pow(3, i, n + 1)for i in range(1, n + 1))) == n)

    v = [0] * n
    for i in range(0, n):
        val = pow(3, i + 1, n + 1)
        v[val - 1] = i

    dp = [[0]]
    for i in range(1, n):
        print(i)
        dp.append([0] * (i + 1))
        dp[i][i] = 0
        for j in range(i - 1, -1, -1):
            if i - j == 1:
                dp[i][j] = abs(v[i] - v[j])
            else:
                best = None
                for k in range(j, i):
                    val = dp[i][k + 1] + dp[k][j] + abs(v[k] - v[i])
#                    print("trying ", j, k, i, "val", val, "=%d+%d+%d" % (dp[k][j], abs(v[k] - v[k + 1]), dp[i][k + 1]))
                    if not best or val < best:
                        best = val
                dp[i][j] = best
    return dp[-1][0]
