#
# Python:   3.10.7
#
# Author:   Lucas K. English
#
# Purpose:  Learning to deal with databases in python
#  
#


import sqlite3

conn = sqlite3.connect('test1.db')

with conn: #building tbl_files
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files ( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        fileList TEXT)")
    conn.commit()
conn.close()


conn = sqlite3.connect('test1.db')

# List of the file names
fileNames = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')


# loop through each object in the tuple to find all .txt files.
for x in fileNames:
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()
        # The value for each row will one file out of the tuple therfore (x,)
        # Will denote a one element tuple for each .txt file
            cur.execute("INSERT INTO tbl_files(fileList) VALUES (?)", (x,))
            print(x)
conn.close()
            









