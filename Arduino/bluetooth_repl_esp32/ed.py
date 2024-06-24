import os
import re

STATE_EDIT = 1
STATE_EVAL = 2
STATE_DEFUN = 3

p = print
pstr = print
state = STATE_EVAL
txt = []
edit_target = None
edit_min = None
edit_max = None
edit_undo_target = None
edit_undo_txt = None
edit_line = -1
edit_kill_ring = []


def save_undo(fname):
    global edit_undo_target, edit_undo_txt
    try:
        f = open(fname, "r")
    except:
        return
    edit_undo_target = fname
    edit_undo_txt = [s.rstrip() for s in f.readlines()]


def undo():
    if edit_undo_target:
        writef(edit_undo_target, edit_undo_txt)
        p("restored", edit_undo_target)


def printf(fname, min=0, max=None, filter=None):
    for i, s in enumerate(open(fname, "r").readlines()):
        if i >= min and (not max or i < max) and (not filter or filter(s)):
            p(str(i) + " " + s.rstrip())


def insertf(fname, txt, line=None):
    orig = open(fname, "r").readlines()
    if None is line:
        line = len(orig)
    if type(txt) == str:
        txt = [txt]
    orig = orig[:line] + txt + orig[line:]
    writef(fname, orig)


def writef(fname, text):
    save_undo(fname)
    f = open(fname, "w")
    if type(text) == str:
        text = [text]
    for s in text:
        f.write(s.rstrip() + "\n")
    f.close()


def appendf(fname, txt, empty=0):
    save_undo(fname)
    f = open(fname, "a")
    if type(txt) == str:
        txt = [txt]
    txt = [""] * empty + txt
    for s in txt:
        f.write(s.rstrip() + "\n")
    f.close()


def replacef(fname, min, max, txt):
    delf(fname, min, max)
    insertf(fname, txt, min)


def run_use():
    exec(open("useful.py", "r").read())


def delf(fname, min, max):
    orig = open(fname, "r").readlines()
    writef(fname, orig[:min] + orig[max:])


def empty_line(s):
    s = s.strip()
    return not s or s[0] == "#"


def tabdepth(s):
    if empty_line(s):
        return None
    s = s.replace("\t", "    ")
    for i in range(len(s)):
        if s[i] != ' ':
            return (i + 3) // 4


def paragraph_len(fname, start_line):
    v = open(fname, "r").readlines()[start_line:]
    d0 = tabdepth(v[0])
    last = start_line
    for s in v[1:]:
        d2 = tabdepth(s)
        if None is d2:
            continue
        last += 1
        if d2 <= d0:
            return last - start_line + 1
    return last - start_line + 1


def isdef(s):
    return re.match("^def.*:$", s.strip())


def finddef(fun_name, file_name=""):
    if not file_name:
        for fname in os.listdir():
            yield from finddef(fun_name, fname)
        return
    try:
        lines = open(file_name, "r").readlines()
    except:
        return
    for i, s in enumerate(lines):
        s = s.strip()
        if re.match("^def\\s+%s.*:$" % fun_name, s):
            yield file_name, i, s


def printdef(fun_name):
    for f, i, s in finddef(fun_name):
        p(f, i)
        p(s)


def printsrc(fun_name, file_name=""):
    v = list(finddef(fun_name, file_name)) or ()
    for file_name, line, _ in v:
        p(file_name)
        printf(file_name, line, line + paragraph_len(file_name, line))


def dotify(x, maxlen=65):
    if type(x) == str:
        s = '"' + x + '"'
    else:
        s = str(x)
    if len(s) > maxlen + 2:
        s = s[:maxlen] + "..."
    return s


def search_filter(txt):
    def ret(s):
        return txt in s
    return ret


def search(txt, fname=None):
    filter = search_filter(txt)
    if fname:
        printf(fname, filter=filter)
    else:
        for fname in os.listdir():
            p(fname)
            printf(fname, filter=filter)


def onlydefs(fname=None):
    if fname:
        printf(fname, filter=isdef)
    else:
        for fname in os.listdir():
            p(fname)
            printf(fname, filter=isdef)


def untabify(s):
    s = s.rstrip()
    for i in range(len(s)):
        if s[i] != ">":
            return "    " * i + s[i:]
    return ""


def dotify(x, maxlen=65):
    if type(x) == str:
        s = '"' + x + '"'
    else:
        s = str(x)
    if len(s) > maxlen + 2:
        s = s[:maxlen] + "..."
    return s


def mydir(x):
    for s in dir(x):
        p(s, dotify(getattr(x, s)).rstrip())


