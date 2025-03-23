import re, math
monkey_input = open("day11_input.txt").readlines()
monkey_desc = [[s.strip() for s in monkey_input[x:x+6]] for x in range(0, len(monkey_input), 7)]


def re_get_int(regex, s):
    return int(re.match(regex, s).groups()[0])

def attempt_to_int(s):
    s = s.strip()
    if re.match("^[0-9]+$", s):
        return int(s)
    return s

def retrieve_int_or_string_lst(s):
    return [attempt_to_int(word) for word in re.split("[, ]+", s)]

class Monkey:
    mod = 1
    def __init__(self, description_lst):
        self.monkey_id = re_get_int("Monkey ([0-9]+):", description_lst[0])
        self.items = retrieve_int_or_string_lst(description_lst[1][16:])
        self.monkey_op1, self.monkey_op, self.monkey_op2  = retrieve_int_or_string_lst(description_lst[2][17:])
        self.test_div = re_get_int("Test: divisible by ([0-9]+)", description_lst[3])
        self.if_true = re_get_int("If true: throw to monkey ([0-9]+)", description_lst[4])
        self.if_false = re_get_int("If false: throw to monkey ([0-9]+)", description_lst[5])
        self.activity_count = 0

        Monkey.mod = Monkey.mod * self.test_div // math.gcd(Monkey.mod, self.test_div)

    def __repr__(self):
        return f'''Monkey {self.monkey_id}
  Starting items: {", ".join(str(item) for item in self.items)}
  Operation: new = {" ".join(str(op) for op in (self.monkey_op1, self.monkey_op, self.monkey_op2))}
  Test: divisible by {self.test_div}
    If true: throw to monkey {self.if_true}
    If false: throw to monkey {self.if_false}
  Activity: {self.activity_count}
'''

    def step(self, monkey_lst):
        for item_worry in self.items:
            self.activity_count += 1
            op1 = item_worry if self.monkey_op1 == "old" else self.monkey_op1
            op2 = item_worry if self.monkey_op2 == "old" else self.monkey_op2
            if self.monkey_op == "+":
                new_worry = op1 + op2
            elif self.monkey_op == "*":
                new_worry = op1 * op2

            new_worry = new_worry % Monkey.mod

            if (new_worry % self.test_div == 0):
                monkey_lst[self.if_true].items.append(new_worry)
            else: 
                monkey_lst[self.if_false].items.append(new_worry)
        self.items = []

monkey = [Monkey(desc) for desc in monkey_desc]


def step_monkeys(monkey_lst, count):
    for _ in range(count): 
        for monkey in monkey_lst:
            monkey.step(monkey_lst)

    m1, m2 = sorted(monkey_lst, key=lambda x: x.activity_count)[-2:]
    return m1.activity_count * m2.activity_count



print(step_monkeys(monkey, 10000))
