#!/usr/bin/python3

import tkinter as tk
import os
import re
import random

list_order = []
gif_list = []

exec(open("./list.py").read())

digits_set = set(str(x) for x in range(10))

gif_list = [s for s in gif_list if not (set(s) & digits_set)]
print(len(gif_list))

if os.path.isfile("list_order.py"):
    exec(open("list_order.py"). read())
else:
    list_order = list(range(0, len(gif_list)))
    print(len(gif_list))
    print(list_order)
    random.shuffle(list_order)

for i in range(len(list_order), len(gif_list)):
    list_order.insert(0, i)

original_count = len(gif_list)
root = tk.Tk()
root.title("member-berry")
panel = False
img = False
id_text = False

edit_box = False


def rootQuit():
    saveInfoFile()
    saveListOrder()
    root.destroy()


def readInfoFile():
    s = gif_list[list_order[0]] + ".txt"
    if os.path.exists(s):
        ret_s = open(s).read()
        return ret_s

    return ""


def saveListOrder():
    f = open("list_order.py", "w")
    f.write("list_order = " + str(list_order))
    f.close()


def saveHaveBeenLog(dif):
    with open("have_been.txt", "a") as f:
        f.write("%20s - %7s\n" % (Name(), dif))


def saveInfoFile():
    if edit_box:
        s = gif_list[list_order[0]] + ".txt"
        txt = edit_box.get("1.0", "end-1c")
        if txt != "":
            f = open(s, "w")
            f.write(txt)
            f.close()
        elif os.path.exists(s):
            os.remove(s)


def Name():
    s = gif_list[list_order[0]]
    s = re.sub(r"\.gif", "", s)
    s = re.sub("[_]+", " ", s)
    return s


def setName(s):
    if button_1_string:
        button_1_string.set(s)


def printName():
    s = Name()
    setName(s)


def destroy(x):
    if x:
        x.destroy()


def makeGetActorImage():
    older_pic = ""
    pic_count = 0

    def lastActorPicCount():
        return pic_count

    def f(current_actor):
        nonlocal older_pic, pic_count
        s = gif_list[current_actor]
        v = [s]
        for i in range(20):
            s2 = (s[::-1].replace(".", ("%d." % i)[::-1], 1))[::-1]
            if os.path.isfile(s2):
                v.append(s2)

        pic_count = len(v)

        if older_pic in v:
            older_pic = v[(v.index(older_pic) + 1) % len(v)]
        else:
            older_pic = v[random.randint(0, len(v) - 1)]
        return older_pic
    return f, lastActorPicCount


getActorImage, getActorPicCount = makeGetActorImage()


def imageClickEvent(event=None):
    k = getActorPicCount()
    if k > 1:
        makeImage()


def makeImage(update_img=True):
    global panel, img, id_text
    global edit_checkbox_var, edit_box
    setName("my name is")

    to_destroy = [panel, id_text, edit_box]

    if update_img:
        img = tk.PhotoImage(file=getActorImage(list_order[0]))
    panel = tk.Frame(root)
    panel.pack(side=tk.BOTTOM)
    image = tk.Label(panel, image=img)
    image.bind("<Button-1>", imageClickEvent)

    id_text = tk.Label(panel, text="%d/%d" % (getActorPicCount(), len(gif_list)))

    if edit_checkbox_var.get() == "1":
        edit_box = tk.Text(panel, height=8, width=30)
        edit_box.insert(tk.END, readInfoFile())
        edit_box.pack(side=tk.RIGHT)
    else:
        edit_box = False

    id_text.pack(side=tk.BOTTOM)
    image.pack(side=tk.BOTTOM, fill="both", expand="yes")

    for d in to_destroy:
        if d:
            destroy(d)


def ActorCommon(delta, dif):
    saveHaveBeenLog(dif)
    saveInfoFile()
    if delta > len(list_order):
        delta = len(list_order) - 2

    x = list_order[0]
    del (list_order[0])
    list_order.insert(delta, x)

    makeImage()


def ActorAgain():
    ActorCommon(random.randrange(int(len(list_order) * 0.08),
                                 int(len(list_order) * 0.12)), "again")


def ActorHard():
    ActorCommon(random.randrange(int(len(list_order) * 0.18),
                                 int(len(list_order) * 0.22)), "hard")


def ActorGood():
    ActorCommon(random.randrange(int(len(list_order) * 0.3),
                                 int(len(list_order) * 0.4)), "good")


def ActorEasy():
    ActorCommon(random.randrange(
        int(len(list_order) * 0.98), int(len(list_order))), "easy")


def EditCheckboxCommand():
    global edit_checkbox_var
    s = edit_checkbox_var.get()
    if s == "0":
        saveInfoFile()

    makeImage(False)


random.seed()
frame_but = tk.Frame(root)

frame_but.pack()  # (side = BOTTOM)


button_1_string = tk.StringVar()
button_1 = tk.Button(frame_but, textvariable=button_1_string,
                     command=printName)
button_1.pack(side=tk.TOP)


edit_checkbox_var = tk.StringVar()
edit_checkbox_var.set("0")
edit_checkbox = tk.Checkbutton(frame_but, variable=edit_checkbox_var,
                               command=EditCheckboxCommand)
edit_checkbox.pack(side=tk.RIGHT)


name_text_string = tk.StringVar()

button_2 = tk.Button(frame_but, text="easy", command=ActorEasy)
button_2.pack(side=tk.RIGHT)

button_3 = tk.Button(frame_but, text="good", command=ActorGood)
button_3.pack(side=tk.RIGHT)


button_4 = tk.Button(frame_but, text="hard", command=ActorHard)
button_4.pack(side=tk.RIGHT)


button_5 = tk.Button(frame_but, text="again", command=ActorAgain)
button_5.pack(side=tk.RIGHT)


makeImage()

root.protocol("WM_DELETE_WINDOW", rootQuit)
root.mainloop()
