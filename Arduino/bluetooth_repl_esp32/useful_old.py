import os, re, time, gc


def printf(fname, min=0, max=None, p=p, filter=None):
    for i, s in enumerate(open(fname).readlines()):
        if i >= min and (not max or i < max) and (not filter or filter(s)):
            p(i, s.rstrip())


def insertf(fname, txt, line=None):
    orig = open(fname, "r").readlines()
    if None is line:
        line = len(orig)

    if type(txt) == str:
        txt = [txt]
    orig = orig[:line] + txt + orig[line:]

    writef(fname, orig)


def writef(fname, txt):
    f = open(fname, "w")
    if type(txt) == str:
        txt = [txt]
    for s in txt:
        f.write(untabify(s))
    f.close()


def appendf(fname, txt, empty=2):
    f = open(fname, "a")
    if type(txt) == str:
        txt = [txt]
    txt = [""] * empty + txt
    for s in txt:
        f.write(untabify(s))
    f.close()


def replacef(fname, min, max, txt=None):
    if not txt:
        txt = ble.last_com
    delf(fname, min, max)
    insertf(fname, txt, min)


def run_use():
    exec(open("useful.py", "r").read())


def delf(fname, min, max):
    orig = open(fname, "r").readlines()
    writef(fname, orig[:min] + orig[max:])


def tabdepth(s):
    s = s.replace("\t", "    ")
    for i in range(len(s)):
        if s[i] != ' ':
            return (i + 3) // 4


def isdef(s):
    return re.match("^def.*:$", s.strip())


def onlydefs(fname, p=p):
    printf(fname, filter=isdef, p=p)


def finddef(fun_name, file_name=""):
    if not file_name:
        for fname in os.listdir():
            yield from finddef(fun_name, fname)
        return

    lines = open(file_name).readlines()
    for i, s in enumerate(lines):
        s = s.strip()
        if re.match("^def\\s+%s.*:$" % fun_name, s):
            yield file_name, i


def printsrc(fun_name, nlines=10, file_name="", p=p):
    file_name, line = next(finddef(fun_name, file_name)) or (None, None)
    if file_name:
        printf(file_name, line, line + nlines, p=p)


def dotify(x, maxlen=65):
    if type(x) == str:
        s = '"' + x + '"'
    else:
        s = str(x)
    if len(s) > maxlen + 2:
        s = s[:maxlen] + "..."
    return s


def untabify(s):
    s = s.rstrip()
    for i in range(len(s)):
        if s[i] != ">":
            return "    " * i + s[i:] + "\n"
    return ""


def dotify(x, maxlen=65):
    if type(x) == str:
        s = '"' + x + '"'
    else:
        s = str(x)
    if len(s) > maxlen + 2:
        s = s[:maxlen] + "..."
    return s


def mydir(x, p=p):
    for s in dir(x):
        p(s, dotify(getattr(x, s)).rstrip())
