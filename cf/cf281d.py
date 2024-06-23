import sys
input_str = sys.stdin.read().split()
input_str_idx = 0


def pop_int():
    global input_str_idx
    input_str_idx += 1
    return int(input_str[input_str_idx - 1])


n = pop_int()
v = [pop_int() for _ in range(n)]

max_stack = [v.pop(0)]

best = 0
for x in v:
    #    print(f"x={x} max_stack={max_stack}")
    while max_stack and max_stack[-1] < x:
        second_best = max_stack.pop()
        if second_best ^ x > best:
            best = second_best ^ x
    if max_stack and x ^ max_stack[-1] > best:
        best = x ^ max_stack[-1]
    max_stack.append(x)
#    print("after", max_stack)

print(best)
