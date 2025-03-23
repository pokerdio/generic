map = [s.strip() for s in open("day16_input.txt").readlines()]

for y in range(len(map)):
    s = map[y]
    if "S" in s:
        startx = s.index("S")
        starty = y
        map[y] = s.replace("S", ".")
    if "E" in s:
        endx = s.index("E")
        endy = y
        map[y] = s.replace("E", ".")


best = {(startx, starty, '>'): 0}
open_lst = [(startx, starty, '>')]


def try_new_pos(new_pos, new_cost): 
    global best, open_lst
    if not new_pos in best or new_cost < best[new_pos]:
        open_lst.append(new_pos)
        best[new_pos] = new_cost



while open_lst: 
    pos = open_lst.pop()
    x, y, dir = pos
    cost = best[pos]
    match dir:
        case '>':
            try_new_pos((x, y, "^"), cost + 1000)
            try_new_pos((x, y, "v"), cost + 1000)
            if map[y][x + 1] == ".":
                try_new_pos((x+1, y, ">"), cost + 1)
        case '<':
            try_new_pos((x, y, "^"), cost + 1000)
            try_new_pos((x, y, "v"), cost + 1000)
            if map[y][x - 1] == ".": #won't break cuz borders
                try_new_pos((x-1, y, "<"), cost + 1)
        case '^':
            try_new_pos((x, y, ">"), cost + 1000)
            try_new_pos((x, y, "<"), cost + 1000)
            if map[y-1][x] == ".": #won't break cuz borders
                try_new_pos((x, y-1, "^"), cost + 1)
        case 'v':
            try_new_pos((x, y, ">"), cost + 1000)
            try_new_pos((x, y, "<"), cost + 1000)
            if map[y+1][x] == ".": #won't break cuz borders
                try_new_pos((x, y+1, "v"), cost + 1)


end_pos = tuple((endx, endy, c) for c in "><^v")

best_score = min(best.get(pos, 10**10) for pos in end_pos)

print(best_score)

best_set = set(((startx, starty), (endx, endy)))

walkback_lst = [pos for pos in end_pos if best_score == best[pos]]
walkback_set = set(walkback_lst)



def walkback_try(new_pos, turn_str): 
    global walkback_set, walkback_lst, best, best_set, map
    
    if map[new_pos[1]][new_pos[0]] == "." and best[new_pos] == best[pos] - 1:
        best_set.add(new_pos[:2])
        if new_pos not in walkback_set: 
            walkback_lst.append(new_pos)
            walkback_set.add(new_pos)
    for dir in turn_str:
        new_pos = (x, y, dir)
        if best[new_pos] + 1000 == best[pos]:
            best_set.add(new_pos[:2])
            if new_pos not in walkback_set:
                walkback_set.add(new_pos)
                walkback_lst.append(new_pos)


while walkback_lst:
    pos = walkback_lst.pop()
    x, y, dir = pos
    match dir:
        case '>':
            walkback_try((x-1, y, ">"), "^v")
        case '<':
            walkback_try((x+1, y, "<"), "^v")
        case '^':
            walkback_try((x, y+1, "^"), "<>")
        case 'v':
            walkback_try((x, y-1, "v"), "<>")

print(len(best_set))
