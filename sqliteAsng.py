#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Python:   3.10.7
#
# Author:   Lucas K. English
#
# Purpose:  To test using sqlite in IDLE
#
# Tested OS:  This code was written and tested to work with Windows 11.


import sqlite3
connection = sqlite3.connect("C:/Users/spike/Documents/GitHub/Tech-Academy-Projects/Python_Projects/test_database.db")

# allows dev to control a db
c = connection.cursor()

# creating a table 
c.execute("CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT)")
    #<sqlite3.Cursor object at 0x000002BBB857CA40>

# adding values to the tables
c.execute("INSERT INTO People VALUES('James', 'Tucker', 28)")
    #<sqlite3.Cursor object at 0x000002BBB857CA40>
connection.commit()

connection = sqlite3.connect(':memory:')
c.execute("DROP TABLE IF EXISTS People")
    #<sqlite3.Cursor object at 0x000002BBB857CA40>

# closes connection to the db and commits all changes made
#connection.close()
#with sqlite3.connect("test_database.db") as connection:
    # perform any SQL operations using connection here

# adding a multi line code to test in idle
import sqlite3
with sqlite3.connect('test_database.db') as connection:
    c = connection.cursor()
    c.executescript("""DROP TABLE IF EXISTS People;
                    CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT);
                    INSERT INTO People VALUES('James', 'Tucker', '28');
                    """)



import sqlite3

# get user data to insert into a tuple
firstName =input("Enter your first name: ")
lastName = input("Enter your last name: ")
age = int(input("Enter your age: "))
personData = (firstName, lastName, age)

# execute insert statement for supplied person data
with sqlite3.connect('test_database.db') as connection:
    c = connection.cursor()
    c.execute("INSERT INTO People VALUES(?, ?, ?)", personData)


# updating a tuple
c.execute("UPDATE People SET Age=? AND LastName=?",
          (28, 'Luigi', 'Spaget'))

# adding multipul values at once
peopleValues = (('James', 'Tucker', 28), ('Luigi', 'Spaget', 28), ('Mario', 'Pasta', 32))

# redoing table People
with sqlite3.connect('test_database.db') as connection:
                c = connection.cursor()
                c.execute("DROP TABLE IF EXISTS People")
                c.execute("CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT)")
                c.executemany("INSERT INTO People VALUES (?, ?, ?)",
                              peopleValues)

# select all first an last names from people over age 30
c.execute("SELECT FirstName, LastName FROM People where Age > 30")
for row in c.fetchall():
    print(row)

c.execute("SELECT FirstName, LastName FROM people WHERE Age > 30")
while True:
    row = c.fetchone()
    if row is None:
        break
    print(row)
