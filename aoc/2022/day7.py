disk = {}

input_name = "day7_input.txt"
coms = [s.strip() for s in open(input_name).readlines()]


class Directory():
    def __init__(self, father = None):
        self.files = {}
        self.dirs = {}
        self.father = father

    def addFile(self, name, size):
        self.files[name] = size
    def addDir(self, name):
        self.dirs[name] = Directory(self)

    def size(self):
        ret = 0
        for _, sz in self.files.items():
            ret += sz
        for _, subdir in self.dirs.items():
            ret += subdir.size()
        return ret

    def problim(self):   
        ret = 0
        size = 0
        for _, sz in self.files.items():
            size += sz
        for _, subdir in self.dirs.items():
            subret, subsize = subdir.problim()
            ret += subret
            size += subsize
        if size <= 100000:
            ret += size
        return ret, size

    def smallestDirAbove(self, minSize):
        ret = 0
        size = 0
        for _, sz in self.files.items():
            size += sz
        for _, subdir in self.dirs.items():
            subret, subsize = subdir.smallestDirAbove(minSize)
            if ret == 0:
                ret = subret
            elif subret != 0:
                ret = min(ret, subret)
            size += subsize
        if size >= minSize:
            if ret == 0: 
                ret = size
            else:
                ret = min(ret, size)
        return ret, size
        

root = Directory()

current = root

for com in coms:
    if com == "$ cd /" or com == "$ cd/":
        current = root
    elif com == "$ cd .." or com == "$ cd..":
        current = current.father
        if not current:
            current = root
    elif com == "$ ls":
        continue
    elif com[:3] == "dir":
        current.addDir(com[4:])
    elif com[0] in "0123456789":
        sz, fname = com.split(" ")
        current.addFile(fname, int(sz))
    elif com[:4] == "$ cd":
        dirname = com[5:]
        current.addDir(dirname)
        current = current.dirs[dirname]

print(root.problim()[0])

diskSize = 70000000
needUnused = 30000000
freeSize = diskSize - root.size()
needFreed = needUnused - freeSize
print(root.smallestDirAbove(needFreed)[0])
