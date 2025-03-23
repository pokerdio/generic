def get_input(fname = "day15_example.txt"):
    s = open(fname).read()
    map, motion = s.split("\n\n")
    xy = map.replace("\n", "").index("@")
    map = [list(s) for s in map.split("\n")]
    width = len(map[0])
    x, y = xy % width, xy // width
    return map, motion.strip(), x, y

warehouse, motion, robotx, roboty = get_input("day15_input.txt")
width = len(warehouse[0])
height = len(warehouse)

def onMap(x, y):
    global width, height
    return x >= 0 and y >= 0 and x < width and y < height

def doMotion(dx, dy):
    global warehouse, motion, robotx, roboty, width, height
    
    x, y = robotx, roboty
    while True:
        x += dx
        y += dy
        if not onMap(x, y) or warehouse[y][x] == "#":
            return # motion failed
        if warehouse[y][x] == ".": # motion success
            warehouse[roboty][robotx] = '.'
            warehouse[y][x] = 'O' # this generates ghost food if robot is walking into empty space
            warehouse[roboty + dy][robotx + dx] = '@' # in which case this overwrites the ghost food
            robotx = robotx + dx
            roboty = roboty + dy
            return 
    
for c in motion:
    #print(f"motion {c}\n")
    match c:
        case "<":
            doMotion(-1, 0)
        case ">":
            doMotion(1, 0)
        case "^":
            doMotion(0, -1)
        case "v":
            doMotion(0, 1)
    #print("\n".join("".join(line) for line in warehouse), "\n")

answer = 0

for y in range(height):
    for x in range(width):
        if warehouse[y][x] == 'O':
            answer += y * 100 + x

print(answer)
