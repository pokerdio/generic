lines = [s.strip() for s in open("day3_input.txt").readlines()]

# lines = ["vJrwpWtwJgWrhcsFMMfFFhFp",
#          "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
#          "PmmdzqPrVvPwwTWBwg",
#          "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
#          "ttgJtRGJQctTZtZT",
#          "CrZsJsPPZsGzwwsLwLmpwMDw"]

common = [set(l[:len(l) // 2]).intersection(set(l[len(l)//2:])).pop() for l in lines]

def score(c):
    if (c >= "a" and c <= "z"):
        return ord(c) - ord("a") + 1
    if (c >= "A" and c <= "Z"):
        return ord(c) - ord("A") + 27



print(sum(score(c) for c in common))

line_sets = [set(l) for l in lines]
badges = [line_sets[i + 0].intersection(line_sets[i + 1]).intersection(line_sets[i + 2]).pop() \
          for i in range(0, len(line_sets), 3)]

print(sum(score(b) for b in badges))
