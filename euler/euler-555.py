def makerecdec():
    data = [0]
    verbose = [1]
    global logpush, logpop

    def logpush(n):
        verbose.append(n)

    def logpop():
        verbose.pop()
        if not verbose:
            verbose.append(0)

    def recdec(f):
        def f2(*args):
            str_args = str(args).strip("(),")
            if verbose[-1]:
                print(" > " * data[0], f"f({str_args})")
            data[0] += 1
            ret = f(*args)
            data[0] -= 1
            if verbose[-1]:
                print(" < " * data[0], f"f({str_args})={ret}")
            return ret
        return f2
    return recdec


@makerecdec()
def fact(n):
    if n < 2:
        return 1
    return n * fact(n - 1)


@makerecdec()
def fibo(n):
    if n < 2:
        return n
    return fibo(n - 1) + fibo(n - 2)


@makerecdec()
def f(m, k, s, n):
    if n > m:
        return n - s
    else:
        return f(m, k, s, f(m, k, s, n + k))


# f(m) = f(f(m+k)) = f(m+k-s) = m+k-2s
# f(m-1) = f(f(m+k-1)) = f(m+k-s-1) = m+k-2s-1


def f91(n):
    return f(100, 11, 10, n)


def foo(m):
    logpush(0)
    for s in range(1, m):
        for k in range(s + 1, m):
            fixed = set()
            for n in range(1, m + 1):
                if f(m, k, s, n) == n:
                    fixed.add(n)
            print(m, k, s, fixed)

    logpop()
