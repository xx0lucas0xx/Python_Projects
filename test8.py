#
# Python:   3.10.7
#
# Author:   Lucas K. English
#
# Purpose:  Learning to deal with databases in python
#  
#


import sqlite3

conn = sqlite3.connect('test.db')

with conn: #building tbl_persons
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_persons ( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fname TEXT, \
        cole_lname TEXT, \
        col_email TEXT \
        )")
    conn.commit()
conn.close()


conn = sqlite3.connect('test.db')

with conn: #adding info into tbl_persons
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_persons(col_fname, cole_lname, col_email) VALUES (?, ?, ?)", \
                ('McKay', 'Swanson', 'brodude@man.com'))
    cur.execute("INSERT INTO tbl_persons(col_fname, cole_lname, col_email) VALUES (?, ?, ?)", \
                ('Devin', 'Kanter', 'manlyman@gmail.com'))
    cur.execute("INSERT INTO tbl_persons(col_fname, cole_lname, col_email) VALUES (?, ?, ?)", \
                ('Meow', 'Meow', 'meowmeow@coolcatz.com'))
    conn.commit()
conn.close()


conn = sqlite3.connect('test.db')

with conn:
    cur = conn.cursor()
    cur.execute("SELECT col_fname,cole_lname,col_email FROM tbl_persons WHERE col_fname = 'Adam'")
    varPerson = cur.fetchall()
    for item in varPerson:
        msg = "First Name: {}\nLast Name: {}\nEmail: {}".format(item[0],item[1],item[2])
    print(msg)
                        










                