def is_assign(e):
    for op in [
            "&=", "+=", "-=", "<<=", ">>=", "**=", "^=", "|=", "%=", "/=",
            "*=", "//="
    ]:
        if op in e:
            return True

    if (re.search("[^><!=]=[^=]", e)):
        return True
    return False


def is_import(e):
    e = e.lstrip()
    return e.startswith("import") or e.startswith("from")


def exec_txt(txt, glo):
    if type(txt) == list:
        txt = "\n".join(txt) + "\n"
    try:
        exec(txt, glo or globals())
        p("exec went okay")
        return True  # success
    except Exception as e:
        p(">>>ERROR<<<", e)
        return False  # fail


def eval_txt(txt, glo):
    try:
        ret = eval(txt, glo or globals())
        if ret is not None:
            pstr(ret)
    except Exception as e:
        p('>>>ERROR<<<', e)


def neg_idx(x, n, default):  # negative to positive index transformation
    if x == "":
        x = default
    else:
        x = int(x)
    if x < 0:
        x = n + x
    if x < 0:
        x = 0
    return x


def valid_txt_range(s):
    if not s:
        return True
    try:
        ret = int(s)
    except:
        v = s.split(":")
        if (len(v) != 2):
            return False
        return valid_txt_range(v[0]) and valid_txt_range(v[1])
    return True


def get_txt_range(s):
    n = len(txt)
    if ":" in s:
        a, b = (x for x in s.split(":"))
        a = neg_idx(a, n, 0)
        b = neg_idx(b, n, n)
    else:
        a = neg_idx(s, n, -1)
        b = a + 1
    if a >= b:
        b = a + 1
    return a, b


def split_txt_range(s):
    for i in range(len(s)):
        if s[i] not in "0123456789-+:":
            if i > 0 and s[i - 1] in "-+":
                return s[:i - 1], s[i - 1:]
            return s[:i], s[i:]
    return s, ""


def startswith_count(big_str, small_str):
    n = len(small_str)
    for i in range(0, len(big_str), n):
        if big_str[i:i + n] != small_str:
            return i // n
    return len(big_str) // n


def print_kill(n):
    assert (n >= 0 and n <= 2)
    p("kill text ", n, ":")
    for i, s in enumerate(edit_kill_ring[n]):
        p(i, s)


def magic_command(s, glo=None):
    global txt, edit_target, edit_max, edit_min, state, edit_line, edit_kill_ring
    glo = glo or globals()
    if s == "$":  # edit end
        if state == STATE_EVAL:
            p("editing")
            state = STATE_EDIT
        elif state == STATE_DEFUN or state == STATE_EDIT:
            state_eval()
        return
    if s == "x":
        exec_txt(txt, glo)
    elif s[0] == "s":  # subst range / sep character other than +-09: / sought word/ sep character / replacement word
        range_s, subst_s = split_txt_range(s[1:])
        a, b = get_txt_range(range_s)
        subst_a, subst_b = subst_s[1:].split(subst_s[0])
        for j in range(a, b):
            txt[j] = txt[j].replace(subst_a, subst_b)
    elif s[0] == "$":  # execute an assignment/eval a statement
        s = s[1:]
        if is_assign(s) or is_import(s):
            exec_txt(s, glo)
        else:
            eval_txt(s, glo)
    elif s[0] == ">":
        i = startswith_count(s, ">")
        if not valid_txt_range(s[i:]):
            p("bad format")
            return
        a, b = get_txt_range(s[i:])
        for j in range(a, b):
            txt[j] = "    " * i + txt[j]
    elif s[0] == "<":
        i = startswith_count(s, "<")
        if not valid_txt_range(s[i:]):
            p("bad format")
            return
        a, b = get_txt_range(s[i:])
        for j in range(a, b):
            k = min(startswith_count(txt[j], " "), i * 4)
            txt[j] = txt[j][k:]
    elif s[0] in "cq":  # cancel, quit
        txt = []
        state_eval()
    elif s[0] == "y":  # yank
        line = edit_line
        n = 0
        if len(s) > 1:
            try:
                v = s[1:].split(">")
                assert (len(v) <= 2)
                n = int(v[0] or "0")
                assert (n >= 0 and n < len(edit_kill_ring))
                if len(v) == 2:
                    line = int(v[1])
                    assert (line >= -1 and line < len(txt))
            except:
                p("yank format: $y $y0 $y1 $y2 $y1>6")
                return
        if line == -1:
            txt = txt + edit_kill_ring[n]
        else:
            txt = txt[:line] + edit_kill_ring[n] + txt[line:]
    elif s[0] == "k":  # kill
        if not valid_txt_range(s[1:]):
            p("bad format")
            return
        a, b = get_txt_range(s[1:])
        if edit_line >= a and edit_line < b:
            edit_line = a
        edit_kill_ring = [txt[a:b]] + edit_kill_ring[0:2]
        txt = txt[:a] + txt[b:]
    elif s == "p":  # print
        for i, s in enumerate(txt):
            p(i, s)
    elif s == "pk":
        for i in range(len(edit_kill_ring)):
            print_kill(i)
    elif s.startswith("pk"):
        try:
            i = int(s[2:])
            print_kill(i)
        except:
            p("print kill format: $pk $pk0 $pk1 $pk2")
    elif s[0] == "w":  # write
        s = s[1:]
        if not s:
            if edit_target:
                replacef(edit_target, edit_min, edit_max, txt)
                edit_max = edit_min + len(txt)
            else:
                p("no writing destination")
        else:
            write(s)
    elif s[0] == "a":  # append
        append(s[1:])
    elif s[0] == "n":  # new
        txt = []
        state_edit()
        edit_line = -1
    elif s == "e":
        edit_line = -1
        state_edit()
    elif s[0] == "e":  # edit
        try:
            edit_line = int(s[1:])
            if edit_line < 0:
                edit_line = max(0, len(txt) + edit_line)
        except:
            p("correct edit commands: $e $e2 $e-3")
            return
        state_edit()
    elif s == "?":  # help
        p("$? $$5+5 $$$anytxt $$ $w $n \n$e $wf.py $af.py $k $k1 $k3:-2")
    else:
        p("unknown magic command")


