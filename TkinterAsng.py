#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Python:   3.10.7
#
# Author:   Lucas K. English
#
# Purpose:  To make use of the Tkinter module
#
# Tested OS:  This code was written and tested to work with Windows 11.

from tkinter import *

# creates a window
win = Tk()

# making buttons
b1 = Button(win, text="One")
b2 = Button(win, text="Two")


# packing buttons so they show up side by side,
# pushed to the left, then adding padding
b1.pack(side=LEFT, padx = 10)
b2.pack(side=LEFT, padx = 10)


# New win: making two by two gird layout with buttons
win = Tk()
b1 = Button(win, text="One")
b2 = Button(win, text="Two")
b1.grid(row=0, column=0)
b2.grid(row=1, column=1)

# adding label widget to window
l = Label(win, text="This is a label")
l.grid(row=1, column=0)

# New win: using Frames
win = Tk()
f = Frame(win)
b1 = Button(f, text="One")
b2 = Button(f, text="Two")
b3 = Button(f, text="Three")

# packing buttons so they are pushed to the left side
b1.pack(side=LEFT)
b2.pack(side=LEFT)
b3.pack(side=LEFT)
l = Label(win, text="This label is over all buttons")
l.pack()
f.pack()

# passing a keyword to its configure method
b1.configure(text="Uno")

# using the command parameter to print a method
def but1():
    print("Button one was pushed")

b1.configure(command=but1)


# New win: making new window with entry field
win = Tk()
v = StringVar()
e = Entry(win, textvariable = v)
e.pack()

# gets what was in entry field
v.get()

# sets text into StringVar object to appear as entry
v.set("this is set by the program")

# New win: using the height parameter to limit how many lines are shown
win = Tk()
lb = Listbox(win, height=3)
lb.pack()
lb.insert(END, "first entry")
lb.insert(END, "second entry")
lb.insert(END, "third entry")
lb.insert(END, "fourth entry")

# making scroll bar
sb = Scrollbar(win, orient = VERTICAL)
sb.pack(side = LEFT, fill = Y)

# adding usability to the scroll bar
sb.configure(command = lb.yview)
lb.configure(yscrollcommand = sb.set)

# returns selected item (and their tuple if one is present)
lb.curselection()

 



