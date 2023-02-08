#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Python:   3.10.7
#
# Author:   Lucas K. English
#
# Purpose:  To create a program that creates a basic html file
#
# Tested OS:  This code was written and tested to work with Windows 11.

import tkinter as tk
from tkinter import *
import webbrowser

# Setting up GUI
class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")

        # adding button for default HTML page
        self.btn = Button(self.master, text = "Default HTML Page", width = 30, height = 2, command=self.defaultHTML)
        self.btn.grid(row =1, column = 0, padx = (10, 10), pady = (10, 10),sticky = E + S)

        # adding button for custom HTML page
        self.btn = Button(self.master, text = "Submit Custom Text", width = 30, height = 2, command=self.customHTML)
        self.btn.grid(row = 1, column = 1, padx = (10, 10), pady = (10, 10),sticky = E + S)

        
        # adding text entry
        self.txtEntry = Entry(self.master, font=("Helvetica", 12))
        self.txtEntry.grid(row = 2, column = 0, padx = (30, 15), pady = (10, 10), columnspan = 3, sticky = W + E)
   
    # adding functionality to the default html button
    def defaultHTML(self):
        htmlText = "We're having a great time aren't we?"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")


    # adding functionality to the custom HTML page
    def customHTML(self):
        htmlFile = open("index.html", "w")
        entry = self.txtEntry.get()
        htmlContent = "<html>\n<body>\n<h1>" + entry + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")


    

        

        





















    

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
    
