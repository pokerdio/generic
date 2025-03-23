s = open("day6_input.txt").read()

def foo(s, n):
    for i in range(len(s) - n):
        if len(set(list(s[i:i+n]))) == n:
            return(i + n)

print(foo(s, 4))
print(foo(s, 14))
