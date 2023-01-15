#
# Python:   3.10.7
#
# Author:   Lucas K. English
#
# Purpose:  To look through the Script_Asng folder, identify the txt. documents,
#  and print those qualifying file names and their corresponding modified time-stamps to the console.
#


import os
import time

for file in os.listdir(os.getcwd()):
    if file.endswith(".txt"):
        print(os.path.join(file))
        print(os.path.getmtime(file))
        
