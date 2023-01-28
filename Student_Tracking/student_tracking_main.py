#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Python:   3.10.7
#
# Author:   Lucas K. English
#
# Purpose:  To make a student program gui with info inputs, a submission and a
#           delete function.
#
# Tested OS:  This code was written and tested to work with Windows 11.

from tkinter import *
import tkinter as tk
from tkinter import messagebox

# Importing modules

import student_tracking_gui
import student_tracking_func

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # set frame size
        self.master = master
        self.master.minsize(600, 400) # (height, width)
        self.master.maxsize(600, 400) #

        # CenterWindow method will center our app on the user's screen
        student_tracking_func.center_window(self,600,400)
        self.master.title("Student Tracker")
        self.master.configure(bg= "#AFC9D8")

        # the user clicks the upper corner, "X" on Windows OS.
        self.master.protocol("WM_DELETE_WINDOW", lambda: student_tracking_func.ask_quit(self))
        arg = self.master

        # load in the GUI widgets from a separate module, 
        student_tracking_gui.load_gui(self)

        # Instantinate the Tkinter menue dropdown object
        # This is the menu that will appear at the top of our window
        menubar = Menu(self.master)
        filemenu = Menu(menubar, tearoff = 0)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", underline=1,accelerator="Ctrl+Q",command=lambda: student+tracking_func.ask_quit(self))
        menubar.add_cascade(label="File", underline=0, menu=filemenu)
        helpmenu = Menu(menubar, tearoff=0) # defines the particular drop down colum and tearoff=0 means do not separate from menubar
        helpmenu.add_separator()
        helpmenu.add_command(label="How to use this program")
        helpmenu.add_separator()
        helpmenu.add_command(label="About This student tracker") # add_command is a child menubar item of the add_cascde parent item
        menubar.add_cascade(label="Help", menu=helpmenu) # add_cascade is a parent menubar item (visible heading)
        
        self.master.config(menu=menubar, borderwidth='1')


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()

        