def command(s, glo=None):
    global state, txt, edit_line
    print(">" + s + "<")
    if s.startswith("$$$"):  # for lines starting with magic combinations
        s = s[3:]
    elif s.startswith("$"):
        magic_command(s[1:], glo)
        return
    else:
        s = untabify(s)
    if (state == STATE_EVAL):
        if s[-1] == ":":
            txt = [s]
            state = STATE_DEFUN
            edit_line = -1
        elif is_assign(s) or is_import(s):
            exec_txt(s, glo)
        else:
            eval_txt(s, glo)
    elif state == STATE_DEFUN:
        if (edit_line == -1 or edit_line == len(txt)) and s == "":
            exec_txt(txt, glo)
            state_eval()
        else:
            if edit_line == -1:
                txt.append(s)
            else:
                txt.insert(edit_line, s)
                edit_line += 1
    elif state == STATE_EDIT:
        if edit_line == -1:
            txt.append(s)
        else:
            txt.insert(edit_line, s)
            edit_line += 1


def state_edit():
    if state != STATE_EDIT:
        p("edit mode")
        state = STATE_EDIT


def state_eval():
    global state, edit_target, edit_min, edit_max, edit_line
    edit_target = None
    edit_min = None
    edit_max = None
    edit_line = -1
    if state != STATE_EVAL:
        state = STATE_EVAL
        p("repl mode")


def apply():
    if txt and edit_target:
        replacef(edit_target, edit_min, edit_max, txt)
    state_eval()


def append(fname):
    if txt and fname:
        appendf(fname, txt)
    state_eval()


def write(fname):
    if txt and fname:
        writef(fname, txt)
    state_eval()


def edit(fname, min=None, max=None):
    global state, edit_target, edit_min, edit_max, txt
    try:
        f = open(fname, "r")
        f.close()
    except:
        p("file not found")
        return

    state = STATE_EDIT
    v = [s.rstrip() for s in open(fname, "r").readlines()]
    if min is None:
        min = 0
    if max is None:
        max = len(v)
    if len(v) < min:
        min = len(v)
    if len(v) < max:
        max = len(v)
    txt = v[min:max]
    edit_target, edit_min, edit_max = fname, min, max


def ls():
    for name in os.listdir():
        try:
            f = open(name, "r")
            p(name, len(f.readlines()))
            f.close()
        except:
            p(name, "???")


def editdef(fun_name, file_name=None):
    v = list(finddef(fun_name, file_name))
    if not v:
        p("function not found")
        return
    file_name, min, defun = v[0]
    max = min + paragraph_len(file_name, min)

    edit(file_name, min, max)


# todo
# $k without parameter should kill the current line, not last
# magic command to extend from defun editing to file editing?
# magic command to restrict to defun editing in current file?
# simple substitution command
# magic command for deleting line and editing in its place (combining $k and $e)
