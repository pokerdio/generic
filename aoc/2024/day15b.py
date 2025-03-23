def convert(c):
    match c:
        case '#':
            return '##'
        case '.':
            return '..'
        case '@':
            return '@.'
        case 'O':
            return '[]'

def get_input(fname = "day15_example.txt"):
    s = open(fname).read()
    map, motion = s.split("\n\n")
    xy = map.replace("\n", "").index("@")
    width = map.index("\n")
    x, y = (xy % width) * 2, xy // width

    map = [list("".join(convert(c) for c in s)) for s in map.split("\n")]
    return map, motion.strip(), x, y

warehouse, motion, robotx, roboty = get_input("day15_input.txt")
width = len(warehouse[0])
height = len(warehouse)

def onMap(x, y):
    global width, height
    return x >= 0 and y >= 0 and x < width and y < height

def doMotionH(dx):
    global warehouse, motion, robotx, roboty, width, height
    
    x, y = robotx, roboty
    box_count = 0
    while True:
        x += dx
        if not onMap(x, y) or warehouse[y][x] == "#":
            return # motion failed
        if warehouse[y][x] == ".": # motion success
            warehouse[roboty][robotx] = '.'
            warehouse[roboty][robotx + dx] = '@'
            s = "[]" if dx > 0 else "]["
            robotx = robotx + dx

            for box in range(box_count):
                warehouse[roboty][robotx + dx * box * 2 + dx] = s[0]
                warehouse[roboty][robotx + dx * box * 2 + 2 * dx] = s[1]
            return
        if warehouse[y][x] == "[":
            box_count += 1

def doMotionV(dy):
    global warehouse, motion, robotx, roboty, width, height
    x, y = robotx, roboty

    boxes = []
    if onMap(x, y + dy):
        match warehouse[y + dy][x]:
            case "[":
                boxes.append((x, y + dy))
            case "]":
                boxes.append((x - 1, y + dy))
            case ".":
                warehouse[y][x] = '.'
                warehouse[y + dy][x] = '@'
                roboty += dy
                return # robot successfully walks into empty space, no pushing required
            case "#":
                return # face->wall. motion fails
    else:
        return # never happens

    # builds a list of boxes that are being pushed by the robot, in order of robot proximity
    # (breadth first); quits function if stuckage is found
    
    box_set = set(boxes)

    for i in range(width * height):
        if (i >= len(boxes)):
            break
        boxx, boxy = boxes[i]
        if not onMap(boxx, boxy + dy):
            return # box is being pushed off the map, motion is a failure (never happens cuz outer walls)
        for j in range(2):
            match warehouse[boxy + dy][boxx + j]:
                case '#':
                    return # blockage, motion is a failure
                case '[':
                    new_box = (boxx + j, boxy + dy)
                    if not new_box in box_set:
                        box_set.add(new_box)
                        boxes.append(new_box)
                case ']':
                    new_box = (boxx + j - 1, boxy + dy)
                    if not new_box in box_set:
                        box_set.add(new_box)
                        boxes.append(new_box)

    #moving the boxes, back to front order
    for i in range(len(boxes) - 1, -1, -1):
        boxx, boxy = boxes[i]
        warehouse[boxy + dy][boxx] = '['
        warehouse[boxy + dy][boxx + 1] = ']'
        warehouse[boxy][boxx] = '.'
        warehouse[boxy][boxx + 1] = '.'
    warehouse[roboty][robotx] = '.'
    roboty += dy
    warehouse[roboty][robotx] = '@'    

    
for c in motion:
    # print(f"motion {c}\n")
    match c:
        case "<":
            doMotionH(-1)
        case ">":
            doMotionH(1)
        case "^":
            doMotionV(-1)
        case "v": 
           doMotionV(1)
    # print("\n".join("".join(line) for line in warehouse), "\n")

answer = 0

for y in range(height):
    for x in range(width):
        if warehouse[y][x] == '[':
            answer += y * 100 + x

print(answer)
