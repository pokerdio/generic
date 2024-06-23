n = int(input())

v = []

for _ in range(n):
    com = input()
    if com == "pwd":
        if v:
            print("/" + "/".join(v) + "/")
        else:
            print("/")
    else:
        path = com[3:]
        if path[0] == "/":
            path = path[1:]
            v = []
        dirs = path.split("/")
        for dir in dirs:
            if dir == "..":
                v.pop()
            elif dir:
                v.append(dir)
