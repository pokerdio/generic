program = [s.strip() for s in open("day10_input.txt").readlines()]

# Initialize the register
x = 1

def sim(opcodes):
    ret = 0
    s = ""
    n = 0
    x = 1
    for opcode in opcodes:
        match opcode.split():
            case ["noop"]:
                s += "#" if abs(x - (n % 40)) < 2 else " "
                n += 1
                if n in (20, 60, 100, 140, 180, 220):
                    ret += n * x
            case ["addx", value]:
                for _ in range(2):
                    s += "#" if abs(x - (n % 40)) < 2 else " "
                    n += 1
                    if n in (20, 60, 100, 140, 180, 220):
                        ret += n * x
                x += int(value)  # Add the specified value to x
            case _:
                print(f"Unknown opcode: {opcode}")
    return ret, s

def crt_print(s, n = 40):
    for i in range((len(s) + n - 1) // n):
        print(s[i * n: (i + 1) * n])

score, crt_output = sim(program)
print("score", score)

crt_print(crt_output)
