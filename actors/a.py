#!/usr/bin/python3

from tkinter import *
import os
import re


from random import shuffle, seed

gif_list = []
exec(open("./list.py").read())
shuffle(gif_list)


original_count = len(gif_list)
root = Tk()
root.title("member-berry")
panel = False
img = False
current_actor = 0
id_text = False
id_text_string = False

edit_box = False
edit_box_str = False


def rootQuit():
    saveInfoFile()
    root.destroy()


def readInfoFile():
    s = gif_list[current_actor] + ".txt"
    if os.path.exists(s):
        ret_s = open(s).read()
        return ret_s

    return ""


def saveInfoFile():
    if edit_box:
        s = gif_list[current_actor] + ".txt"
        txt = edit_box.get("1.0", "end-1c")
        if txt != "":
            f = open(s, "w")
            f.write(txt)
            f.close()
        elif os.path.exists(s):
            os.remove(s)


def idText():
    if id_text_string:
        count = len(gif_list)
        s = "%d-%d" % (current_actor + 1, count)
        if count != original_count:
            s += "(%d)" % original_count

        id_text_string.set(s)


def setName(s):
    if button_1_string:
        button_1_string.set(s)


def printName():
    s = gif_list[current_actor]
    gif_list.append(s)

    s = re.sub(r"\.gif", "", s)
    s = re.sub("[_]+", " ", s)
    setName(s)
    idText()


def destroy(x):
    if x:
        x.destroy()


def getActorImage():
    s = gif_list[current_actor]
    v = [s]
    for i in range(20):
        s2 = s.replace(".", "%d." % i)
        if os.path.isfile(s2):
            v.append(s)
    return v[randint(len(v))]


def makeImage():
    global panel, img, id_text, id_text_string
    global edit_box_str, edit_box
    setName("my name is")

    destroy(panel)
    destroy(id_text)
    destroy(edit_box)

    img = PhotoImage(file=gif_list[current_actor])
    panel = Frame(root)
    panel.pack(side=BOTTOM)
    image = Label(panel, image=img)

    id_text_string = StringVar()
    id_text = Label(panel, textvariable=id_text_string)

    edit_box = Text(panel, height=8, width=30)
    edit_box.insert(END, readInfoFile())

    idText()

    edit_box.pack(side=RIGHT)
    id_text.pack(side=BOTTOM)
    image.pack(side=BOTTOM, fill="both", expand="yes")


def prevActor():
    global current_actor
    if current_actor > 0:
        saveInfoFile()
        current_actor -= 1
        makeImage()


def nextActor():
    global current_actor
    saveInfoFile()
    current_actor += 1
    if current_actor >= len(gif_list):
        root.quit()
    else:
        makeImage()


seed()
frame_but = Frame(root)

frame_but.pack()  # (side = BOTTOM)

button_1_string = StringVar()
button_1 = Button(frame_but, textvariable=button_1_string, command=printName)
button_1.pack(side=TOP)

name_text_string = StringVar()

button_2 = Button(frame_but, text="next", command=nextActor)
button_2.pack(side=RIGHT)

button_3 = Button(frame_but, text="previous", command=prevActor)
button_3.pack(side=RIGHT)


makeImage()

root.protocol("WM_DELETE_WINDOW", rootQuit)
root.mainloop()
