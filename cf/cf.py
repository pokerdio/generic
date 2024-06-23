input_str = sys.stdin.read().split()
input_str_idx = 0


def pop_int():
    global input_str_idx
    input_str_idx += 1
    return int(input_str[input_str_idx - 1])


def pop_str():
    global input_str_idx
    input_str_idx += 1
    return input_str[input_str_idx - 1]
