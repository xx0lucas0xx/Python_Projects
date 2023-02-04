#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Python:   3.10.7
#
# Author:   Lucas K. English
#
# Purpose:  To test using sqlite with test table
#
# Tested OS:  This code was written and tested to work with Windows 11.

import sqlite3
connection = sqlite3.connect("C:/Users/spike/Documents/GitHub/Tech-Academy-Projects/Python_Projects/database_Roster.db")

# allows dev to control a db
c = connection.cursor()

# creating and adding fields Name, Species, and IQ to database table
c.execute("CREATE TABLE Roster(Name TEXT, Species TEXT, IQ INT)")


# populate table
c.execute("INSERT INTO Roster VALUES('Jean-Baptiste Zorg', 'Human', 122), ('Korben Dallas', 'Meat Popsicle', 100), ('Aknot', 'Mangalore', -5)")
connection.commit()


# updating Species of Korben Dallas to Human
c.execute("UPDATE Roster SET Name=? AND Species=?",
          ( 'Korben Dallas', 'Human'))

# closing connection
connection.close()

# displays all tuples of Roster
c.execute("SELECT * FROM Roster")




