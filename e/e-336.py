def go(c, n):
    if n == 2:
        yield chr(ord(c) + 1) + c
        return

    for s in go(chr(ord(c) + 1), n - 1):
        for i in range(1, len(s)):
            #            yield s[:i] + c + s[i:]
            yield s[i:][::-1] + c + s[:i]


print(sorted(list(go("A", 11)))[2010])
